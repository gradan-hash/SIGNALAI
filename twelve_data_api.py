#!/usr/bin/env python3
"""
Twelve Data API integration for SignalAI
Handles real market data with proper rate limiting
"""

import requests
import time
from datetime import datetime, date
from typing import Dict, Any, Optional

# Twelve Data API configuration
TWELVE_DATA_API_KEY = "75f27ed4144449b1a06748691a937a63"
TWELVE_DATA_BASE_URL = "https://api.twelvedata.com"

# Rate limiting globals
twelve_data_request_count = 0
twelve_data_minute_requests = []
last_reset_date = str(date.today())
MAX_REQUESTS_PER_MINUTE = 7  # Conservative (8 max)
MAX_REQUESTS_PER_DAY = 750   # Conservative (800 max)
RATE_LIMIT_DELAY = 8         # Seconds between requests

def reset_daily_counters():
    """Reset request counters if it's a new day"""
    global last_reset_date, twelve_data_request_count
    today = str(date.today())
    if today != last_reset_date:
        print(f"🔄 New day detected! Resetting Twelve Data request counters...")
        twelve_data_request_count = 0
        last_reset_date = today
        print(f"📊 Fresh limits: {MAX_REQUESTS_PER_DAY} requests per day, {MAX_REQUESTS_PER_MINUTE} per minute")

def check_twelve_data_rate_limit():
    """
    Check if we can make a request to Twelve Data API
    Enforces 8 requests/minute and 800 requests/day limits
    """
    global twelve_data_request_count, twelve_data_minute_requests
    
    # Reset counters if new day
    reset_daily_counters()
    
    # Check daily limit
    if twelve_data_request_count >= MAX_REQUESTS_PER_DAY:
        print(f"⚠️ Daily limit reached ({twelve_data_request_count}/{MAX_REQUESTS_PER_DAY}), switching to AI fallback")
        return False
    
    # Check minute limit by removing requests older than 1 minute
    now = time.time()
    twelve_data_minute_requests = [req_time for req_time in twelve_data_minute_requests if now - req_time < 60]
    
    if len(twelve_data_minute_requests) >= MAX_REQUESTS_PER_MINUTE:
        wait_time = 60 - (now - twelve_data_minute_requests[0]) + 1
        print(f"⚠️ Minute limit reached, waiting {wait_time:.0f} seconds...")
        time.sleep(wait_time)
        return check_twelve_data_rate_limit()  # Recheck after waiting
    
    return True

def record_twelve_data_request():
    """Record a successful request for rate limiting"""
    global twelve_data_request_count, twelve_data_minute_requests
    twelve_data_request_count += 1
    twelve_data_minute_requests.append(time.time())
    print(f"📊 Request recorded: {twelve_data_request_count}/{MAX_REQUESTS_PER_DAY} daily, {len(twelve_data_minute_requests)}/{MAX_REQUESTS_PER_MINUTE} per minute")

def get_twelve_data_quote(symbol: str, asset_type: str) -> Optional[Dict[str, Any]]:
    """
    Get real market data from Twelve Data API
    Returns formatted data or None if failed
    """
    
    if not check_twelve_data_rate_limit():
        return None
    
    try:
        # Add delay to respect rate limits
        time.sleep(RATE_LIMIT_DELAY)
        
        # Format symbol for Twelve Data
        if asset_type == "forex":
            # Special handling for XAUUSD (Gold) - keep slash format
            if symbol in ["XAUUSD", "XAU/USD"]:
                symbol = "XAU/USD"  # Twelve Data format for gold
            # For other forex pairs, ensure they have slash format
            elif "/" not in symbol and len(symbol) == 6:
                # Convert EURUSD to EUR/USD format
                symbol = f"{symbol[:3]}/{symbol[3:]}"
        
        # Make API request
        url = f"{TWELVE_DATA_BASE_URL}/quote"
        params = {
            "symbol": symbol,
            "apikey": TWELVE_DATA_API_KEY
        }
        
        print(f"📡 Fetching real {asset_type} data for {symbol} from Twelve Data...")
        response = requests.get(url, params=params, timeout=10)
        data = response.json()
        
        # Check for errors
        if "error" in data:
            print(f"❌ Twelve Data API error: {data['error']}")
            return None
        
        if "status" in data and data["status"] == "error":
            print(f"❌ Twelve Data error: {data.get('message', 'Unknown error')}")
            return None
        
        # Record successful request
        record_twelve_data_request()
        
        # Parse response
        if not data or "symbol" not in data:
            print(f"⚠️ Invalid response format from Twelve Data for {symbol}")
            return None
            
        # Extract data
        current_price = float(data.get("close", 0))
        previous_close = float(data.get("previous_close", current_price))
        
        # Calculate change
        change = current_price - previous_close
        change_percent = (change / previous_close * 100) if previous_close != 0 else 0.0
        
        # Return formatted data
        formatted_data = {
            "symbol": symbol,
            "price": current_price,
            "change": change,
            "change_percent": change_percent,
            "volume": int(data.get("volume", 0)),
            "timestamp": data.get("datetime", datetime.now().isoformat()),
            "source": "Twelve Data"
        }
        
        print(f"✅ Got real data for {symbol}: ${current_price:.4f} ({change_percent:+.2f}%)")
        return formatted_data
        
    except Exception as e:
        print(f"❌ Error fetching data for {symbol}: {str(e)}")
        return None

def test_twelve_data_api():
    """Test the Twelve Data API with sample requests"""
    print("🧪 Testing Twelve Data API...")
    
    test_symbols = [
        ("AAPL", "stock"),
        ("EUR/USD", "forex"), 
        ("XAU/USD", "forex")  # Gold
    ]
    
    for symbol, asset_type in test_symbols:
        print(f"\n🔍 Testing {symbol} ({asset_type})")
        result = get_twelve_data_quote(symbol, asset_type)
        if result:
            print(f"✅ Success: {result['symbol']} = ${result['price']:.4f}")
        else:
            print(f"❌ Failed to get data for {symbol}")

if __name__ == "__main__":
    test_twelve_data_api()
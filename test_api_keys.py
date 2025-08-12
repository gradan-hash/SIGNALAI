#!/usr/bin/env python3
import requests
import time
from datetime import datetime

# Your API keys
API_KEYS = [
    "Y1E0SFES4O0ATXVZ",  # Key 1
    "QEAE2D1SZUNB85O4",  # Key 2  
    "XAG63SKT2UM5JICF",  # Key 3
]

def test_api_key(api_key, key_number):
    """Test a single API key with a simple request"""
    print(f"\n🔑 Testing API Key {key_number} (ending in ...{api_key[-4:]})")
    
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=AAPL&apikey={api_key}"
    
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        
        print(f"📡 Response Status: {response.status_code}")
        
        if "Global Quote" in data:
            quote = data["Global Quote"]
            print(f"✅ Key {key_number} WORKING - AAPL: ${quote.get('05. price', 'N/A')}")
            return True
        elif "Note" in data:
            print(f"⚠️ Key {key_number} RATE LIMITED - {data['Note']}")
            return False
        elif "Error Message" in data:
            print(f"❌ Key {key_number} ERROR - {data['Error Message']}")
            return False
        elif "Information" in data:
            print(f"⚠️ Key {key_number} INFO - {data['Information']}")
            return False
        else:
            print(f"🤔 Key {key_number} UNKNOWN RESPONSE - {data}")
            return False
            
    except Exception as e:
        print(f"❌ Key {key_number} FAILED - {str(e)}")
        return False

def main():
    print(f"🧪 Testing Alpha Vantage API Keys")
    print(f"⏰ Test Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"🔑 Total Keys: {len(API_KEYS)}")
    
    working_keys = 0
    
    for i, key in enumerate(API_KEYS, 1):
        if test_api_key(key, i):
            working_keys += 1
        
        # Wait 12 seconds between requests to respect rate limits
        if i < len(API_KEYS):
            print("⏳ Waiting 12 seconds (rate limit compliance)...")
            time.sleep(12)
    
    print(f"\n📊 Results Summary:")
    print(f"✅ Working Keys: {working_keys}/{len(API_KEYS)}")
    print(f"❌ Failed Keys: {len(API_KEYS) - working_keys}/{len(API_KEYS)}")
    
    if working_keys == 0:
        print("\n💡 Possible Issues:")
        print("   - All keys hit daily 25-request limit")
        print("   - Keys are invalid or suspended") 
        print("   - IP-based rate limiting")
        print("   - Wait 24 hours and try again")

if __name__ == "__main__":
    main()
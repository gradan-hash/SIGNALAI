# 🚀 Signal AI - Financial Intelligence Platform

Transform market noise into actionable trading insights using AI-powered agents and beautiful dashboards.

![Signal AI Dashboard](https://img.shields.io/badge/Signal%20AI-1.0.0-purple?style=for-the-badge&logo=chartdotjs)
![Vue 3](https://img.shields.io/badge/Vue.js-3.4-4FC08D?style=for-the-badge&logo=vue.js&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Gemini AI](https://img.shields.io/badge/Google%20Gemini-AI%20Powered-orange?style=for-the-badge&logo=google&logoColor=white)

## 💡 The Problem We Solve

**Retail investors are drowning in financial noise.**

- Bloomberg Terminal: $24,000/year (out of reach)
- Free platforms: Too much noise, no insights
- **Signal AI: $29/month** - Professional insights at retail prices

## 🎯 What Signal AI Does

**Input:** Stock symbols (AAPL, TSLA, NVDA...)  
**Output:** Clear, actionable trading insights delivered 30 minutes before market open

### Pre-Market Intelligence Delivered:
- 📈 **Top Movers & Why** - Biggest gainers/losers with explanations
- 🎯 **Trading Signals** - Bullish/bearish setups with confidence scores
- 📰 **News Impact Analysis** - How headlines affect stock prices  
- ⚠️  **Risk Alerts** - Market events that could cause volatility
- 💎 **Opportunities** - Undervalued stocks with catalysts

## 🏗️ Architecture - Multi-Agent System

Based on the proven **Digital Artisan's Forge** pattern with 4 specialized AI agents:

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│  Market Data    │───▶│ News Synthesis  │───▶│ Signal Analysis │───▶│   Dashboard     │
│     Agent       │    │     Agent       │    │     Agent       │    │     Agent       │
└─────────────────┘    └─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │                       │
         ▼                       ▼                       ▼                       ▼
   Real-time prices      Financial news         Trading signals        Beautiful UI
   Volume analysis       Sentiment scores       Risk assessments       Mobile-ready
   Technical levels      Market themes          Price targets          Auto-refresh
```

### Agent Responsibilities:

1. **Market Data Agent** 🔍
   - Pulls real-time stock prices, volume, pre-market movers
   - Uses Gemini's web search for current market data
   - Identifies unusual trading activity

2. **News Synthesis Agent** 📰  
   - Aggregates financial news from multiple sources
   - Analyzes sentiment impact on stock prices
   - Filters noise to highlight market-moving stories

3. **Signal Analysis Agent** 🎯
   - Transforms data into actionable trading insights
   - Provides "WHAT, WHY, SO WHAT" for each signal
   - Generates confidence scores and price targets

4. **Dashboard Agent** 📱
   - Formats insights for beautiful Vue 3 dashboard
   - Creates mobile-friendly, scannable layouts
   - Optimizes for quick decision-making

## 🚀 Quick Start

### 1. Environment Setup

```bash
# Clone or create the Signal AI directory
cd /path/to/SIGNALAI

# Create virtual environment
python -m venv signal_env
source signal_env/bin/activate  # On Windows: signal_env\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. API Configuration

```bash
# Copy environment template
cp .env.example .env

# Edit .env with your API keys
nano .env
```

Add your Google Gemini API key:
```env
GOOGLE_API_KEY=your_actual_google_api_key_here
```

### 3. Test the Agents

```bash
# Test all financial agents
python financial_agents.py

# Run complete pipeline
python signal_pipeline.py --symbols AAPL,TSLA,NVDA

# Pre-market mode (run 30 mins before market open)
python signal_pipeline.py --premarket
```

### 4. Launch Dashboard

```bash
# Navigate to dashboard
cd dashboard

# Install Vue dependencies
npm install

# Start development server
npm run dev

# Dashboard will be available at http://localhost:5173
```

## 📊 Dashboard Features

### Beautiful, Mobile-First Design
- **Dark theme** optimized for traders
- **Real-time updates** every 15 minutes
- **Responsive layout** works on all devices
- **Gradient animations** and smooth transitions

### Key Components:
- 🎯 **Hero Metrics** - Market sentiment, active signals, opportunities
- 📈 **Signal Cards** - Individual stock insights with strength indicators
- 🌍 **Market Themes** - Sector trends (AI, EV, etc.)
- ⚠️  **Risk Alerts** - Fed meetings, earnings, volatility warnings

## ⚡ Usage Examples

### Basic Analysis
```bash
# Analyze top tech stocks
python signal_pipeline.py --symbols AAPL,MSFT,GOOGL,NVDA

# Get broader market view
python signal_pipeline.py --symbols SPY,QQQ,IWM,VIX
```

### Pre-Market Intelligence
```bash
# Run 30 minutes before market open (8:30 AM EST)
python signal_pipeline.py --premarket

# This generates insights for:
# - Pre-market movers
# - Overnight news impact  
# - Day trading setups
# - Risk events to watch
```

### Custom Symbol Lists
```bash
# Analyze your watchlist
python signal_pipeline.py --symbols TSLA,AMD,CRM,PLTR,ROKU

# Focus on specific sectors
python signal_pipeline.py --symbols XLK,XLF,XLE,XLV  # Tech, Finance, Energy, Health
```

## 🔄 Automation & Scheduling

### Pre-Market Automation (Recommended)
Set up a cron job to run Signal AI 30 minutes before market open:

```bash
# Edit crontab
crontab -e

# Add this line (runs at 8:30 AM EST, Monday-Friday)
30 8 * * 1-5 cd /path/to/SIGNALAI && python signal_pipeline.py --premarket
```

### Continuous Updates
For live trading during market hours:

```bash
# Update every 15 minutes during market hours (9:30 AM - 4:00 PM EST)
*/15 9-16 * * 1-5 cd /path/to/SIGNALAI && python signal_pipeline.py
```

## 📝 Configuration

### `signal_config.json` - Main Settings
```json
{
  "default_symbols": ["AAPL", "TSLA", "NVDA", "MSFT", "SPY", "QQQ"],
  "premarket_time": "08:30",
  "refresh_interval": 15,
  "trading_settings": {
    "min_signal_strength": 70,
    "max_risk_level": "high"
  },
  "notification_settings": {
    "premarket_alert": true,
    "high_signal_alert": true
  }
}
```

### Key Settings:
- **default_symbols**: Stocks to analyze by default
- **min_signal_strength**: Only show signals above this confidence level
- **premarket_time**: When to run pre-market analysis
- **notification_settings**: Email/webhook alerts

## 🎯 Business Model & ROI

### Target Market: "Prosumer Traders"
- More sophisticated than beginners
- Don't have Bloomberg Terminal budget
- Want professional-grade insights
- Willing to pay for quality analysis

### Pricing Strategy:
- **Signal AI**: $29/month
- **Bloomberg Terminal**: $24,000/year  
- **Our advantage**: 1/83rd the cost!

### Revenue Projections:
- 100 users: $2,900/month = $34,800/year
- 1,000 users: $29,000/month = $348,000/year  
- 10,000 users: $290,000/month = $3,480,000/year

### Expansion Path:
1. **Phase 1**: Stocks (Current)
2. **Phase 2**: Forex currencies  
3. **Phase 3**: Cryptocurrency
4. **Phase 4**: Options trading signals

## 🔧 Development

### Project Structure
```
SIGNALAI/
├── financial_agents.py        # Core AI agents
├── signal_pipeline.py         # Main orchestrator
├── signal_config.json         # Configuration
├── requirements.txt           # Python dependencies
├── .env.example              # Environment template
├── dashboard/                # Vue 3 frontend
│   ├── src/
│   │   ├── App.vue          # Main dashboard component
│   │   ├── main.js          # Vue app entry
│   │   └── style.css        # Global styles
│   ├── index.html           # HTML template
│   └── package.json         # Node dependencies
└── backups/                 # Historical insights
```

### Adding New Features

1. **New Agent**: Add to `financial_agents.py`
2. **Dashboard Component**: Create in `dashboard/src/components/`
3. **Configuration**: Update `signal_config.json`
4. **Pipeline Step**: Modify `signal_pipeline.py`

### Testing
```bash
# Test individual agents
python -c "from financial_agents import test_all_agents; test_all_agents()"

# Test complete pipeline
python signal_pipeline.py --symbols AAPL

# Test dashboard (in dashboard/ directory)
npm run dev
```

## 🚨 Error Handling

### Common Issues:

1. **API Quota Exceeded**
   - Solution: Wait 24 hours or upgrade API plan
   - Tip: Run pre-market only to conserve quota

2. **No Market Data**
   - Check if markets are open
   - Verify symbol accuracy (AAPL, not Apple)

3. **Dashboard Not Loading**
   - Ensure `insights.json` exists in `dashboard/public/data/`
   - Run pipeline first to generate data

## 📈 Performance Metrics

### Agent Execution Times:
- Market Data Agent: ~10-15 seconds
- News Synthesis Agent: ~15-20 seconds  
- Signal Analysis Agent: ~20-25 seconds
- Dashboard Agent: ~5-10 seconds
- **Total Pipeline**: ~60-90 seconds

### Accuracy Targets:
- Signal accuracy: >65% (target: 70%+)
- News relevance: >80%
- Market trend prediction: >60%

## 🔒 Security & Privacy

- **API Keys**: Stored in `.env` (never committed)
- **Data**: Processed locally, not stored externally
- **Privacy**: No user trading data collected
- **Updates**: Secure HTTPS connections only

## 🛣️ Roadmap

### Version 1.1 (Next 30 days)
- [ ] Options flow analysis
- [ ] Social sentiment integration
- [ ] Email notifications
- [ ] Performance tracking

### Version 1.2 (Next 60 days)  
- [ ] Forex currency pairs
- [ ] Crypto integration
- [ ] Mobile app (React Native)
- [ ] Backtesting engine

### Version 2.0 (Next 90 days)
- [ ] Machine learning models
- [ ] Portfolio optimization
- [ ] Risk management tools
- [ ] Subscription management

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Create Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Digital Artisan's Forge** - Architecture inspiration
- **Google Gemini** - AI processing power
- **Vue 3 & Tailwind CSS** - Beautiful, responsive UI
- **Financial community** - Feedback and validation

---

**🚀 Ready to turn market noise into trading signals?**

```bash
python signal_pipeline.py --premarket
```

**💰 Transform your trading with AI-powered insights.**

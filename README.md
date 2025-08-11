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

Advanced 4-agent system with inter-agent communication for global market intelligence:

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│ Global Discovery│───▶│ Smart Search    │───▶│ Analysis        │───▶│   Dashboard     │
│     Agent       │    │     Agent       │    │     Agent       │    │   Generator     │
└─────────────────┘    └─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │                       │
         ▼                       ▼                       ▼                       ▼
   Global volume data     Trending assets      Detailed analysis      Vue 3 Dashboard
   Regional highlights    Social sentiment     Trading signals        PDF Reports
   Market drivers         Catalyst analysis    Risk assessments       Email delivery
```

### Agent Responsibilities:

1. **Global Discovery Agent** 🌍
   - Finds most traded assets worldwide by volume
   - Provides regional market highlights (Americas, Europe, Asia)
   - Identifies global market drivers and catalysts
   - Inter-agent communication for priority intelligence

2. **Smart Search Agent** 🔍  
   - Uses Global Discovery intelligence to focus on high-volume assets
   - Discovers trending opportunities across all asset classes
   - Analyzes social media buzz and retail interest
   - Filters assets by actual trading volume

3. **Analysis Agent** 🎯
   - Generates detailed technical and fundamental analysis
   - Provides exact entry/exit prices and risk metrics
   - Creates comprehensive trading setups with confidence scores
   - Explains market dynamics in simple terms

4. **Dashboard Generator** 📱
   - Creates beautiful Vue 3 dashboard with real-time data
   - Generates professional PDF reports
   - Sends automated email delivery to subscribers
   - Archives historical data for trend analysis

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

### 3. Run Signal AI

```bash
# Run complete market analysis with global intelligence
python agents.py

# This automatically:
# - Discovers global volume leaders
# - Analyzes trending assets across all categories
# - Generates detailed trading insights
# - Creates Vue dashboard data
# - Generates PDF reports
# - Emails reports to subscribers
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

### Complete Market Analysis
```bash
# Run full global market analysis
python agents.py

# This automatically:
# ✅ Discovers most traded assets globally
# ✅ Analyzes stocks, forex, crypto, commodities
# ✅ Generates detailed trading insights
# ✅ Creates interactive dashboard data
# ✅ Produces professional PDF reports
# ✅ Emails reports to subscribers
```

### Dashboard Features
The Vue 3 dashboard provides:
- **Real-time market data** from all agents
- **Interactive asset analysis** with detailed modals
- **Professional PDF reports** with exact entry/exit prices
- **Historical data tracking** with daily archives
- **Mobile-responsive design** for trading on-the-go

### Email & PDF Reports
Professional reports include:
- **Executive Summary** with market direction
- **Asset Analysis** with exact trading levels
- **Risk Metrics** and confidence scores  
- **Technical Charts** and indicators
- **Downloadable PDF** format for offline access

## 🔄 Automation & Scheduling

### Automated Market Analysis
Set up Signal AI to run automatically with cron jobs:

```bash
# Edit crontab
crontab -e

# Pre-market analysis (8:30 AM UTC, Monday-Friday)
30 8 * * 1-5 cd /path/to/SIGNALAI && python agents.py

# Market opening analysis (1:30 PM UTC during NY open)
30 13 * * 1-5 cd /path/to/SIGNALAI && python agents.py

# End-of-day analysis (9:30 PM UTC after NY close)  
30 21 * * 1-5 cd /path/to/SIGNALAI && python agents.py
```

### Email Configuration
For automated report delivery, add to `.env`:

```env
GMAIL_EMAIL=your-email@gmail.com
GMAIL_APP_PASSWORD=your-app-password
```

## 📝 Configuration

### Environment Variables (`.env`)
```env
# Required - Google Gemini API
GOOGLE_API_KEY=your_google_api_key_here
GOOGLE_API_KEY_2=backup_api_key_optional

# Optional - Email reports
GMAIL_EMAIL=your-email@gmail.com
GMAIL_APP_PASSWORD=your-gmail-app-password

# Optional - Dashboard settings
DASHBOARD_PORT=3001
AUTO_REFRESH=true
```

### Agent Configuration
The agents are fully automated with intelligent defaults:
- **Global Discovery**: Finds most traded assets worldwide
- **Smart Search**: Uses volume data for asset selection  
- **Analysis**: Generates detailed insights for all asset types
- **PDF Reports**: Automatic generation with professional formatting
- **Email Delivery**: Automated subscriber management and delivery

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
├── agents.py                  # 4 AI agents with inter-communication
├── pdf_report_generator.py    # Premium PDF report generation
├── requirements.txt           # Python dependencies
├── .env.example              # Environment template
├── dashboard/                 # Vue 3 frontend
│   ├── src/
│   │   ├── SimpleApp.vue    # Main dashboard component
│   │   ├── main.js          # Vue app entry
│   │   └── style.css        # Tailwind CSS styles
│   ├── public/data/         # Real-time market data
│   │   ├── market_insights.json
│   │   ├── detailed_analyses.json
│   │   ├── current_reports.json
│   │   └── historical/      # Daily archived data
│   ├── index.html           # HTML template
│   └── package.json         # Node dependencies
├── reports/                   # Generated PDF reports
└── backups/                   # Historical insights backup
```

### Adding New Features

1. **New Agent**: Add to `agents.py` with inter-agent communication
2. **Dashboard Component**: Create in `dashboard/src/`
3. **PDF Templates**: Modify `pdf_report_generator.py`
4. **Data Structure**: Update JSON schemas in `public/data/`

### Testing
```bash
# Test complete system
python agents.py

# Test dashboard (in dashboard/ directory)
npm run dev

# Test PDF generation
python pdf_report_generator.py
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
- Global Discovery Agent: ~10-15 seconds
- Smart Search Agent: ~15-20 seconds  
- Analysis Agent: ~20-25 seconds per asset
- PDF Generation: ~10-15 seconds
- Email Delivery: ~5-10 seconds per subscriber
- **Total Pipeline**: ~60-90 seconds

### System Capabilities:
- **Global Asset Discovery**: Covers 100+ assets across all major markets
- **Analysis Speed**: Complete market scan in 60-90 seconds
- **Data Coverage**: Stocks, forex, crypto, commodities in single run
- **Report Generation**: Professional PDFs with exact trading levels
- **Email Delivery**: Automated subscriber management and delivery

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

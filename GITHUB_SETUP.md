# Signal AI - Complete GitHub Setup Guide

## 🏗️ **Architecture Overview:**
- **Frontend**: Vue.js dashboard deployed to GitHub Pages
- **Backend**: Python AI agents running on GitHub Actions
- **Email System**: Automated daily PDF reports to subscribers
- **Data Flow**: Agents → JSON files → Dashboard → Users

## 🚀 **Workflows Created:**

### 1. **Subscription Workflow** (`subscription.yml`)
- Triggered when users subscribe via frontend
- Automatically updates `subscribers.json` 
- No manual work required

### 2. **Signal Generation Workflow** (`signal-generation.yml`)
- Runs **twice daily** before markets open:
  - **8:30 AM UTC** (4:30 AM EST, 1:30 AM PST) - Pre-market signals
  - **1:00 PM UTC** (9:00 AM EST, 6:00 AM PST) - Before US market open
- Generates market analysis with AI
- Creates PDF reports
- Emails all subscribers worldwide
- Updates dashboard data
- Deploys fresh dashboard

### 3. **Deploy Pages Workflow** (`deploy-pages.yml`)
- Deploys dashboard on code changes
- Builds Vue.js app
- Publishes to GitHub Pages

## 📝 **Required GitHub Secrets:**

Go to `gradan-hash/SIGNALAI` → Settings → Secrets and variables → Actions:

### **AI API Keys:**
```
GOOGLE_GENERATIVE_AI_API_KEY: Your Gemini API key
GOOGLE_API_KEY_1: Backup API key 1  
GOOGLE_API_KEY_2: Backup API key 2
```

### **Email Configuration:**
```
GMAIL_EMAIL: signail.ai.team@gmail.com
GMAIL_APP_PASSWORD: gkaqofeqdrksglmc
```

## 🔧 **Frontend Setup:**

### **Add GitHub Token to Frontend:**
Replace this line in `dashboard/src/SimpleApp.vue`:
```javascript
'Authorization': 'Bearer ghp_YOUR_GITHUB_TOKEN_HERE'
```

### **Create Personal Access Token:**
1. GitHub → Settings → Developer settings → Personal access tokens
2. Generate new token with scopes: `repo`, `workflow`
3. Copy token and add to frontend code

## 🌐 **Deploy to GitHub Pages:**

### **Enable Pages:**
1. Repository Settings → Pages
2. Source: GitHub Actions
3. The workflows handle deployment automatically

### **Repository Structure:**
```
SIGNALAI/
├── .github/workflows/     # All automation
├── dashboard/            # Vue.js frontend  
├── agents.py            # AI signal generation
├── .env                 # Local environment (not committed)
└── subscribers.json     # Email list (auto-managed)
```

## ✅ **Complete System Flow:**

### **Daily Operation:**
1. **8:30 AM UTC**: Pre-market signals generated and emailed
2. **1:00 PM UTC**: Market opening signals generated and emailed  
3. **AI generates**: Fresh market analysis + PDF reports twice daily
4. **Emails sent**: To all subscribers worldwide before key market sessions
5. **Dashboard updated**: With latest signals and data
6. **Site deployed**: Fresh content live on GitHub Pages

### **User Subscription:**
1. **User subscribes** → GitHub Action triggered
2. **Email added** → `subscribers.json` updated automatically  
3. **Next day** → User receives first PDF report

## 🎯 **Benefits:**
- ✅ **Fully Automated**: Zero manual work after setup
- ✅ **Scalable**: Handles unlimited subscribers  
- ✅ **Reliable**: GitHub Actions infrastructure
- ✅ **Cost-Effective**: Free GitHub Pages hosting
- ✅ **Professional**: Daily PDF reports via email
- ✅ **Real-time**: Fresh market data daily

## 🚀 **Go Live:**
1. Add secrets to repository
2. Update frontend with GitHub token  
3. Push code to `main` branch
4. Workflows activate automatically
5. Daily signals and emails begin!

**Your Signal AI system is ready for production traffic!** 🎉
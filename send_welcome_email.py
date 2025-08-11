#!/usr/bin/env python3
"""
Send welcome email with latest Signal AI report to new subscriber
"""

import os
import sys
import smtplib
import glob
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime

def main():
    # Get environment variables
    gmail_email = os.getenv('GMAIL_EMAIL')
    app_password = os.getenv('GMAIL_APP_PASSWORD')
    new_email = sys.argv[1] if len(sys.argv) > 1 else None
    
    if not gmail_email or not app_password:
        print('❌ Gmail credentials not configured')
        sys.exit(0)
    
    if not new_email:
        print('❌ No email address provided')
        sys.exit(1)
    
    # Find the most recent PDF report
    pdf_files = glob.glob('reports/SignalAI_Report_*.pdf')
    if not pdf_files:
        print('⚠️ No PDF reports found, skipping welcome email')
        sys.exit(0)
    
    # Get the most recent PDF
    latest_pdf = max(pdf_files, key=os.path.getctime)
    print(f'📄 Found latest report: {latest_pdf}')
    
    try:
        # Create email message
        msg = MIMEMultipart()
        msg['From'] = f'Signal AI Team <{gmail_email}>'
        msg['To'] = new_email
        msg['Subject'] = f'🎉 Welcome to Signal AI - Your First Report Inside!'
        
        # Email body
        body = f"""🎉 Welcome to Signal AI!

Thank you for subscribing to our daily market intelligence reports!

As a welcome gift, we have attached your first Signal AI report. This comprehensive analysis includes:

✅ Global Market Discovery - Top traded assets worldwide
✅ Smart Search Intelligence - Trending opportunities  
✅ Detailed Asset Analysis - Entry points, targets, and risks
✅ Market Prediction - AI-powered outlook
✅ Professional Trading Insights

🔔 You will receive fresh reports twice daily:
• Pre-Market Intelligence (8:30 AM UTC)
• Market Opening Intelligence (1:00 PM UTC)

Generated: {datetime.now().strftime("%A, %B %d, %Y at %I:%M %p UTC")}

Welcome to smarter trading!

Best regards,
Signal AI Team
{gmail_email}

---
This report is for informational purposes only and should not be considered as financial advice.
Always conduct your own research and consider consulting with a financial advisor.
"""
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Attach PDF
        with open(latest_pdf, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            
        encoders.encode_base64(part)
        part.add_header(
            'Content-Disposition',
            f'attachment; filename={os.path.basename(latest_pdf)}'
        )
        msg.attach(part)
        
        # Send via SMTP
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(gmail_email, app_password)
        
        text = msg.as_string()
        server.sendmail(gmail_email, new_email, text)
        server.quit()
        
        print(f'✅ Welcome email with PDF sent to {new_email}')
        
    except Exception as e:
        print(f'❌ Failed to send welcome email: {e}')

if __name__ == '__main__':
    main()
#!/usr/bin/env python3
"""
Signal AI PDF Report Generator
Creates premium-looking market analysis PDFs for email delivery
Designed to build confidence and drive subscriptions
"""

import os
import json
from datetime import datetime
from typing import Dict, Any, List
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, black, white
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.graphics.shapes import Drawing, Rect
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.charts.barcharts import VerticalBarChart
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.mime.text import MIMEText

class SignalAIPDFReportGenerator:
    """
    Premium PDF Report Generator for Signal AI
    Creates professional market analysis reports that users want to pay for
    """
    
    def __init__(self):
        self.colors = {
            'primary': HexColor('#3B82F6'),    # Blue
            'success': HexColor('#10B981'),    # Green  
            'danger': HexColor('#EF4444'),     # Red
            'warning': HexColor('#F59E0B'),    # Yellow
            'dark': HexColor('#1F2937'),       # Dark gray
            'light': HexColor('#F3F4F6'),      # Light gray
            'accent': HexColor('#8B5CF6')      # Purple
        }
        
        # Custom styles for premium look
        self.styles = getSampleStyleSheet()
        self.setup_custom_styles()
    
    def setup_custom_styles(self):
        """Setup custom paragraph styles for premium look"""
        
        # Title style
        self.styles.add(ParagraphStyle(
            name='CustomTitle',
            parent=self.styles['Heading1'],
            fontSize=24,
            spaceAfter=30,
            alignment=TA_CENTER,
            textColor=self.colors['primary'],
            fontName='Helvetica-Bold'
        ))
        
        # Subtitle style
        self.styles.add(ParagraphStyle(
            name='CustomSubtitle',
            parent=self.styles['Heading2'],
            fontSize=16,
            spaceAfter=20,
            alignment=TA_CENTER,
            textColor=self.colors['dark'],
            fontName='Helvetica'
        ))
        
        # Executive summary style
        self.styles.add(ParagraphStyle(
            name='ExecutiveSummary',
            parent=self.styles['Normal'],
            fontSize=12,
            spaceAfter=15,
            leftIndent=20,
            rightIndent=20,
            textColor=self.colors['dark'],
            fontName='Helvetica',
            backColor=self.colors['light'],
            borderPadding=10
        ))
        
        # Action item style
        self.styles.add(ParagraphStyle(
            name='ActionItem',
            parent=self.styles['Normal'],
            fontSize=14,
            spaceAfter=10,
            leftIndent=15,
            textColor=self.colors['success'],
            fontName='Helvetica-Bold'
        ))
        
        # Risk warning style
        self.styles.add(ParagraphStyle(
            name='RiskWarning',
            parent=self.styles['Normal'],
            fontSize=10,
            spaceAfter=10,
            leftIndent=20,
            rightIndent=20,
            textColor=self.colors['danger'],
            fontName='Helvetica-Oblique'
        ))
    
    def generate_premium_report(self, market_data: Dict[str, Any], output_path: str) -> str:
        """
        Generate a premium PDF report that users want to pay for
        Focus: Clear actions, simple metrics, professional design
        """
        
        doc = SimpleDocTemplate(
            output_path,
            pagesize=A4,
            rightMargin=72,
            leftMargin=72,
            topMargin=72,
            bottomMargin=18
        )
        
        # Build report content
        story = []
        
        # Header
        story.extend(self._build_header(market_data))
        
        # Top Opportunities (What users pay for) - GO STRAIGHT TO THE MONEY
        story.extend(self._build_top_opportunities(market_data))
        
        # Asset Analysis
        story.extend(self._build_asset_analysis(market_data))
        
        # Risk Warnings (Builds trust)
        story.extend(self._build_risk_warnings())
        
        # Footer
        story.extend(self._build_footer())
        
        # Generate PDF
        doc.build(story)
        print(f"✅ Premium PDF report generated: {output_path}")
        return output_path
    
    def _build_header(self, data: Dict[str, Any]) -> List:
        """Build professional header"""
        elements = []
        
        # Title
        title = Paragraph("📊 Signal AI Market Intelligence Report", self.styles['CustomTitle'])
        elements.append(title)
        
        # Subtitle with date
        date_str = datetime.now().strftime('%B %d, %Y')
        subtitle = Paragraph(f"Premium Market Analysis • {date_str}", self.styles['CustomSubtitle'])
        elements.append(subtitle)
        
        elements.append(Spacer(1, 20))
        
        # Market overview box
        market_direction = data.get('summary', {}).get('market_direction', 'Mixed')
        confidence = data.get('market_prediction', {}).get('confidence', 70)
        
        overview_text = f"""
        <b>Market Direction:</b> {market_direction} <br/>
        <b>AI Confidence:</b> {confidence}% <br/>
        <b>Assets Analyzed:</b> {data.get('summary', {}).get('total_assets', 0)}
        """
        
        overview = Paragraph(overview_text, self.styles['ExecutiveSummary'])
        elements.append(overview)
        elements.append(Spacer(1, 30))
        
        return elements
    
    def _build_executive_summary(self, data: Dict[str, Any]) -> List:
        """Build executive summary - THE HOOK that makes users pay"""
        elements = []
        
        # Section title
        title = Paragraph("🎯 Executive Summary", self.styles['Heading2'])
        elements.append(title)
        
        # Key insights (2-3 bullet points MAX)
        market_prediction = data.get('market_prediction', {})
        top_story = data.get('summary', {}).get('top_story', 'Market monitoring ongoing')
        key_catalyst = market_prediction.get('key_catalyst', 'Economic indicators')
        
        summary_points = [
            f"• <b>Market Outlook:</b> {market_prediction.get('direction', 'Mixed')} trend expected over {market_prediction.get('timeframe', '1-3 days')}",
            f"• <b>Key Driver:</b> {key_catalyst}",
            f"• <b>Top Opportunity:</b> {top_story}"
        ]
        
        for point in summary_points:
            elements.append(Paragraph(point, self.styles['Normal']))
            elements.append(Spacer(1, 8))
        
        elements.append(Spacer(1, 20))
        return elements
    
    def _build_market_overview(self, data: Dict[str, Any]) -> List:
        """Build market overview with key metrics"""
        elements = []
        
        title = Paragraph("📈 Market Overview", self.styles['Heading2'])
        elements.append(title)
        
        # Create a simple metrics table
        global_leaders = data.get('summary', {}).get('global_volume_leaders', [])[:5]
        
        table_data = [
            ['Metric', 'Value', 'Signal'],
            ['Market Direction', data.get('summary', {}).get('market_direction', 'Mixed'), '🎯'],
            ['AI Confidence', f"{data.get('market_prediction', {}).get('confidence', 70)}%", '🤖'],
            ['Opportunity Score', f"{data.get('market_prediction', {}).get('opportunity_score', 75)}/100", '⭐'],
            ['Top Volume Leaders', ', '.join(global_leaders[:3]) if global_leaders else 'Analyzing...', '🚀']
        ]
        
        table = Table(table_data, colWidths=[2*inch, 2.5*inch, 0.5*inch])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), self.colors['primary']),
            ('TEXTCOLOR', (0, 0), (-1, 0), white),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), self.colors['light']),
            ('GRID', (0, 0), (-1, -1), 1, self.colors['dark'])
        ]))
        
        elements.append(table)
        elements.append(Spacer(1, 20))
        
        # Add comprehensive market analysis
        market_analysis = f"""
        <b>Current Market Environment:</b><br/>
        The market is currently showing a <b>{data.get('summary', {}).get('market_direction', 'mixed').lower()}</b> bias with 
        {data.get('market_prediction', {}).get('confidence', 70)}% AI confidence based on technical and fundamental analysis. 
        Our proprietary algorithms have identified {data.get('summary', {}).get('total_assets', 0)} actionable opportunities 
        across multiple asset classes.<br/><br/>
        
        <b>Key Market Drivers:</b><br/>
        {str(data.get('market_prediction', {}).get('key_catalyst', 'Multiple factors contributing to current market dynamics including economic indicators, corporate earnings, and technical patterns.'))}<br/><br/>
        
        <b>Global Volume Analysis:</b><br/>
        Current global volume leaders include: {', '.join(global_leaders) if global_leaders else 'Analyzing current volume patterns across global markets'}. 
        These assets are showing significant trading interest and may present both opportunities and risks for active traders.<br/><br/>
        
        <b>Risk Assessment:</b><br/>
        Market volatility remains within normal ranges. Current risk factors include: {', '.join(data.get('market_prediction', {}).get('risk_factors', ['Market uncertainty', 'Economic data releases']))}. 
        Traders should maintain appropriate position sizing and risk management protocols.<br/><br/>
        
        <b>Market Outlook:</b><br/>
        {str(data.get('market_prediction', {}).get('reasoning', 'Based on comprehensive analysis of current market conditions, technical indicators, and fundamental factors, we expect continued selective opportunities across asset classes. Maintain disciplined approach to position management.'))}
        """
        
        elements.append(Paragraph(market_analysis, self.styles['Normal']))
        elements.append(Spacer(1, 30))
        
        return elements
    
    def _build_top_opportunities(self, data: Dict[str, Any]) -> List:
        """Build top opportunities section - WHAT USERS PAY FOR"""
        elements = []
        
        title = Paragraph("🚀 Top Opportunities", self.styles['Heading2'])
        elements.append(title)
        
        # Get top 3 assets across all categories
        opportunities = []
        
        for category, category_data in data.get('detailed_analyses', {}).items():
            if category_data.get('analyses'):
                for asset in category_data['analyses'][:2]:  # Top 2 from each category
                    action = asset.get('action', 'watch').upper()
                    if action in ['BUY', 'SELL']:  # Only actionable opportunities
                        opportunities.append({
                            'symbol': asset.get('symbol', 'N/A'),
                            'action': action,
                            'move': asset.get('current_move', '+0.0%'),
                            'why': asset.get('trade_setup', asset.get('why_simple', 'Market analysis')),
                            'confidence': asset.get('confidence', 'medium'),
                            'risk': asset.get('risk', 'medium'),
                            'entry': asset.get('entry_price', 'At market'),
                            'stop': asset.get('stop_loss', 'Set -5%'),
                            'target': asset.get('profit_target', asset.get('next_target', 'TBD')),
                            'time_sensitive': asset.get('time_sensitive', False)
                        })
        
        # Show top 3 opportunities with full detailed analysis
        for i, opp in enumerate(opportunities[:3], 1):
            color = self.colors['success'] if opp['action'] == 'BUY' else self.colors['danger']
            
            # Time sensitivity alert
            time_alert = " ⏰ <b>TIME SENSITIVE - ACT WITHIN 24 HOURS</b>" if opp['time_sensitive'] else ""
            
            # Create comprehensive opportunity breakdown
            opportunity_header = f"""
            <b>OPPORTUNITY #{i}: {opp['symbol']} - {opp['action']} SIGNAL</b>{time_alert}
            """
            elements.append(Paragraph(opportunity_header, self.styles['Heading3']))
            
            # Market Performance Section
            performance_text = f"""
            <b>📊 MARKET PERFORMANCE ANALYSIS:</b><br/>
            Current Price Movement: {opp['move']}<br/>
            AI Confidence Level: {opp['confidence'].title()} confidence based on technical and fundamental analysis<br/>
            Risk Assessment: {opp['risk'].title()} risk - suitable for {self._get_risk_profile(opp['risk'])} investors<br/>
            """
            elements.append(Paragraph(performance_text, self.styles['Normal']))
            elements.append(Spacer(1, 10))
            
            # Extract specific numerical prices
            entry_price = self._extract_price(str(opp['entry']))
            stop_price = self._extract_price(str(opp['stop']))
            target_price = self._extract_price(str(opp['target']))
            
            # Calculate risk/reward if we have numbers
            risk_reward = self._calculate_risk_reward(entry_price, stop_price, target_price)
            
            # Complete Trading Setup Section with EXACT PRICES
            trading_setup_text = f"""
            <b>💰 EXACT TRADING SETUP - COPY THESE NUMBERS:</b><br/><br/>
            
            <b>🔥 ENTRY PRICE: {entry_price}</b><br/>
            Copy this exact price into your trading platform<br/><br/>
            
            <b>🛑 STOP LOSS: {stop_price}</b><br/>
            Set this as your stop loss order immediately after entry<br/><br/>
            
            <b>🎯 TAKE PROFIT: {target_price}</b><br/>
            Set this as your take profit target<br/><br/>
            
            <b>📊 RISK/REWARD RATIO: {risk_reward}</b><br/>
            {self._get_risk_reward_explanation(risk_reward)}<br/><br/>
            
            <b>💡 TRADE EXECUTION STEPS:</b><br/>
            1. Enter {opp['action']} order at {entry_price}<br/>
            2. Immediately set stop loss at {stop_price}<br/>
            3. Set take profit order at {target_price}<br/>
            4. Position size: Risk only 1-2% of your account on this trade<br/>
            """
            elements.append(Paragraph(trading_setup_text, self.styles['Normal']))
            elements.append(Spacer(1, 10))
            
            # Comprehensive Analysis Section
            analysis_text = f"""
            <b>💡 COMPREHENSIVE MARKET ANALYSIS:</b><br/>
            {str(opp['why'])}<br/><br/>
            <b>Market Context:</b> This opportunity emerges from our AI-powered analysis of current market conditions, 
            technical indicators, and fundamental factors. The signal strength indicates {opp['confidence']} probability 
            of successful execution within the specified timeframe.<br/><br/>
            <b>Execution Recommendation:</b> {self._get_execution_advice(opp['action'], opp['risk'])}
            """
            elements.append(Paragraph(analysis_text, self.styles['Normal']))
            elements.append(Spacer(1, 20))
            
            # Add separator line between opportunities
            if i < len(opportunities[:3]):
                separator = "━" * 80
                elements.append(Paragraph(separator, self.styles['Normal']))
                elements.append(Spacer(1, 15))
        
        if not opportunities:
            elements.append(Paragraph("• No strong actionable opportunities identified at this time. Market in consolidation phase.", self.styles['Normal']))
        
        elements.append(Spacer(1, 20))
        return elements
    
    def _get_risk_profile(self, risk_level: str) -> str:
        """Get investor profile description based on risk level"""
        risk_profiles = {
            'low': 'conservative and risk-averse',
            'medium': 'moderate risk tolerance',
            'high': 'aggressive and high-risk tolerance'
        }
        return risk_profiles.get(risk_level.lower(), 'all types of')
    
    def _get_execution_advice(self, action: str, risk: str) -> str:
        """Get specific execution advice based on action and risk"""
        if action.upper() == 'BUY':
            if risk.lower() == 'low':
                return "Consider dollar-cost averaging into this position over 2-3 sessions to minimize entry risk. Suitable for long-term portfolios."
            elif risk.lower() == 'high':
                return "This is a tactical opportunity requiring quick execution. Limit position size to 2-3% of portfolio. Consider partial profit-taking at interim targets."
            else:
                return "Standard position sizing recommended. Consider entering at current levels with disciplined stop-loss management."
        else:  # SELL
            if risk.lower() == 'high':
                return "Consider partial position closure or hedging strategies. This is a defensive move to protect capital."
            else:
                return "Systematic exit strategy recommended. Consider reducing exposure while maintaining some position for potential recovery."
    
    def _get_position_advice(self, risk_level: str) -> str:
        """Get position management advice based on risk level"""
        if risk_level.lower() == 'low':
            return "Suitable for larger position sizes (5-10% of portfolio). Conservative investors can consider this for core holdings."
        elif risk_level.lower() == 'high':
            return "Limit position size to 1-3% of portfolio. This is a tactical trade requiring active monitoring and quick decision making."
        else:
            return "Standard position sizing (3-5% of portfolio). Suitable for most investment strategies with proper risk management."
    
    def _extract_price(self, price_text: str) -> str:
        """Extract numerical price from text, return formatted price"""
        import re
        
        # Look for price patterns like $123.45, €1.2345, 123.45, etc.
        price_patterns = [
            r'\$(\d+\.?\d*)',  # $123.45
            r'€(\d+\.?\d*)',   # €1.23
            r'(\d+\.\d+)',     # 123.45
            r'(\d+)',          # 123
        ]
        
        for pattern in price_patterns:
            match = re.search(pattern, price_text)
            if match:
                price_num = float(match.group(1))
                # Format based on asset type context
                if '$' in price_text or price_num > 10:
                    return f"${price_num:.2f}"
                else:
                    return f"${price_num:.4f}"  # For forex/crypto
        
        # Fallback to original text if no price found
        return price_text
    
    def _calculate_risk_reward(self, entry: str, stop: str, target: str) -> str:
        """Calculate risk/reward ratio from price strings"""
        try:
            import re
            
            # Extract numbers
            entry_num = float(re.search(r'(\d+\.?\d*)', entry).group(1))
            stop_num = float(re.search(r'(\d+\.?\d*)', stop).group(1))
            target_num = float(re.search(r'(\d+\.?\d*)', target).group(1))
            
            risk = abs(entry_num - stop_num)
            reward = abs(target_num - entry_num)
            
            if risk > 0:
                ratio = reward / risk
                return f"1:{ratio:.1f}"
            else:
                return "1:2.0"
                
        except:
            return "1:2.0"  # Default fallback
    
    def _get_risk_reward_explanation(self, ratio: str) -> str:
        """Get explanation of risk/reward ratio quality"""
        try:
            ratio_num = float(ratio.split(':')[1])
            if ratio_num >= 3.0:
                return "Excellent risk/reward ratio - very attractive trade setup"
            elif ratio_num >= 2.0:
                return "Good risk/reward ratio - solid trade opportunity"
            elif ratio_num >= 1.5:
                return "Acceptable risk/reward ratio - proceed with caution"
            else:
                return "Lower risk/reward ratio - consider smaller position size"
        except:
            return "Standard risk/reward parameters apply"
    
    def _build_asset_analysis(self, data: Dict[str, Any]) -> List:
        """Build detailed asset analysis section"""
        elements = []
        
        title = Paragraph("📊 Asset Analysis", self.styles['Heading2'])
        elements.append(title)
        
        # Analyze each category
        for category_name, category_data in data.get('detailed_analyses', {}).items():
            if not category_data.get('analyses'):
                continue
                
            # Category header with comprehensive analysis
            cat_title = Paragraph(f"📈 {category_name.title()} Analysis", self.styles['Heading3'])
            elements.append(cat_title)
            elements.append(Spacer(1, 10))
            
            # Detailed analysis for each asset in this category
            for j, asset in enumerate(category_data['analyses'][:6], 1):  # Top 6 per category for thorough coverage
                
                # Asset header
                asset_header = f"<b>{j}. {asset.get('symbol', 'N/A')} - {asset.get('action', 'WATCH').upper()} RECOMMENDATION</b>"
                elements.append(Paragraph(asset_header, self.styles['Heading4']))
                
                # Current market status
                market_status = f"""
                <b>Current Market Status:</b><br/>
                Price Movement: {asset.get('current_move', 'Analyzing...')}<br/>
                Market Sentiment: {asset.get('confidence', 'Medium').title()} confidence level<br/>
                Risk Assessment: {asset.get('risk', 'Medium').title()} risk profile<br/>
                """
                elements.append(Paragraph(market_status, self.styles['Normal']))
                
                # Extract exact prices for this asset
                asset_entry = self._extract_price(str(asset.get('entry_price', asset.get('current_move', 'At market'))))
                asset_stop = self._extract_price(str(asset.get('stop_loss', 'Set -5%')))
                asset_target = self._extract_price(str(asset.get('profit_target', asset.get('next_target', 'TBD'))))
                asset_ratio = self._calculate_risk_reward(asset_entry, asset_stop, asset_target)
                
                # Complete trading strategy with EXACT NUMBERS
                trading_strategy = f"""
                <b>🔥 EXACT TRADING NUMBERS - COPY & PASTE:</b><br/>
                <b>📍 ENTRY: {asset_entry}</b> - Enter {asset.get('action', 'position').upper()} at this exact price<br/>
                <b>🛑 STOP: {asset_stop}</b> - Set stop loss at this price to protect capital<br/>
                <b>🎯 TARGET: {asset_target}</b> - Take profit at this price level<br/>
                <b>⚡ RATIO: {asset_ratio}</b> - {self._get_risk_reward_explanation(asset_ratio)}<br/>
                <b>💼 POSITION: {self._get_position_advice(asset.get('risk', 'medium'))}</b><br/>
                """
                elements.append(Paragraph(trading_strategy, self.styles['Normal']))
                
                # Fundamental analysis
                fundamental_analysis = f"""
                <b>Market Analysis & Rationale:</b><br/>
                <b>Why This Asset:</b> {str(asset.get('why_simple', 'Based on technical and fundamental factors'))}<br/>
                <b>Detailed Explanation:</b> {str(asset.get('explanation', 'Comprehensive market analysis indicates favorable conditions for this position'))}<br/>
                <b>Market Impact:</b> {str(asset.get('what_it_means', 'This represents an opportunity based on current market dynamics'))}<br/>
                """
                elements.append(Paragraph(fundamental_analysis, self.styles['Normal']))
                
                # Trade setup and catalyst
                if asset.get('trade_setup') or asset.get('catalyst'):
                    trade_details = f"""
                    <b>Trade Setup Details:</b><br/>
                    <b>Setup Explanation:</b> {str(asset.get('trade_setup', 'Standard technical setup based on market conditions'))}<br/>
                    <b>Key Catalyst:</b> {str(asset.get('catalyst', 'Market dynamics and technical indicators'))}<br/>
                    <b>Time Sensitivity:</b> {'High - Consider executing within 24-48 hours' if asset.get('time_sensitive') else 'Normal - Execute when convenient within trading strategy'}<br/>
                    """
                    elements.append(Paragraph(trade_details, self.styles['Normal']))
                
                # Market prediction and outlook
                market_outlook = f"""
                <b>Market Outlook & Prediction:</b><br/>
                {str(asset.get('market_prediction', 'Based on current analysis, we expect this asset to follow the recommended direction within the specified timeframe. Monitor market conditions for any changes that might affect the trade setup.'))}<br/>
                """
                elements.append(Paragraph(market_outlook, self.styles['Normal']))
                
                # Separator between assets
                if j < len(category_data['analyses'][:6]):
                    separator = "─" * 60
                    elements.append(Paragraph(separator, self.styles['Normal']))
                
                elements.append(Spacer(1, 15))
            
            # Category summary
            category_summary = f"""
            <b>Category Summary:</b> Analyzed {len(category_data['analyses'])} {category_name} assets. 
            Focus on assets with BUY/SELL signals for active opportunities. WATCH signals indicate 
            assets to monitor for future entry points. All analysis based on current market conditions 
            and may change based on market developments.<br/>
            """
            elements.append(Paragraph(category_summary, self.styles['Normal']))
            elements.append(Spacer(1, 25))
        
        return elements
    
    def _build_risk_warnings(self) -> List:
        """Build risk warnings - BUILDS TRUST"""
        elements = []
        
        title = Paragraph("⚠️ Important Risk Disclosures", self.styles['Heading3'])
        elements.append(title)
        
        risk_text = """
        <b>Investment Risks:</b> All investments involve risk of loss. Past performance does not guarantee future results. 
        This report is for informational purposes only and should not be considered personalized investment advice. 
        Please consult with a qualified financial advisor before making investment decisions.
        <br/><br/>
        <b>AI Limitations:</b> This analysis is generated by artificial intelligence and may contain errors or 
        incomplete information. Market conditions can change rapidly, and predictions may not materialize.
        <br/><br/>
        <b>No Guarantees:</b> Signal AI makes no warranties about the accuracy or completeness of this information. 
        Trading and investing carry substantial risk of loss.
        """
        
        elements.append(Paragraph(risk_text, self.styles['RiskWarning']))
        elements.append(Spacer(1, 20))
        
        return elements
    
    def _build_footer(self) -> List:
        """Build professional footer"""
        elements = []
        
        footer_text = f"""
        <br/><br/>
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━<br/>
        <b>Signal AI</b> | Premium Market Intelligence | Generated {datetime.now().strftime('%B %d, %Y at %H:%M UTC')}<br/>
        © 2024 Signal AI. All rights reserved. | Visit our dashboard for real-time updates
        """
        
        elements.append(Paragraph(footer_text, self.styles['Normal']))
        return elements

class EmailDeliverySystem:
    """
    Email delivery system for PDF reports
    Professional email marketing for Signal AI
    """
    
    def __init__(self, smtp_server: str, smtp_port: int, email: str, password: str):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.email = email
        self.password = password
    
    def send_premium_report(self, recipient_email: str, pdf_path: str, market_data: Dict[str, Any]) -> bool:
        """
        Send premium PDF report via email
        Professional presentation to build subscriber value
        """
        
        try:
            # Create message
            msg = MIMEMultipart()
            msg['From'] = self.email
            msg['To'] = recipient_email
            msg['Subject'] = f"📊 Signal AI Market Report - {datetime.now().strftime('%B %d, %Y')}"
            
            # Email body
            market_direction = market_data.get('summary', {}).get('market_direction', 'Mixed')
            confidence = market_data.get('market_prediction', {}).get('confidence', 70)
            
            body = f"""
            <html>
            <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
                <div style="max-width: 600px; margin: 0 auto; padding: 20px;">
                    <h2 style="color: #3B82F6; text-align: center;">📊 Your Signal AI Market Report</h2>
                    
                    <div style="background: #F3F4F6; padding: 20px; border-radius: 8px; margin: 20px 0;">
                        <h3 style="color: #1F2937; margin-top: 0;">Today's Market Intelligence:</h3>
                        <ul style="list-style: none; padding: 0;">
                            <li style="margin: 10px 0;"><strong>📈 Direction:</strong> {market_direction}</li>
                            <li style="margin: 10px 0;"><strong>🤖 AI Confidence:</strong> {confidence}%</li>
                            <li style="margin: 10px 0;"><strong>📊 Assets Analyzed:</strong> {market_data.get('summary', {}).get('total_assets', 0)}</li>
                        </ul>
                    </div>
                    
                    <p><strong>Your detailed PDF report is attached</strong> with specific buy/sell recommendations and market insights.</p>
                    
                    <div style="background: #EF4444; color: white; padding: 15px; border-radius: 8px; margin: 20px 0;">
                        <p style="margin: 0;"><strong>⚠️ Risk Warning:</strong> All investments carry risk. This is for informational purposes only.</p>
                    </div>
                    
                    <p style="text-align: center; margin-top: 30px;">
                        <a href="http://localhost:3001" style="background: #3B82F6; color: white; padding: 12px 24px; text-decoration: none; border-radius: 6px;">
                            View Live Dashboard
                        </a>
                    </p>
                    
                    <hr style="margin: 30px 0; border: none; border-top: 1px solid #E5E7EB;">
                    <p style="font-size: 12px; color: #6B7280; text-align: center;">
                        Signal AI | Premium Market Intelligence<br/>
                        © 2024 Signal AI. All rights reserved.
                    </p>
                </div>
            </body>
            </html>
            """
            
            msg.attach(MIMEText(body, 'html'))
            
            # Attach PDF
            with open(pdf_path, "rb") as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header(
                    'Content-Disposition',
                    f'attachment; filename= "SignalAI_Report_{datetime.now().strftime("%Y%m%d")}.pdf"'
                )
                msg.attach(part)
            
            # Send email
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.email, self.password)
            text = msg.as_string()
            server.sendmail(self.email, recipient_email, text)
            server.quit()
            
            print(f"✅ Premium report emailed to: {recipient_email}")
            return True
            
        except Exception as e:
            print(f"❌ Email delivery failed: {e}")
            return False

# Usage example
def generate_and_send_report():
    """
    Example usage of the PDF report system
    """
    
    # Load market data
    try:
        with open('dashboard/public/data/market_insights.json', 'r') as f:
            market_data = json.load(f)
    except FileNotFoundError:
        print("❌ No market data found. Run agents.py first.")
        return
    
    # Generate PDF report
    report_generator = SignalAIPDFReportGenerator()
    pdf_path = f"reports/SignalAI_Report_{datetime.now().strftime('%Y%m%d_%H%M')}.pdf"
    
    # Create reports directory
    os.makedirs('reports', exist_ok=True)
    
    # Generate report
    report_generator.generate_premium_report(market_data, pdf_path)
    
    # Email setup (you'll need to configure these)
    """
    email_system = EmailDeliverySystem(
        smtp_server="smtp.gmail.com",
        smtp_port=587,
        email="your_signal_ai@gmail.com",
        password="your_app_password"
    )
    
    # Send to test email
    email_system.send_premium_report("test@example.com", pdf_path, market_data)
    """
    
    print(f"✅ Report ready: {pdf_path}")

if __name__ == "__main__":
    generate_and_send_report()
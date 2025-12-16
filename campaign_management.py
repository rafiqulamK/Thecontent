"""
Real-World Campaign Analysis & Reporting
Similar to Madgicx's real-time dashboard and campaign management features
"""
import json
from datetime import datetime, timedelta
from typing import Dict, List

class CampaignDashboard:
    """Real-time campaign monitoring and reporting (Madgicx core)"""
    
    def __init__(self):
        self.active_campaigns = {}
        self.campaign_history = []
        self.alerts = []
        
    def create_campaign_report(self, campaign_data: Dict) -> Dict:
        """Generate comprehensive campaign report"""
        return {
            'report_timestamp': datetime.now().isoformat(),
            'campaign_summary': self._generate_summary(campaign_data),
            'performance_overview': self._generate_performance(campaign_data),
            'detailed_metrics': self._generate_detailed_metrics(campaign_data),
            'visualizations': self._prepare_visualizations(campaign_data),
            'alerts': self._check_for_alerts(campaign_data),
            'daily_breakdown': self._get_daily_breakdown(campaign_data),
            'hourly_breakdown': self._get_hourly_breakdown(campaign_data),
            'roi_analysis': self._analyze_roi(campaign_data),
            'recommendations': self._generate_recommendations(campaign_data),
            'export_options': ['PDF', 'CSV', 'JSON']
        }
    
    def _generate_summary(self, data: Dict) -> Dict:
        """Generate campaign summary"""
        return {
            'campaign_id': data.get('campaign_id'),
            'campaign_name': data.get('name'),
            'status': data.get('status', 'Active'),
            'duration': data.get('duration_days', 30),
            'objective': data.get('objective', 'Conversions'),
            'total_budget': data.get('budget', 0),
            'spent': data.get('spend', 0),
            'budget_remaining': data.get('budget', 0) - data.get('spend', 0),
            'spend_percentage': (data.get('spend', 0) / max(data.get('budget', 1), 1)) * 100,
            'ads_count': data.get('ad_count', 1),
            'audiences': data.get('audience_count', 1),
            'created_date': data.get('created_date'),
            'end_date': data.get('end_date')
        }
    
    def _generate_performance(self, data: Dict) -> Dict:
        """Generate performance overview"""
        impressions = data.get('impressions', 0)
        clicks = data.get('clicks', 0)
        conversions = data.get('conversions', 0)
        spend = data.get('spend', 0)
        revenue = data.get('revenue', 0)
        
        return {
            'impressions': impressions,
            'clicks': clicks,
            'conversions': conversions,
            'spend': spend,
            'revenue': revenue,
            'ctr': (clicks / impressions * 100) if impressions > 0 else 0,
            'cpc': (spend / clicks) if clicks > 0 else 0,
            'cpa': (spend / conversions) if conversions > 0 else 0,
            'roas': (revenue / spend) if spend > 0 else 0,
            'cost_per_impression': (spend / impressions * 1000) if impressions > 0 else 0,
            'conversion_rate': (conversions / clicks * 100) if clicks > 0 else 0,
            'profit': revenue - spend,
            'profit_margin': ((revenue - spend) / revenue * 100) if revenue > 0 else 0
        }
    
    def _generate_detailed_metrics(self, data: Dict) -> Dict:
        """Generate detailed metrics breakdown"""
        return {
            'reach': data.get('reach', 0),
            'frequency': data.get('frequency', 1.0),
            'relevance_score': data.get('relevance_score', 0),
            'quality_score': data.get('quality_score', 0),
            'engagement': data.get('engagement', 0),
            'engagement_rate': data.get('engagement_rate', 0),
            'adds_to_cart': data.get('adds_to_cart', 0),
            'purchases': data.get('purchases', 0),
            'leads': data.get('leads', 0),
            'video_views': data.get('video_views', 0),
            'video_view_rate': data.get('video_view_rate', 0),
            'landing_page_views': data.get('lp_views', 0),
            'initiated_checkout': data.get('initiated_checkout', 0),
            'checkout_rate': (data.get('initiated_checkout', 0) / data.get('clicks', 1) * 100) if data.get('clicks') else 0
        }
    
    def _prepare_visualizations(self, data: Dict) -> Dict:
        """Prepare data for visualizations"""
        return {
            'daily_spend_chart': self._get_daily_trend(data),
            'cpa_trend': self._get_cpa_trend(data),
            'roas_trend': self._get_roas_trend(data),
            'device_breakdown': self._get_device_breakdown(data),
            'placement_breakdown': self._get_placement_breakdown(data),
            'geographic_breakdown': self._get_geographic_breakdown(data),
            'time_of_day_breakdown': self._get_time_breakdown(data)
        }
    
    def _get_daily_trend(self, data: Dict) -> List[Dict]:
        """Generate daily spend trend"""
        days_running = data.get('days_running', 7)
        daily_budget = data.get('spend', 0) / max(days_running, 1)
        
        trend = []
        for day in range(days_running):
            trend.append({
                'day': (datetime.now() - timedelta(days=days_running-day)).strftime('%Y-%m-%d'),
                'spend': daily_budget * (0.8 + (day % 3) * 0.1),
                'conversions': int(daily_budget * 0.05 * (0.8 + (day % 3) * 0.1))
            })
        return trend
    
    def _get_cpa_trend(self, data: Dict) -> List[Dict]:
        """Generate CPA trend"""
        return [
            {'date': (datetime.now() - timedelta(days=i)).strftime('%Y-%m-%d'), 
             'cpa': 20 + (i * 0.5)}
            for i in range(7)
        ]
    
    def _get_roas_trend(self, data: Dict) -> List[Dict]:
        """Generate ROAS trend"""
        return [
            {'date': (datetime.now() - timedelta(days=i)).strftime('%Y-%m-%d'), 
             'roas': 2.5 + (i * 0.1)}
            for i in range(7)
        ]
    
    def _get_device_breakdown(self, data: Dict) -> Dict:
        """Get device breakdown"""
        return {
            'mobile': {
                'percentage': 60,
                'ctr': 2.1,
                'cpc': 0.45,
                'cpa': 18
            },
            'desktop': {
                'percentage': 35,
                'ctr': 1.2,
                'cpc': 0.65,
                'cpa': 25
            },
            'tablet': {
                'percentage': 5,
                'ctr': 1.0,
                'cpc': 0.70,
                'cpa': 28
            }
        }
    
    def _get_placement_breakdown(self, data: Dict) -> Dict:
        """Get placement breakdown"""
        return {
            'facebook_feed': {
                'percentage': 40,
                'ctr': 1.8,
                'cpa': 22
            },
            'instagram_feed': {
                'percentage': 35,
                'ctr': 2.2,
                'cpa': 20
            },
            'instagram_reels': {
                'percentage': 15,
                'ctr': 3.1,
                'cpa': 18
            },
            'audience_network': {
                'percentage': 10,
                'ctr': 0.8,
                'cpa': 35
            }
        }
    
    def _get_geographic_breakdown(self, data: Dict) -> Dict:
        """Get geographic breakdown"""
        return {
            'US': {
                'percentage': 70,
                'cpa': 22,
                'roas': 2.8
            },
            'Canada': {
                'percentage': 15,
                'cpa': 25,
                'roas': 2.5
            },
            'UK': {
                'percentage': 10,
                'cpa': 28,
                'roas': 2.2
            },
            'Other': {
                'percentage': 5,
                'cpa': 35,
                'roas': 1.8
            }
        }
    
    def _get_time_breakdown(self, data: Dict) -> Dict:
        """Get time of day breakdown"""
        return {
            'morning_6am_12pm': {
                'percentage': 25,
                'ctr': 1.5,
                'cpa': 25
            },
            'afternoon_12pm_6pm': {
                'percentage': 35,
                'ctr': 2.1,
                'cpa': 20
            },
            'evening_6pm_12am': {
                'percentage': 30,
                'ctr': 2.3,
                'cpa': 19
            },
            'night_12am_6am': {
                'percentage': 10,
                'ctr': 1.2,
                'cpa': 28
            }
        }
    
    def _check_for_alerts(self, data: Dict) -> List[Dict]:
        """Check for performance alerts"""
        alerts = []
        
        ctr = (data.get('clicks', 0) / data.get('impressions', 1) * 100) if data.get('impressions') else 0
        if ctr < 0.5:
            alerts.append({
                'severity': 'HIGH',
                'alert': 'Very low CTR detected',
                'recommendation': 'Review ad creative and copy'
            })
        
        cpa = (data.get('spend', 0) / data.get('conversions', 1)) if data.get('conversions') else 0
        target_cpa = data.get('target_cpa', 25)
        if cpa > target_cpa * 1.5:
            alerts.append({
                'severity': 'HIGH',
                'alert': f'CPA exceeds target by {((cpa/target_cpa - 1) * 100):.0f}%',
                'recommendation': 'Pause and audit campaign immediately'
            })
        
        frequency = data.get('frequency', 1)
        if frequency > 5:
            alerts.append({
                'severity': 'MEDIUM',
                'alert': 'High ad frequency detected',
                'recommendation': 'Increase audience size or reduce daily budget'
            })
        
        budget_spent = (data.get('spend', 0) / max(data.get('budget', 1), 1)) * 100
        if budget_spent > 90 and data.get('days_running', 1) < data.get('duration_days', 30) * 0.5:
            alerts.append({
                'severity': 'MEDIUM',
                'alert': 'Budget spent too quickly',
                'recommendation': 'Reduce daily budget or improve targeting efficiency'
            })
        
        return alerts
    
    def _get_daily_breakdown(self, data: Dict) -> List[Dict]:
        """Get daily performance breakdown"""
        days_running = data.get('days_running', 7)
        daily_spend = data.get('spend', 0) / max(days_running, 1)
        
        breakdown = []
        for day in range(days_running):
            date = (datetime.now() - timedelta(days=days_running-day))
            breakdown.append({
                'date': date.strftime('%Y-%m-%d'),
                'day_name': date.strftime('%A'),
                'spend': daily_spend,
                'impressions': int(daily_spend * 50),
                'clicks': int(daily_spend * 2),
                'conversions': int(daily_spend * 0.08),
                'ctr': 2.0 if (day % 2 == 0) else 1.8,
                'cpa': 22 if (day % 2 == 0) else 24
            })
        
        return breakdown
    
    def _get_hourly_breakdown(self, data: Dict) -> List[Dict]:
        """Get hourly performance breakdown"""
        breakdown = []
        for hour in range(24):
            multiplier = 1.2 if 12 <= hour <= 18 else 0.8  # Peak hours
            breakdown.append({
                'hour': f"{hour:02d}:00",
                'spend': (data.get('spend', 0) / 24) * multiplier,
                'impressions': int((data.get('impressions', 0) / 24) * multiplier),
                'conversions': int((data.get('conversions', 0) / 24) * multiplier),
                'cpa': 22 if 12 <= hour <= 18 else 25
            })
        
        return breakdown
    
    def _analyze_roi(self, data: Dict) -> Dict:
        """Analyze ROI and profitability"""
        revenue = data.get('revenue', 0)
        spend = data.get('spend', 0)
        profit = revenue - spend
        roas = (revenue / spend) if spend > 0 else 0
        roi = ((profit / spend) * 100) if spend > 0 else 0
        
        return {
            'total_revenue': revenue,
            'total_spend': spend,
            'profit': profit,
            'roas': roas,
            'roi': roi,
            'break_even_point': 'Reached' if roas > 1.0 else f"In {spend - revenue:.0f} days",
            'daily_profit': profit / max(data.get('days_running', 1), 1),
            'weekly_profit': (profit / max(data.get('days_running', 1), 1)) * 7,
            'monthly_profit': (profit / max(data.get('days_running', 1), 1)) * 30,
            'profitability_grade': self._grade_profitability(roas)
        }
    
    def _grade_profitability(self, roas: float) -> str:
        """Grade profitability"""
        if roas >= 4.0:
            return "A+ (Exceptional)"
        elif roas >= 3.0:
            return "A (Excellent)"
        elif roas >= 2.0:
            return "B (Good)"
        elif roas >= 1.5:
            return "C (Break-even approaching)"
        else:
            return "D (Unprofitable)"
    
    def _generate_recommendations(self, data: Dict) -> List[Dict]:
        """Generate actionable recommendations"""
        recommendations = []
        
        ctr = (data.get('clicks', 0) / max(data.get('impressions', 1), 1)) * 100
        if ctr > 2.5:
            recommendations.append({
                'priority': 'HIGH',
                'recommendation': 'Scale aggressively - excellent CTR',
                'action': 'Increase daily budget by 50%',
                'expected_impact': '50% more revenue'
            })
        
        cpa = (data.get('spend', 0) / max(data.get('conversions', 1), 1))
        if cpa < data.get('target_cpa', 25) * 0.8:
            recommendations.append({
                'priority': 'HIGH',
                'recommendation': 'CPA is below target - expand audience',
                'action': 'Add lookalike audiences at 1-3%',
                'expected_impact': 'Double reach with maintained efficiency'
            })
        
        frequency = data.get('frequency', 1)
        if frequency > 3:
            recommendations.append({
                'priority': 'MEDIUM',
                'recommendation': 'Reduce ad fatigue',
                'action': 'Refresh creative assets or expand audience',
                'expected_impact': '+15% CTR improvement'
            })
        
        return recommendations


class MultiCampaignManager:
    """Manage and optimize multiple campaigns simultaneously (Madgicx feature)"""
    
    def __init__(self):
        self.campaigns = {}
        self.portfolio_metrics = {}
        
    def analyze_portfolio(self, campaigns: List[Dict]) -> Dict:
        """Analyze entire campaign portfolio"""
        portfolio_analysis = {
            'total_campaigns': len(campaigns),
            'total_spend': sum(c.get('spend', 0) for c in campaigns),
            'total_revenue': sum(c.get('revenue', 0) for c in campaigns),
            'portfolio_roas': self._calculate_portfolio_roas(campaigns),
            'portfolio_roi': self._calculate_portfolio_roi(campaigns),
            'campaigns_by_status': self._categorize_by_status(campaigns),
            'high_performers': self._identify_top_performers(campaigns),
            'underperformers': self._identify_underperformers(campaigns),
            'budget_allocation_recommendations': self._recommend_budget_reallocation(campaigns),
            'overall_health': self._assess_portfolio_health(campaigns)
        }
        
        return portfolio_analysis
    
    def _calculate_portfolio_roas(self, campaigns: List[Dict]) -> float:
        """Calculate overall portfolio ROAS"""
        total_revenue = sum(c.get('revenue', 0) for c in campaigns)
        total_spend = sum(c.get('spend', 0) for c in campaigns)
        return (total_revenue / total_spend) if total_spend > 0 else 0
    
    def _calculate_portfolio_roi(self, campaigns: List[Dict]) -> float:
        """Calculate overall portfolio ROI"""
        total_revenue = sum(c.get('revenue', 0) for c in campaigns)
        total_spend = sum(c.get('spend', 0) for c in campaigns)
        profit = total_revenue - total_spend
        return ((profit / total_spend) * 100) if total_spend > 0 else 0
    
    def _categorize_by_status(self, campaigns: List[Dict]) -> Dict:
        """Categorize campaigns by status"""
        categories = {
            'active': [],
            'paused': [],
            'completed': [],
            'scaling': [],
            'optimizing': []
        }
        
        for campaign in campaigns:
            status = campaign.get('status', 'active').lower()
            if status in categories:
                categories[status].append(campaign.get('name'))
        
        return categories
    
    def _identify_top_performers(self, campaigns: List[Dict]) -> List[Dict]:
        """Identify top performing campaigns"""
        sorted_campaigns = sorted(
            campaigns,
            key=lambda x: x.get('roas', 0),
            reverse=True
        )
        
        return [
            {
                'name': c.get('name'),
                'roas': c.get('roas', 0),
                'spend': c.get('spend', 0),
                'revenue': c.get('revenue', 0)
            }
            for c in sorted_campaigns[:5]
        ]
    
    def _identify_underperformers(self, campaigns: List[Dict]) -> List[Dict]:
        """Identify underperforming campaigns"""
        underperformers = [
            c for c in campaigns
            if c.get('roas', 0) < 1.5
        ]
        
        return [
            {
                'name': c.get('name'),
                'roas': c.get('roas', 0),
                'issue': 'Low ROAS' if c.get('roas', 0) < 1 else 'Below target',
                'recommendation': 'Pause and audit' if c.get('roas', 0) < 1 else 'Optimize targeting'
            }
            for c in underperformers[:5]
        ]
    
    def _recommend_budget_reallocation(self, campaigns: List[Dict]) -> Dict:
        """Recommend budget reallocation"""
        total_spend = sum(c.get('spend', 0) for c in campaigns)
        top_performers = self._identify_top_performers(campaigns)
        
        return {
            'recommendation': 'Reallocate 20% of budget from underperformers to top 3',
            'expected_impact': '+15-25% portfolio ROAS',
            'top_performers_to_scale': [c['name'] for c in top_performers[:3]],
            'underperformers_to_pause': [
                c['name'] for c in self._identify_underperformers(campaigns)[:2]
            ]
        }
    
    def _assess_portfolio_health(self, campaigns: List[Dict]) -> str:
        """Assess overall portfolio health"""
        healthy_count = sum(1 for c in campaigns if c.get('roas', 0) > 2.0)
        healthy_percentage = (healthy_count / len(campaigns) * 100) if campaigns else 0
        
        if healthy_percentage >= 80:
            return "🟢 Excellent - Most campaigns profitable"
        elif healthy_percentage >= 60:
            return "🟡 Good - Majority performing well"
        elif healthy_percentage >= 40:
            return "🔴 Fair - Review underperformers"
        else:
            return "🔴 Poor - Major optimization needed"

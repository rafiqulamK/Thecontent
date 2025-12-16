"""
Real-time Analytics & Reporting System
Live dashboards, custom reports, predictive analytics
"""

from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from datetime import datetime, timedelta
from enum import Enum
import statistics

class ReportType(Enum):
    """Types of analytics reports"""
    PERFORMANCE = "performance"
    COMPETITIVE = "competitive"
    AUDIENCE = "audience"
    CONTENT = "content"
    BUDGET = "budget"
    FORECAST = "forecast"


@dataclass
class MetricPoint:
    """Single metric data point"""
    timestamp: datetime
    value: float
    dimension: str  # 'platform', 'campaign', 'audience', etc


class RealTimeMetrics:
    """Track real-time campaign metrics"""
    
    def __init__(self):
        self.metrics: Dict[str, List[MetricPoint]] = {}
        self.aggregations: Dict[str, float] = {}
    
    def record_metric(self, metric_name: str, value: float, dimension: str = 'global') -> None:
        """Record new metric point"""
        if metric_name not in self.metrics:
            self.metrics[metric_name] = []
        
        point = MetricPoint(
            timestamp=datetime.now(),
            value=value,
            dimension=dimension
        )
        self.metrics[metric_name].append(point)
        
        # Keep only last 1000 points to avoid memory overflow
        if len(self.metrics[metric_name]) > 1000:
            self.metrics[metric_name] = self.metrics[metric_name][-1000:]
    
    def get_metric_trend(self, metric_name: str, hours: int = 24) -> List[Dict]:
        """Get metric trend over time"""
        if metric_name not in self.metrics:
            return []
        
        cutoff = datetime.now() - timedelta(hours=hours)
        points = [
            {
                'timestamp': p.timestamp.isoformat(),
                'value': p.value,
                'dimension': p.dimension
            }
            for p in self.metrics[metric_name]
            if p.timestamp > cutoff
        ]
        return points
    
    def get_metric_stats(self, metric_name: str) -> Dict:
        """Get statistics for metric"""
        if metric_name not in self.metrics:
            return {}
        
        values = [p.value for p in self.metrics[metric_name]]
        if not values:
            return {}
        
        return {
            'count': len(values),
            'current': values[-1],
            'min': min(values),
            'max': max(values),
            'avg': statistics.mean(values),
            'median': statistics.median(values),
            'std_dev': statistics.stdev(values) if len(values) > 1 else 0
        }


class PerformanceReport:
    """Generate performance reports"""
    
    def __init__(self):
        self.metrics = RealTimeMetrics()
    
    def generate_performance_report(self, campaign_id: str, days: int = 7) -> Dict:
        """Generate comprehensive performance report"""
        report = {
            'report_type': 'performance',
            'campaign_id': campaign_id,
            'period_days': days,
            'generated_at': datetime.now().isoformat(),
            'metrics': {},
            'benchmarks': {},
            'insights': []
        }
        
        # Simulate data collection
        metrics_to_track = [
            'impressions', 'clicks', 'conversions', 'spend', 'cpc', 'ctr', 'cpa', 'roas'
        ]
        
        for metric in metrics_to_track:
            trend = self.metrics.get_metric_trend(metric, hours=days*24)
            if trend:
                report['metrics'][metric] = self.metrics.get_metric_stats(metric)
        
        # Add benchmarks and insights
        report['benchmarks'] = self._get_benchmarks(campaign_id)
        report['insights'] = self._generate_insights(report['metrics'], report['benchmarks'])
        
        return report
    
    def generate_comparative_report(self, campaign_ids: List[str], metric: str = 'roas') -> Dict:
        """Compare performance across campaigns"""
        comparison = {
            'metric': metric,
            'campaigns': [],
            'best_performer': None,
            'worst_performer': None,
            'generated_at': datetime.now().isoformat()
        }
        
        performance_data = []
        for campaign_id in campaign_ids:
            stats = self.metrics.get_metric_stats(metric)
            if stats:
                perf_data = {
                    'campaign_id': campaign_id,
                    'value': stats.get('current', 0),
                    'avg': stats.get('avg', 0),
                    'trend': 'up' if stats.get('current', 0) > stats.get('avg', 0) else 'down'
                }
                performance_data.append(perf_data)
                comparison['campaigns'].append(perf_data)
        
        if performance_data:
            comparison['best_performer'] = max(performance_data, key=lambda x: x['value'])['campaign_id']
            comparison['worst_performer'] = min(performance_data, key=lambda x: x['value'])['campaign_id']
        
        return comparison
    
    def _get_benchmarks(self, campaign_id: str) -> Dict:
        """Get industry benchmarks"""
        return {
            'ctr': 2.5,  # Average click-through rate
            'cpc': 1.25,  # Average cost per click
            'cpa': 45.00,  # Average cost per acquisition
            'roas': 3.5,  # Average return on ad spend
            'conversion_rate': 3.2  # Average conversion rate
        }
    
    def _generate_insights(self, metrics: Dict, benchmarks: Dict) -> List[str]:
        """Generate actionable insights"""
        insights = []
        
        # Compare metrics to benchmarks
        for metric, value_dict in metrics.items():
            if 'current' in value_dict and metric in benchmarks:
                current = value_dict['current']
                benchmark = benchmarks.get(metric, 0)
                
                if metric in ['ctr', 'roas', 'conversion_rate']:
                    # Higher is better
                    if current < benchmark * 0.8:
                        insights.append(f"⚠️ {metric.upper()} is {(benchmark - current) / benchmark * 100:.0f}% below benchmark")
                    elif current > benchmark * 1.2:
                        insights.append(f"✅ {metric.upper()} is {(current - benchmark) / benchmark * 100:.0f}% above benchmark")
                else:
                    # Lower is better (CPC, CPA)
                    if current > benchmark * 1.2:
                        insights.append(f"⚠️ {metric.upper()} is {(current - benchmark) / benchmark * 100:.0f}% above benchmark")
                    elif current < benchmark * 0.8:
                        insights.append(f"✅ {metric.upper()} is {(benchmark - current) / benchmark * 100:.0f}% below benchmark")
        
        if not insights:
            insights.append("📊 Campaign performing at benchmark levels")
        
        return insights


class PredictiveAnalytics:
    """Forecast future performance"""
    
    def __init__(self):
        self.metrics = RealTimeMetrics()
    
    def forecast_conversions(self, campaign_id: str, days_ahead: int = 7) -> Dict:
        """Forecast future conversions"""
        # Get historical conversion data
        trend = self.metrics.get_metric_trend('conversions', hours=7*24)
        
        if not trend or len(trend) < 7:
            return {'forecast': 'Insufficient data', 'requires_days': 7}
        
        # Simple linear trend analysis
        values = [p['value'] for p in trend]
        current = values[-1]
        
        # Calculate daily growth rate
        if len(values) > 1:
            daily_change = (values[-1] - values[0]) / (len(values) - 1)
        else:
            daily_change = 0
        
        # Project forward
        forecast = []
        for day in range(1, days_ahead + 1):
            projected_value = current + (daily_change * day)
            forecast.append({
                'day': day,
                'projected_conversions': max(0, projected_value),
                'confidence': 0.85 - (day * 0.05)  # Confidence decreases with time
            })
        
        return {
            'campaign_id': campaign_id,
            'forecast_days': days_ahead,
            'current_conversions': current,
            'estimated_daily_growth': daily_change,
            'forecast': forecast,
            'generated_at': datetime.now().isoformat()
        }
    
    def predict_budget_efficiency(self, campaign_id: str) -> Dict:
        """Predict future budget efficiency"""
        spend_trend = self.metrics.get_metric_trend('spend', hours=7*24)
        roas_trend = self.metrics.get_metric_trend('roas', hours=7*24)
        
        if not spend_trend or not roas_trend:
            return {'prediction': 'Insufficient data'}
        
        current_spend = spend_trend[-1]['value'] if spend_trend else 0
        current_roas = roas_trend[-1]['value'] if roas_trend else 0
        
        # Analyze trend
        roas_values = [p['value'] for p in roas_trend]
        roas_trend_direction = 'up' if len(roas_values) > 1 and roas_values[-1] > roas_values[0] else 'down'
        
        return {
            'campaign_id': campaign_id,
            'current_daily_spend': current_spend,
            'current_roas': current_roas,
            'roas_trend': roas_trend_direction,
            'recommendation': 'Increase budget' if roas_trend_direction == 'up' else 'Review targeting',
            'predicted_7day_roi': current_roas * 7 * current_spend if current_roas > 0 else 0
        }
    
    def identify_optimization_opportunities(self, campaign_id: str) -> List[Dict]:
        """Identify opportunities for optimization"""
        opportunities = []
        
        cpc_trend = self.metrics.get_metric_trend('cpc', hours=7*24)
        if cpc_trend:
            cpc_values = [p['value'] for p in cpc_trend]
            if len(cpc_values) > 1 and cpc_values[-1] > cpc_values[0] * 1.2:
                opportunities.append({
                    'type': 'High CPC Trend',
                    'severity': 'High',
                    'recommendation': 'Review keyword bids and ad quality. Consider pausing underperforming keywords.',
                    'potential_savings': cpc_values[-1] - cpc_values[0]
                })
        
        ctr_trend = self.metrics.get_metric_trend('ctr', hours=7*24)
        if ctr_trend:
            ctr_values = [p['value'] for p in ctr_trend]
            if len(ctr_values) > 1 and ctr_values[-1] < ctr_values[0] * 0.8:
                opportunities.append({
                    'type': 'Declining CTR',
                    'severity': 'Medium',
                    'recommendation': 'Creative fatigue detected. Test new ad creatives and copy variations.',
                    'potential_impact': 'Could recover 20-30% of lost clicks'
                })
        
        return opportunities


class CustomReportBuilder:
    """Build custom reports"""
    
    def __init__(self):
        self.performance_report = PerformanceReport()
        self.predictive = PredictiveAnalytics()
    
    def build_executive_summary(self, campaign_ids: List[str]) -> Dict:
        """Build one-page executive summary"""
        summary = {
            'type': 'Executive Summary',
            'generated_at': datetime.now().isoformat(),
            'campaigns_covered': len(campaign_ids),
            'key_metrics': {
                'total_spend': 25000,
                'total_conversions': 875,
                'average_roas': 3.5,
                'average_cpa': 28.57
            },
            'top_performers': [],
            'bottom_performers': [],
            'critical_alerts': [],
            'recommendations': []
        }
        
        # Add sample data
        summary['critical_alerts'] = [
            'One campaign exceeds daily budget limits',
            'CTR declining in 2 campaigns',
            'CPA above threshold in 1 campaign'
        ]
        
        summary['recommendations'] = [
            'Scale budget for top 3 performing campaigns',
            'Pause bottom 2 campaigns until creative refresh',
            'Test new audiences in regional campaigns'
        ]
        
        return summary
    
    def build_detailed_report(self, campaign_id: str, include_forecast: bool = True) -> Dict:
        """Build detailed multi-section report"""
        report = {
            'campaign_id': campaign_id,
            'generated_at': datetime.now().isoformat(),
            'sections': {}
        }
        
        # Performance section
        report['sections']['performance'] = self.performance_report.generate_performance_report(campaign_id)
        
        # Forecast section (if requested)
        if include_forecast:
            report['sections']['forecast'] = self.predictive.forecast_conversions(campaign_id)
            report['sections']['opportunities'] = self.predictive.identify_optimization_opportunities(campaign_id)
        
        return report
    
    def export_report(self, report: Dict, format: str = 'json') -> str:
        """Export report in different formats"""
        if format == 'json':
            import json
            return json.dumps(report, indent=2, default=str)
        elif format == 'csv':
            return self._convert_to_csv(report)
        elif format == 'html':
            return self._convert_to_html(report)
        
        return str(report)
    
    def _convert_to_csv(self, report: Dict) -> str:
        """Convert report to CSV"""
        lines = ['Metric,Value']
        
        def flatten_dict(d, prefix=''):
            for k, v in d.items():
                if isinstance(v, dict):
                    flatten_dict(v, f"{prefix}{k}_")
                elif isinstance(v, list):
                    pass  # Skip lists for CSV
                else:
                    lines.append(f'{prefix}{k},{v}')
        
        flatten_dict(report)
        return '\n'.join(lines)
    
    def _convert_to_html(self, report: Dict) -> str:
        """Convert report to HTML"""
        html = '<html><body><h1>Report</h1>'
        
        def render_dict(d, depth=0):
            html_str = '<ul>'
            for k, v in d.items():
                if isinstance(v, dict):
                    html_str += f'<li><strong>{k}</strong><br/>{render_dict(v, depth+1)}</li>'
                elif isinstance(v, list):
                    html_str += f'<li><strong>{k}</strong><br/><ul>'
                    for item in v:
                        if isinstance(item, dict):
                            html_str += f'<li>{render_dict(item, depth+1)}</li>'
                        else:
                            html_str += f'<li>{item}</li>'
                    html_str += '</ul></li>'
                else:
                    html_str += f'<li><strong>{k}</strong>: {v}</li>'
            html_str += '</ul>'
            return html_str
        
        html += render_dict(report)
        html += '</body></html>'
        return html

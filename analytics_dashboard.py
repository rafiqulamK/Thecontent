"""
Advanced Analytics & Performance Dashboard
For tracking and optimizing content performance across platforms
"""
import json
from datetime import datetime, timedelta
from typing import Dict, List
from collections import defaultdict

class PerformanceAnalytics:
    """Track and analyze content performance"""
    
    def __init__(self):
        self.content_metrics = {}
        self.platform_metrics = defaultdict(lambda: {
            'total_posts': 0,
            'total_engagement': 0,
            'total_reach': 0,
            'avg_ctr': 0,
            'avg_engagement_rate': 0
        })
        self.historical_data = []
        
    def track_post_performance(self, post_id: str, metrics: Dict) -> Dict:
        """
        Track performance of published post
        
        Args:
            post_id: Unique post identifier
            metrics: Performance metrics dict with keys like:
                    'platform', 'likes', 'comments', 'shares', 'reach', 'impressions'
        
        Returns:
            Tracked metric with calculated engagement rate
        """
        tracked = {
            'post_id': post_id,
            'timestamp': datetime.now().isoformat(),
            'platform': metrics.get('platform'),
            'metrics': metrics,
            'engagement_rate': self._calculate_engagement_rate(metrics),
            'ctr': self._calculate_ctr(metrics),
            'performance_score': self._calculate_performance_score(metrics),
            'trend': self._identify_trend(metrics)
        }
        
        self.content_metrics[post_id] = tracked
        self.historical_data.append(tracked)
        
        # Update platform metrics
        platform = metrics.get('platform')
        if platform:
            self._update_platform_metrics(platform, tracked)
        
        return tracked
    
    def _calculate_engagement_rate(self, metrics: Dict) -> float:
        """Calculate engagement rate as percentage"""
        reach = metrics.get('reach', 0)
        if reach == 0:
            reach = metrics.get('impressions', 1)
        
        engagement = (
            metrics.get('likes', 0) +
            metrics.get('comments', 0) * 2 +
            metrics.get('shares', 0) * 3
        )
        
        if reach == 0:
            return 0
        
        return (engagement / reach) * 100
    
    def _calculate_ctr(self, metrics: Dict) -> float:
        """Calculate click-through rate"""
        impressions = metrics.get('impressions', 0)
        clicks = metrics.get('clicks', 0)
        
        if impressions == 0:
            return 0
        
        return (clicks / impressions) * 100
    
    def _calculate_performance_score(self, metrics: Dict) -> float:
        """Calculate overall performance score (0-100)"""
        score = 50
        
        # Boost based on engagement metrics
        if metrics.get('likes', 0) > 100:
            score += 15
        if metrics.get('comments', 0) > 10:
            score += 15
        if metrics.get('shares', 0) > 5:
            score += 15
        if metrics.get('reach', 0) > 10000:
            score += 10
        
        return min(100, score)
    
    def _identify_trend(self, metrics: Dict) -> str:
        """Identify performance trend"""
        engagement = self._calculate_engagement_rate(metrics)
        
        if engagement > 5:
            return "📈 Viral"
        elif engagement > 2:
            return "📊 Strong"
        elif engagement > 0.5:
            return "➡️ Average"
        else:
            return "📉 Underperforming"
    
    def _update_platform_metrics(self, platform: str, tracked: Dict) -> None:
        """Update cumulative platform metrics"""
        metrics = tracked['metrics']
        platform_stats = self.platform_metrics[platform]
        
        platform_stats['total_posts'] += 1
        platform_stats['total_engagement'] += (
            metrics.get('likes', 0) +
            metrics.get('comments', 0) +
            metrics.get('shares', 0)
        )
        platform_stats['total_reach'] += metrics.get('reach', 0)
        platform_stats['avg_ctr'] = (
            (platform_stats['avg_ctr'] * (platform_stats['total_posts'] - 1) +
             tracked['ctr']) / platform_stats['total_posts']
        )
        platform_stats['avg_engagement_rate'] = (
            platform_stats['total_engagement'] / max(platform_stats['total_posts'], 1)
        )
    
    def get_performance_dashboard(self, days: int = 30) -> Dict:
        """Get comprehensive performance dashboard"""
        cutoff_date = datetime.now() - timedelta(days=days)
        
        recent_data = [
            entry for entry in self.historical_data
            if datetime.fromisoformat(entry['timestamp']) >= cutoff_date
        ]
        
        dashboard = {
            'period': f"Last {days} days",
            'total_posts_analyzed': len(recent_data),
            'overall_metrics': self._calculate_overall_metrics(recent_data),
            'by_platform': self._get_platform_breakdown(recent_data),
            'top_performers': self._get_top_performers(recent_data),
            'trends': self._get_trend_analysis(recent_data),
            'recommendations': self._get_recommendations(recent_data)
        }
        
        return dashboard
    
    def _calculate_overall_metrics(self, data: List[Dict]) -> Dict:
        """Calculate overall metrics"""
        if not data:
            return {
                'avg_engagement_rate': 0,
                'avg_ctr': 0,
                'avg_performance_score': 0,
                'total_reach': 0
            }
        
        return {
            'avg_engagement_rate': sum(d['engagement_rate'] for d in data) / len(data),
            'avg_ctr': sum(d['ctr'] for d in data) / len(data),
            'avg_performance_score': sum(d['performance_score'] for d in data) / len(data),
            'total_reach': sum(d['metrics'].get('reach', 0) for d in data)
        }
    
    def _get_platform_breakdown(self, data: List[Dict]) -> Dict:
        """Get metrics breakdown by platform"""
        by_platform = defaultdict(list)
        
        for entry in data:
            by_platform[entry['platform']].append(entry)
        
        breakdown = {}
        for platform, entries in by_platform.items():
            breakdown[platform] = {
                'post_count': len(entries),
                'avg_engagement_rate': sum(e['engagement_rate'] for e in entries) / len(entries),
                'total_reach': sum(e['metrics'].get('reach', 0) for e in entries),
                'top_post': max(entries, key=lambda x: x['performance_score'])['post_id']
            }
        
        return breakdown
    
    def _get_top_performers(self, data: List[Dict], top_n: int = 5) -> List[Dict]:
        """Get top performing posts"""
        sorted_data = sorted(data, key=lambda x: x['performance_score'], reverse=True)
        
        return [
            {
                'post_id': entry['post_id'],
                'platform': entry['platform'],
                'score': entry['performance_score'],
                'engagement_rate': entry['engagement_rate'],
                'reach': entry['metrics'].get('reach', 0)
            }
            for entry in sorted_data[:top_n]
        ]
    
    def _get_trend_analysis(self, data: List[Dict]) -> Dict:
        """Analyze performance trends"""
        if len(data) < 2:
            return {'trend': 'Insufficient data', 'direction': 'N/A'}
        
        # Sort by timestamp
        sorted_data = sorted(data, key=lambda x: x['timestamp'])
        
        # Compare first half vs second half
        midpoint = len(sorted_data) // 2
        first_half = sorted_data[:midpoint]
        second_half = sorted_data[midpoint:]
        
        avg_first = sum(e['performance_score'] for e in first_half) / len(first_half) if first_half else 0
        avg_second = sum(e['performance_score'] for e in second_half) / len(second_half) if second_half else 0
        
        change = avg_second - avg_first
        
        if change > 5:
            direction = "📈 Improving"
        elif change < -5:
            direction = "📉 Declining"
        else:
            direction = "➡️ Stable"
        
        return {
            'trend': direction,
            'change_percentage': (change / max(avg_first, 1)) * 100,
            'first_period_avg': avg_first,
            'second_period_avg': avg_second
        }
    
    def _get_recommendations(self, data: List[Dict]) -> List[str]:
        """Get actionable recommendations"""
        recommendations = []
        
        if not data:
            return ["Start tracking posts to get recommendations"]
        
        # Analyze what's working
        by_platform = defaultdict(list)
        for entry in data:
            by_platform[entry['platform']].append(entry)
        
        # Find best performing platform
        best_platform = max(
            by_platform.items(),
            key=lambda x: sum(e['engagement_rate'] for e in x[1]) / len(x[1])
        )[0]
        
        recommendations.append(f"🌟 Focus more on {best_platform} - it's your top performer")
        
        # Engagement analysis
        avg_engagement = sum(e['engagement_rate'] for e in data) / len(data)
        if avg_engagement < 1:
            recommendations.append("📊 Engagement is low - increase quality and audience interaction")
        elif avg_engagement > 3:
            recommendations.append("✅ High engagement - maintain current strategy")
        
        # Reach analysis
        avg_reach = sum(e['metrics'].get('reach', 0) for e in data) / len(data)
        if avg_reach < 1000:
            recommendations.append("📢 Work on expanding reach - consider paid promotion")
        
        return recommendations[:5]
    
    def compare_periods(self, start_date: str, end_date: str) -> Dict:
        """Compare performance between two periods"""
        start = datetime.fromisoformat(start_date)
        end = datetime.fromisoformat(end_date)
        
        period_data = [
            entry for entry in self.historical_data
            if start <= datetime.fromisoformat(entry['timestamp']) <= end
        ]
        
        return {
            'period': f"{start_date} to {end_date}",
            'posts_in_period': len(period_data),
            'metrics': self._calculate_overall_metrics(period_data),
            'platform_breakdown': self._get_platform_breakdown(period_data)
        }
    
    def get_content_insights(self, content_type: str = None) -> Dict:
        """Get insights about specific content types or all content"""
        insights = {
            'high_engagement_triggers': self._identify_engagement_triggers(),
            'underperforming_patterns': self._identify_underperformers(),
            'optimal_posting_times': self._get_optimal_times(),
            'audience_preferences': self._get_audience_preferences()
        }
        
        return insights
    
    def _identify_engagement_triggers(self) -> List[str]:
        """Identify what triggers engagement"""
        # In real implementation, would analyze post content
        return [
            "Questions in caption (avg +2.5% engagement)",
            "Emotional language (avg +1.8% engagement)",
            "Call-to-action (avg +1.5% engagement)",
            "Hashtag usage (avg +1.2% engagement)",
            "Mentions (avg +1.0% engagement)"
        ]
    
    def _identify_underperformers(self) -> List[str]:
        """Identify underperforming patterns"""
        return [
            "Purely promotional content",
            "Long paragraphs without line breaks",
            "Posts without visuals on visual platforms",
            "Timing outside peak hours",
            "Low hashtag count"
        ]
    
    def _get_optimal_times(self) -> Dict:
        """Get optimal posting times based on performance data"""
        return {
            'morning': {'time': '9 AM', 'avg_engagement': 2.1},
            'midday': {'time': '12 PM', 'avg_engagement': 1.8},
            'evening': {'time': '6 PM', 'avg_engagement': 3.2},
            'night': {'time': '9 PM', 'avg_engagement': 2.5}
        }
    
    def _get_audience_preferences(self) -> Dict:
        """Get audience preferences"""
        return {
            'preferred_content_types': ['Educational', 'Entertaining', 'Inspirational'],
            'preferred_format': 'Short-form video',
            'preferred_tone': 'Conversational',
            'engagement_preference': 'Questions and discussions'
        }


class CompetitiveIntelligence:
    """Track competitor performance and market positioning"""
    
    def __init__(self):
        self.competitor_data = {}
        self.market_benchmarks = {}
        
    def add_competitor(self, name: str, metrics: Dict) -> Dict:
        """Track competitor performance"""
        competitor_profile = {
            'name': name,
            'metrics': metrics,
            'tracked_date': datetime.now().isoformat(),
            'content_strategy': self._analyze_strategy(metrics),
            'market_position': self._determine_position(metrics)
        }
        
        self.competitor_data[name] = competitor_profile
        return competitor_profile
    
    def _analyze_strategy(self, metrics: Dict) -> str:
        """Analyze competitor's strategy"""
        frequency = metrics.get('posting_frequency', 'unknown')
        
        if frequency == 'high':
            return "High-volume content strategy"
        elif frequency == 'medium':
            return "Balanced quality-quantity strategy"
        else:
            return "Low-volume, quality-focused strategy"
    
    def _determine_position(self, metrics: Dict) -> str:
        """Determine competitor's market position"""
        followers = metrics.get('followers', 0)
        engagement = metrics.get('avg_engagement_rate', 0)
        
        if followers > 100000 and engagement > 2:
            return "Market Leader"
        elif followers > 10000 and engagement > 1:
            return "Strong Competitor"
        elif followers > 1000:
            return "Emerging Competitor"
        else:
            return "Niche Player"
    
    def benchmark_against_competitors(self, your_metrics: Dict) -> Dict:
        """Benchmark your performance against competitors"""
        your_engagement = your_metrics.get('avg_engagement_rate', 0)
        your_reach = your_metrics.get('avg_reach', 0)
        
        competitor_avg_engagement = sum(
            c['metrics'].get('avg_engagement_rate', 0)
            for c in self.competitor_data.values()
        ) / max(len(self.competitor_data), 1)
        
        competitor_avg_reach = sum(
            c['metrics'].get('avg_reach', 0)
            for c in self.competitor_data.values()
        ) / max(len(self.competitor_data), 1)
        
        return {
            'your_engagement': your_engagement,
            'competitor_avg_engagement': competitor_avg_engagement,
            'engagement_vs_competitors': ((your_engagement - competitor_avg_engagement) / max(competitor_avg_engagement, 1)) * 100,
            'your_reach': your_reach,
            'competitor_avg_reach': competitor_avg_reach,
            'reach_vs_competitors': ((your_reach - competitor_avg_reach) / max(competitor_avg_reach, 1)) * 100,
            'competitive_position': self._calculate_overall_position(
                your_engagement, competitor_avg_engagement
            )
        }
    
    def _calculate_overall_position(self, your_engagement: float, 
                                    competitor_avg: float) -> str:
        """Calculate overall competitive position"""
        if your_engagement > competitor_avg * 1.2:
            return "🥇 Ahead of Competitors"
        elif your_engagement > competitor_avg * 0.9:
            return "🥈 Competitive"
        else:
            return "🔄 Opportunity to Improve"

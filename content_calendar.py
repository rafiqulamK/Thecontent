"""
Content Calendar & Scheduling Manager
For comprehensive content planning across platforms
"""
import json
from datetime import datetime, timedelta
from typing import Dict, List

class ContentCalendar:
    """Manage content calendar across multiple platforms"""
    
    def __init__(self):
        self.calendar = {}
        self.scheduled_posts = []
        self.content_themes = self._initialize_themes()
        
    def _initialize_themes(self) -> Dict:
        """Initialize content themes for different days/weeks"""
        return {
            'monday': 'Motivation Monday - Inspirational content',
            'tuesday': 'Tips & Tricks Tuesday - Educational content',
            'wednesday': 'Wisdom Wednesday - Thought leadership',
            'thursday': 'Throwback Thursday - Past successes',
            'friday': 'Feature Friday - Product/service highlights',
            'weekend': 'Engagement Weekend - Community focus'
        }
    
    def plan_weekly_content(self, platform: str, theme: str, 
                           topics: List[str], posting_times: Dict) -> List[Dict]:
        """
        Plan a week of content
        
        Args:
            platform: Social platform (twitter, instagram, etc)
            theme: Weekly theme
            topics: List of topics to cover
            posting_times: Dict with day->time mapping
        
        Returns:
            List of scheduled posts
        """
        weekly_plan = []
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        
        for i, day in enumerate(days):
            if i < len(topics):
                post = {
                    'day': day,
                    'date': (datetime.now() + timedelta(days=i)).strftime('%Y-%m-%d'),
                    'platform': platform,
                    'topic': topics[i],
                    'theme': self.content_themes.get(day.lower(), 'General'),
                    'posting_time': posting_times.get(day.lower(), '9:00 AM'),
                    'status': 'planned',
                    'content_type': self._determine_content_type(platform, i),
                    'estimated_reach': self._estimate_reach(platform),
                    'engagement_goal': self._set_engagement_goal(platform)
                }
                weekly_plan.append(post)
                self.scheduled_posts.append(post)
        
        return weekly_plan
    
    def _determine_content_type(self, platform: str, day_index: int) -> str:
        """Determine content type based on platform and day"""
        content_types = {
            'twitter': ['Thread', 'Quick tip', 'Question', 'News', 'Discussion', 'Poll', 'Thread'],
            'instagram': ['Carousel', 'Reel', 'Story', 'Post', 'Video', 'Story', 'Post'],
            'linkedin': ['Article', 'Post', 'Document', 'Video', 'Article', 'Poll', 'Post'],
            'facebook': ['Post', 'Video', 'Story', 'Event', 'Poll', 'Video', 'Story'],
            'tiktok': ['Video', 'Video', 'Video', 'Video', 'Video', 'Video', 'Video']
        }
        
        types_list = content_types.get(platform, ['Post', 'Post', 'Post', 'Post', 'Post', 'Post', 'Post'])
        return types_list[day_index % len(types_list)]
    
    def _estimate_reach(self, platform: str) -> int:
        """Estimate potential reach on platform"""
        reach_estimates = {
            'twitter': 500,
            'instagram': 1500,
            'linkedin': 800,
            'facebook': 1200,
            'tiktok': 3000
        }
        return reach_estimates.get(platform, 1000)
    
    def _set_engagement_goal(self, platform: str) -> Dict:
        """Set engagement goals"""
        goals = {
            'twitter': {'likes': 20, 'retweets': 5, 'replies': 3},
            'instagram': {'likes': 100, 'comments': 10, 'shares': 2},
            'linkedin': {'reactions': 50, 'comments': 5, 'shares': 2},
            'facebook': {'reactions': 80, 'comments': 8, 'shares': 3},
            'tiktok': {'likes': 500, 'comments': 50, 'shares': 10}
        }
        return goals.get(platform, {'likes': 50, 'comments': 5, 'shares': 1})
    
    def add_to_calendar(self, content: Dict, date: str, platform: str) -> Dict:
        """Add content to calendar"""
        calendar_entry = {
            'id': self._generate_id(),
            'content': content,
            'date': date,
            'platform': platform,
            'status': 'scheduled',
            'created_at': datetime.now().isoformat(),
            'scheduled_time': None,
            'posted_at': None
        }
        
        if date not in self.calendar:
            self.calendar[date] = []
        
        self.calendar[date].append(calendar_entry)
        return calendar_entry
    
    def get_calendar_view(self, start_date: str, end_date: str, 
                         platform: str = None) -> Dict:
        """Get calendar view for date range"""
        # Parse dates
        start = datetime.strptime(start_date, '%Y-%m-%d')
        end = datetime.strptime(end_date, '%Y-%m-%d')
        
        view = {
            'period': f"{start_date} to {end_date}",
            'platform': platform,
            'total_posts_planned': 0,
            'posts_by_day': {},
            'posting_schedule': []
        }
        
        current = start
        while current <= end:
            date_key = current.strftime('%Y-%m-%d')
            
            if date_key in self.calendar:
                posts = self.calendar[date_key]
                
                if platform:
                    posts = [p for p in posts if p['platform'] == platform]
                
                if posts:
                    view['posts_by_day'][date_key] = len(posts)
                    view['total_posts_planned'] += len(posts)
                    
                    for post in posts:
                        view['posting_schedule'].append({
                            'date': date_key,
                            'platform': post['platform'],
                            'time': post.get('scheduled_time', 'TBD'),
                            'status': post['status'],
                            'topic': post.get('content', {}).get('topic', 'N/A')
                        })
            
            current += timedelta(days=1)
        
        return view
    
    def optimize_posting_times(self, platform: str) -> Dict:
        """Get optimized posting times based on analytics"""
        optimal_times = {
            'twitter': {
                'best_hours': ['9 AM', '12 PM', '5 PM'],
                'best_days': ['Tuesday', 'Wednesday', 'Thursday'],
                'avoid_times': ['2-4 AM'],
                'reasoning': 'Peak user activity hours'
            },
            'instagram': {
                'best_hours': ['11 AM', '1 PM', '6 PM'],
                'best_days': ['Wednesday', 'Thursday', 'Friday'],
                'avoid_times': ['Late night'],
                'reasoning': 'Peak engagement hours'
            },
            'linkedin': {
                'best_hours': ['8 AM', '12 PM', '6 PM'],
                'best_days': ['Tuesday', 'Wednesday', 'Thursday'],
                'avoid_times': ['Weekends', 'Late evening'],
                'reasoning': 'Professional activity hours'
            },
            'facebook': {
                'best_hours': ['1 PM', '7 PM', '8 PM'],
                'best_days': ['Thursday', 'Friday', 'Saturday'],
                'avoid_times': ['Early morning'],
                'reasoning': 'Peak family activity hours'
            },
            'tiktok': {
                'best_hours': ['6 PM', '7 PM', '8 PM'],
                'best_days': ['Friday', 'Saturday', 'Sunday'],
                'avoid_times': ['Morning hours'],
                'reasoning': 'Peak teen/young adult activity'
            }
        }
        
        return optimal_times.get(platform, {
            'best_hours': ['9 AM', '12 PM', '6 PM'],
            'best_days': ['Tuesday-Thursday'],
            'avoid_times': ['2-4 AM']
        })
    
    def suggest_content_pillar(self, platform: str, audience: str) -> List[Dict]:
        """Suggest content pillars for strategy"""
        pillars = {
            'marketing': [
                {
                    'pillar': 'Education',
                    'percentage': 40,
                    'description': 'Tips, tutorials, how-tos',
                    'examples': ['Step-by-step guides', 'Industry insights', 'Best practices']
                },
                {
                    'pillar': 'Engagement',
                    'percentage': 30,
                    'description': 'Community and interaction',
                    'examples': ['Questions', 'Polls', 'Discussions', 'User features']
                },
                {
                    'pillar': 'Promotion',
                    'percentage': 20,
                    'description': 'Product/service promotion',
                    'examples': ['Product launches', 'Offers', 'Case studies']
                },
                {
                    'pillar': 'Entertainment',
                    'percentage': 10,
                    'description': 'Fun and personality',
                    'examples': ['Memes', 'Behind-the-scenes', 'Team culture']
                }
            ],
            'b2b': [
                {
                    'pillar': 'Thought Leadership',
                    'percentage': 40,
                    'description': 'Industry insights and expertise',
                    'examples': ['Research findings', 'Industry trends', 'Expert analysis']
                },
                {
                    'pillar': 'Company Culture',
                    'percentage': 20,
                    'description': 'Team and company stories',
                    'examples': ['Team spotlights', 'Company news', 'Office stories']
                },
                {
                    'pillar': 'Educational',
                    'percentage': 25,
                    'description': 'Educational content',
                    'examples': ['Webinars', 'Guides', 'Tutorials']
                },
                {
                    'pillar': 'Community',
                    'percentage': 15,
                    'description': 'Engagement and networking',
                    'examples': ['Networking events', 'Partnerships', 'User stories']
                }
            ]
        }
        
        return pillars.get(audience, pillars['marketing'])
    
    def _generate_id(self) -> str:
        """Generate unique ID for calendar entry"""
        import hashlib
        timestamp = datetime.now().isoformat()
        return hashlib.md5(timestamp.encode()).hexdigest()[:8]
    
    def get_posting_analytics(self) -> Dict:
        """Get analytics on posting patterns"""
        total_posts = len(self.scheduled_posts)
        platform_breakdown = {}
        
        for post in self.scheduled_posts:
            platform = post.get('platform')
            if platform not in platform_breakdown:
                platform_breakdown[platform] = 0
            platform_breakdown[platform] += 1
        
        return {
            'total_scheduled_posts': total_posts,
            'posts_by_platform': platform_breakdown,
            'posting_days_covered': len(self.calendar),
            'average_posts_per_day': total_posts / max(len(self.calendar), 1),
            'recommended_optimization': self._get_optimization_recommendation(platform_breakdown)
        }
    
    def _get_optimization_recommendation(self, platform_breakdown: Dict) -> str:
        """Get optimization recommendation based on posting patterns"""
        if len(platform_breakdown) == 1:
            return "Consider expanding to multiple platforms for wider reach"
        elif not any(count > 3 for count in platform_breakdown.values()):
            return "Consider increasing posting frequency on high-engagement platforms"
        else:
            return "Good platform diversity and frequency distribution"


class ContentScheduler:
    """Schedule and manage content publishing"""
    
    def __init__(self):
        self.scheduled_queue = []
        self.published_log = []
        
    def schedule_post(self, content: str, platform: str, 
                     publish_date: str, publish_time: str) -> Dict:
        """Schedule a post for publishing"""
        scheduled_item = {
            'id': self._generate_id(),
            'content': content,
            'platform': platform,
            'scheduled_date': publish_date,
            'scheduled_time': publish_time,
            'status': 'scheduled',
            'created_at': datetime.now().isoformat(),
            'retry_count': 0
        }
        
        self.scheduled_queue.append(scheduled_item)
        return scheduled_item
    
    def publish_post(self, post_id: str) -> Dict:
        """Publish a scheduled post"""
        for item in self.scheduled_queue:
            if item['id'] == post_id:
                item['status'] = 'published'
                item['published_at'] = datetime.now().isoformat()
                self.published_log.append(item)
                self.scheduled_queue.remove(item)
                
                return {
                    'success': True,
                    'post_id': post_id,
                    'platform': item['platform'],
                    'published_at': item['published_at']
                }
        
        return {
            'success': False,
            'error': f'Post {post_id} not found'
        }
    
    def get_pending_posts(self) -> List[Dict]:
        """Get all pending posts ready to publish"""
        now = datetime.now()
        pending = []
        
        for item in self.scheduled_queue:
            if item['status'] == 'scheduled':
                scheduled_dt = datetime.strptime(
                    f"{item['scheduled_date']} {item['scheduled_time']}", 
                    '%Y-%m-%d %H:%M'
                )
                
                if scheduled_dt <= now:
                    pending.append(item)
        
        return pending
    
    def _generate_id(self) -> str:
        """Generate unique ID"""
        import hashlib
        timestamp = datetime.now().isoformat()
        return hashlib.md5(timestamp.encode()).hexdigest()[:12]

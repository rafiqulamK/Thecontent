import ollama
import json
from datetime import datetime, timedelta
import schedule
import time
from typing import List, Dict, Optional
import random

class TrendAnalyzer:
    """Analyze and incorporate current trends into content generation"""
    
    def __init__(self):
        self.trending_topics = []
        self.seasonal_context = ""
        self.industry_insights = {}
        
    def get_current_context(self) -> Dict:
        """Get current date/time context for trend-aware generation"""
        now = datetime.now()
        month = now.strftime("%B")
        day_of_week = now.strftime("%A")
        
        context = {
            'current_date': now.isoformat(),
            'month': month,
            'day_of_week': day_of_week,
            'season': self._get_season(now.month),
            'is_weekend': now.weekday() >= 5,
            'hour': now.hour
        }
        return context
    
    def _get_season(self, month: int) -> str:
        """Get current season based on month"""
        if month in [12, 1, 2]:
            return "Winter"
        elif month in [3, 4, 5]:
            return "Spring"
        elif month in [6, 7, 8]:
            return "Summer"
        else:
            return "Fall"
    
    def add_trending_topic(self, topic: str):
        """Add a trending topic to track"""
        if topic not in self.trending_topics:
            self.trending_topics.append(topic)
    
    def set_industry_insights(self, insights: Dict):
        """Set current industry insights"""
        self.industry_insights = insights


class CreativeOptimizer:
    """Omneky-inspired creative optimization for better ad performance"""
    
    def __init__(self):
        self.creative_variants = []
        self.performance_scores = {}
        
    def optimize_creative(self, content: str, platform: str) -> Dict:
        """
        Optimize creative based on Omneky principles
        - Hook optimization
        - Emotional triggers
        - Call-to-action effectiveness
        """
        optimization_rules = {
            'hook_strength': self._score_hook(content),
            'emotional_appeal': self._score_emotional_appeal(content),
            'clarity_score': self._score_clarity(content),
            'cta_effectiveness': self._score_cta(content),
            'platform_fit': self._score_platform_fit(content, platform),
            'overall_score': 0
        }
        
        # Calculate overall score
        scores = list(optimization_rules.values())[:-1]
        optimization_rules['overall_score'] = sum(scores) / len(scores) if scores else 0
        
        return optimization_rules
    
    def _score_hook(self, content: str) -> float:
        """Score the opening hook quality (0-100)"""
        hook_words = ['discover', 'revealed', 'shocking', 'breakthrough', 'secret', 
                     'urgent', 'wait', 'don\'t', 'you won\'t', 'finally']
        hook_score = sum(10 for word in hook_words if word.lower() in content.lower())
        
        # First 20 characters should be engaging
        first_20 = content[:20].lower()
        if any(word in first_20 for word in hook_words):
            hook_score += 20
        
        return min(hook_score, 100)
    
    def _score_emotional_appeal(self, content: str) -> float:
        """Score emotional triggers (0-100)"""
        emotional_words = [
            'love', 'amazing', 'incredible', 'transform', 'success', 'powerful',
            'exclusive', 'limited', 'urgent', 'essential', 'game-changing',
            'revolutionary', 'unbelievable', 'stunning', 'massive', 'proven'
        ]
        score = sum(10 for word in emotional_words if word.lower() in content.lower())
        return min(score, 100)
    
    def _score_clarity(self, content: str) -> float:
        """Score message clarity (0-100)"""
        # Shorter, clearer messages score higher
        avg_word_length = sum(len(word) for word in content.split()) / max(len(content.split()), 1)
        clarity = 100 - (avg_word_length - 4) * 5  # Optimal word length ~4 chars
        return max(0, min(clarity, 100))
    
    def _score_cta(self, content: str) -> float:
        """Score call-to-action effectiveness (0-100)"""
        cta_words = ['click', 'learn', 'discover', 'get', 'shop', 'download',
                    'subscribe', 'register', 'join', 'start', 'try', 'explore',
                    'view', 'check out', 'grab', 'snag', 'secure']
        cta_score = 0
        for word in cta_words:
            if word.lower() in content.lower():
                cta_score += 20
        
        # Bonus if CTA is at the end
        last_20_words = ' '.join(content.split()[-20:]).lower()
        if any(word in last_20_words for word in cta_words):
            cta_score += 10
        
        return min(cta_score, 100)
    
    def _score_platform_fit(self, content: str, platform: str) -> float:
        """Score platform-specific optimization (0-100)"""
        platform_optimal_length = {
            'twitter': (50, 250),      # 50-250 chars optimal
            'linkedin': (150, 1300),   # LinkedIn likes longer form
            'instagram': (50, 2200),   # Instagram captions can be long
            'facebook': (50, 500),     # Facebook medium-length
            'tiktok': (30, 100)        # TikTok short and punchy
        }
        
        content_len = len(content)
        if platform.lower() in platform_optimal_length:
            min_len, max_len = platform_optimal_length[platform.lower()]
            if min_len <= content_len <= max_len:
                return 100
            elif min_len <= content_len <= max_len * 1.2:
                return 80
            else:
                return 50
        return 70


class CampaignAnalyzer:
    """Madgicx-inspired campaign performance analysis and optimization"""
    
    def __init__(self):
        self.campaigns = {}
        self.performance_metrics = {}
    
    def predict_performance(self, content: Dict, audience: Dict) -> Dict:
        """
        Predict campaign performance based on Madgicx principles
        - Audience alignment
        - Creative quality
        - Timing optimization
        - Budget efficiency recommendations
        """
        predictions = {
            'estimated_ctr': self._estimate_ctr(content, audience),
            'estimated_cpc': self._estimate_cpc(content, audience),
            'quality_score': self._calculate_quality_score(content),
            'audience_alignment': self._score_audience_alignment(content, audience),
            'scaling_potential': self._evaluate_scaling_potential(content, audience),
            'recommendations': self._generate_recommendations(content, audience),
            'timestamp': datetime.now().isoformat()
        }
        return predictions
    
    def _estimate_ctr(self, content: Dict, audience: Dict) -> float:
        """Estimate Click-Through Rate (0-10%)"""
        base_ctr = 2.0
        
        # Content quality factor
        if content.get('optimization_score', 0) > 80:
            base_ctr += 1.5
        elif content.get('optimization_score', 0) > 60:
            base_ctr += 0.8
        
        # Audience relevance factor
        if audience.get('interest_match', 0) > 80:
            base_ctr += 1.2
        
        # Timing factor
        context = content.get('context', {})
        if context.get('is_weekend'):
            base_ctr -= 0.5
        
        return min(base_ctr, 10.0)
    
    def _estimate_cpc(self, content: Dict, audience: Dict) -> float:
        """Estimate Cost Per Click (in cents)"""
        platform = content.get('platform', 'facebook').lower()
        
        base_cpc = {
            'facebook': 0.50,
            'instagram': 0.40,
            'linkedin': 2.50,
            'twitter': 1.00,
            'tiktok': 0.30
        }.get(platform, 0.50)
        
        # Quality factor (higher quality = lower cost)
        quality_factor = 1.0 - (content.get('optimization_score', 0) / 100 * 0.4)
        
        # Audience saturation factor
        audience_factor = 1.0 + (audience.get('saturation', 0.5) * 0.5)
        
        return max(base_cpc * quality_factor * audience_factor, 0.10)
    
    def _calculate_quality_score(self, content: Dict) -> float:
        """Calculate content quality score (0-100)"""
        score = 50
        
        # Optimization score (Omneky)
        if 'optimization_score' in content:
            score += content['optimization_score'] * 0.3
        
        # Trend awareness
        if content.get('trend_aware'):
            score += 10
        
        # Content type variety
        if content.get('generation_type') == 'keyword_optimized':
            score += 5
        
        return min(score, 100)
    
    def _score_audience_alignment(self, content: Dict, audience: Dict) -> float:
        """Score how well content aligns with target audience (0-100)"""
        alignment = 50
        
        # Tone matching
        if content.get('tone') == audience.get('preferred_tone'):
            alignment += 20
        
        # Interest matching
        if 'interests' in audience and content.get('keywords'):
            matching_interests = len(set(audience['interests']) & set(content.get('keywords', [])))
            alignment += matching_interests * 5
        
        return min(alignment, 100)
    
    def _evaluate_scaling_potential(self, content: Dict, audience: Dict) -> Dict:
        """Evaluate if campaign can be scaled (Madgicx approach)"""
        quality_score = content.get('optimization_score', 0)
        audience_size = audience.get('audience_size', 1000000)
        
        if quality_score > 80 and audience_size > 500000:
            scaling_status = "Ready to Scale"
            scaling_multiplier = 1.5
        elif quality_score > 60 and audience_size > 250000:
            scaling_status = "Can Scale with Optimization"
            scaling_multiplier = 1.2
        else:
            scaling_status = "Test & Optimize First"
            scaling_multiplier = 1.0
        
        return {
            'status': scaling_status,
            'budget_multiplier': scaling_multiplier,
            'recommendation': f"Start with 1-2x budget if {scaling_status.lower()}"
        }
    
    def _generate_recommendations(self, content: Dict, audience: Dict) -> List[str]:
        """Generate actionable optimization recommendations"""
        recommendations = []
        
        quality = content.get('optimization_score', 0)
        if quality < 70:
            recommendations.append("Strengthen emotional appeal and hook")
        
        if quality < 60:
            recommendations.append("Improve call-to-action clarity")
        
        if not content.get('trend_aware'):
            recommendations.append("Incorporate current trends for relevance")
        
        if audience.get('audience_size', 1000000) < 100000:
            recommendations.append("Expand audience targeting for better reach")
        
        if content.get('platform') == 'instagram' and 'keywords' not in content:
            recommendations.append("Add keyword-optimized hashtags for discovery")
        
        if len(recommendations) == 0:
            recommendations.append("Content is well-optimized. Ready to launch!")
        
        return recommendations


class SocialMediaGenerator:
    """Generate social media content using Omneky + Madgicx optimization principles"""
    
    def __init__(self, model: str = 'gemma:2b'):
        """
        Initialize the Social Media Generator with optimization engines
        
        Args:
            model: The Ollama model to use (default: gemma:2b)
        """
        self.model = model
        self.content_history = []
        self.trend_analyzer = TrendAnalyzer()
        self.creative_optimizer = CreativeOptimizer()
        self.campaign_analyzer = CampaignAnalyzer()
        self.trending_topics = [
            "AI", "machine learning", "web3", "sustainability",
            "creator economy", "remote work", "automation"
        ]
        
    def generate_post(
        self,
        platform: str,
        topic: str,
        tone: str = "professional",
        temperature: float = 0.7,
        include_trends: bool = True,
        hashtag_strategy: str = "trending"
    ) -> Dict:
        """
        Generate a social media post with trend awareness
        
        Args:
            platform: Social media platform (twitter, linkedin, instagram, etc.)
            topic: Topic for the post
            tone: Tone of voice (professional, casual, funny, inspirational, urgent)
            temperature: Creativity level (0.0-1.0)
            include_trends: Include trending topics in the post
            hashtag_strategy: Hashtag strategy (trending, niche, balanced)
            
        Returns:
            Dictionary with generated post and metadata
        """
        # Get current context for trend awareness
        context = self.trend_analyzer.get_current_context()
        
        # Build trend-aware prompt
        trend_context = ""
        if include_trends:
            trend_context = f"""
Additional context for relevance:
- Current season: {context['season']}
- Day: {context['day_of_week']}
- Time-sensitive: Create content relevant to current times
- Trending keywords to consider: {', '.join(self.trending_topics[:3])}
"""
        
        hashtag_instruction = self._get_hashtag_instruction(platform, hashtag_strategy)
        
        prompt = f"""
Create a {platform} post about {topic}.
Tone: {tone}
Requirements:
1. Engaging opening that captures attention
2. Clear, concise message
3. Current and relevant context
{hashtag_instruction}
5. Strong call to action
6. Make it shareable and trendy
{trend_context}

{platform} Post:
"""
        
        try:
            response = ollama.generate(
                model=self.model,
                prompt=prompt,
                options={'temperature': temperature, 'num_predict': 200}
            )
            
            post = {
                'platform': platform,
                'topic': topic,
                'tone': tone,
                'content': response['response'],
                'model': self.model,
                'timestamp': datetime.now().isoformat(),
                'context': context,
                'hashtag_strategy': hashtag_strategy,
                'trend_aware': include_trends
            }
            
            self.content_history.append(post)
            return post
        except Exception as e:
            print(f"Error generating post: {e}")
            return {
                'platform': platform,
                'topic': topic,
                'tone': tone,
                'content': f"Error generating content: {str(e)}",
                'error': True,
                'timestamp': datetime.now().isoformat()
            }
    
    def _get_hashtag_instruction(self, platform: str, strategy: str) -> str:
        """Get hashtag instruction based on platform and strategy"""
        if platform.lower() == "twitter":
            return "4. Use 2-3 relevant hashtags (max 3 hashtags)"
        elif platform.lower() == "instagram":
            if strategy == "trending":
                return "4. Use 15-30 trending and relevant hashtags"
            elif strategy == "niche":
                return "4. Use 10-15 niche-specific hashtags"
            else:  # balanced
                return "4. Use 15-20 mixed hashtags (trending + niche)"
        elif platform.lower() == "linkedin":
            return "4. Use 3-5 professional hashtags"
        elif platform.lower() == "facebook":
            return "4. Use 5-8 relevant hashtags"
        else:
            return "4. Use platform-appropriate hashtags"
    
    def batch_generate(
        self,
        content_calendar: List[Dict],
        temperature: float = 0.7,
        include_trends: bool = True
    ) -> List[Dict]:
        """
        Generate content for multiple items with trend awareness
        
        Args:
            content_calendar: List of content items with platform, topic, and optional tone
            temperature: Creativity level for all posts
            include_trends: Include trending topics in posts
            
        Returns:
            List of generated posts
        """
        generated = []
        for i, item in enumerate(content_calendar, 1):
            print(f"Generating post {i}/{len(content_calendar)}...")
            try:
                post = self.generate_post(
                    platform=item['platform'],
                    topic=item['topic'],
                    tone=item.get('tone', 'professional'),
                    temperature=temperature,
                    include_trends=include_trends,
                    hashtag_strategy=item.get('hashtag_strategy', 'trending')
                )
                generated.append(post)
            except Exception as e:
                print(f"Error generating post {i}: {e}")
        return generated
    
    def analyze_content_performance(self) -> Dict:
        """Analyze generated content for insights"""
        if not self.content_history:
            return {'error': 'No content history available'}
        
        analysis = {
            'total_posts': len(self.content_history),
            'platforms': {},
            'average_length': 0,
            'tone_distribution': {},
            'recent_posts': self.content_history[-5:],
            'timestamp': datetime.now().isoformat()
        }
        
        total_length = 0
        for post in self.content_history:
            # Platform analysis
            platform = post.get('platform', 'unknown')
            analysis['platforms'][platform] = analysis['platforms'].get(platform, 0) + 1
            
            # Tone analysis
            tone = post.get('tone', 'unknown')
            analysis['tone_distribution'][tone] = analysis['tone_distribution'].get(tone, 0) + 1
            
            # Length analysis
            if 'content' in post:
                total_length += len(post['content'])
        
        if self.content_history:
            analysis['average_length'] = total_length // len(self.content_history)
        
        return analysis
    
    def get_trending_suggestions(self, industry: str = "technology") -> List[str]:
        """Get trending topic suggestions for a given industry"""
        industry_trends = {
            'technology': [
                'AI and machine learning advances',
                'Web3 and blockchain',
                'Cybersecurity trends',
                'Cloud computing innovations',
                'DevOps practices',
                'API development',
                'Low-code/no-code platforms'
            ],
            'marketing': [
                'AI-powered personalization',
                'Omnichannel strategies',
                'Video marketing trends',
                'Influencer partnerships',
                'User-generated content',
                'Community building',
                'Data privacy and compliance'
            ],
            'business': [
                'Digital transformation',
                'Remote work optimization',
                'Sustainability initiatives',
                'Supply chain resilience',
                'Customer experience innovation',
                'Business intelligence',
                'Workplace culture'
            ],
            'finance': [
                'Fintech innovation',
                'Sustainable investing',
                'Cryptocurrency markets',
                'Digital payments',
                'Wealth management trends',
                'Financial wellness',
                'Investment diversification'
            ]
        }
        
        return industry_trends.get(industry.lower(), self.trending_topics)
    
    def generate_with_keywords(
        self,
        platform: str,
        topic: str,
        keywords: List[str],
        tone: str = "professional",
        temperature: float = 0.7
    ) -> Dict:
        """Generate post with specific keywords incorporated"""
        keywords_str = ', '.join(keywords)
        
        prompt = f"""
Create a {platform} post about {topic}.
Tone: {tone}

Must include these keywords naturally: {keywords_str}

Requirements:
1. Engaging opening
2. Clear message incorporating the keywords
3. Relevant hashtags
4. Strong call to action
5. Make it trend-aware and current

{platform} Post:
"""
        
        try:
            response = ollama.generate(
                model=self.model,
                prompt=prompt,
                options={'temperature': temperature, 'num_predict': 200}
            )
            
            post = {
                'platform': platform,
                'topic': topic,
                'tone': tone,
                'content': response['response'],
                'keywords': keywords,
                'model': self.model,
                'timestamp': datetime.now().isoformat(),
                'generation_type': 'keyword_optimized'
            }
            
            self.content_history.append(post)
            return post
        except Exception as e:
            print(f"Error generating keyword-optimized post: {e}")
            return {'error': str(e)}
    
    def save_history(self, filename: str = "content_library.json") -> None:
        """
        Save content history to file
        
        Args:
            filename: Output JSON file path
        """
        try:
            with open(filename, 'r') as f:
                existing = json.load(f)
        except FileNotFoundError:
            existing = []
        
        existing.extend(self.content_history)
        
        with open(filename, 'w') as f:
            json.dump(existing, f, indent=2)
        
        print(f"Saved {len(self.content_history)} posts to {filename}")
    
    @staticmethod
    def load_content(filename: str = "content_library.json") -> List[Dict]:
        """
        Load saved content from file
        
        Args:
            filename: Input JSON file path
            
        Returns:
            List of saved posts
        """
        try:
            with open(filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []
    
    @staticmethod
    def search_content(keyword: str, filename: str = "content_library.json") -> List[Dict]:
        """
        Search through saved content
        
        Args:
            keyword: Search keyword
            filename: Content library file
            
        Returns:
            List of matching posts
        """
        library = SocialMediaGenerator.load_content(filename)
        results = []
        for post in library:
            if keyword.lower() in post['content'].lower():
                results.append(post)
        return results


def schedule_content_generation():
    """
    Example function to schedule content generation
    This can be run in a separate process or container
    """
    generator = SocialMediaGenerator()
    
    # Content calendar for the week
    content_calendar = [
        {'platform': 'twitter', 'topic': 'AI in marketing', 'tone': 'professional'},
        {'platform': 'linkedin', 'topic': 'Digital transformation', 'tone': 'professional'},
        {'platform': 'instagram', 'topic': 'Behind the scenes', 'tone': 'casual'},
        {'platform': 'twitter', 'topic': 'Machine learning tips', 'tone': 'helpful'},
        {'platform': 'facebook', 'topic': 'Community updates', 'tone': 'friendly'},
    ]
    
    # Generate all posts
    posts = generator.batch_generate(content_calendar)
    
    # Display results
    print("\n" + "="*60)
    print("GENERATED CONTENT")
    print("="*60)
    for post in posts:
        print(f"\n=== {post['platform'].upper()} ===")
        print(f"Topic: {post['topic']}")
        print(f"Tone: {post['tone']}")
        print("-" * 60)
        print(post['content'])
        print("-" * 60)
    
    # Save to file
    generator.save_history()


if __name__ == "__main__":
    print("Starting Social Media Content Generator...")
    schedule_content_generation()

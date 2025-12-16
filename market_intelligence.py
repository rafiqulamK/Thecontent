"""
Competitor Analysis & Market Intelligence Engine
For Omneky-like competitive positioning and Madgicx-like market insights
"""

from typing import Dict, List

class CompetitorAnalysis:
    """Analyze competitor content and market positioning"""
    
    def __init__(self):
        self.competitor_database = {}
        self.market_trends = {}
        self.content_templates = self._get_content_templates()
        
    def analyze_competitor_content(self, competitor_name: str, 
                                  competitor_content: str,
                                  your_content: str) -> Dict:
        """
        Analyze how your content compares to competitors
        
        Args:
            competitor_name: Name of competitor
            competitor_content: Competitor's content
            your_content: Your content
        
        Returns:
            Comparative analysis
        """
        analysis = {
            'competitor': competitor_name,
            'competitor_score': self._score_content(competitor_content),
            'your_score': self._score_content(your_content),
            'competitive_advantage': self._find_advantages(your_content, competitor_content),
            'gaps': self._find_gaps(your_content, competitor_content),
            'recommendations': self._get_recommendations(your_content, competitor_content),
            'positioning': self._determine_positioning(your_content, competitor_content)
        }
        return analysis
    
    def _score_content(self, content: str) -> Dict:
        """Score content on multiple dimensions"""
        return {
            'originality': self._score_originality(content),
            'clarity': self._score_clarity(content),
            'emotional_appeal': self._score_emotional_appeal(content),
            'persuasiveness': self._score_persuasiveness(content),
            'differentiation': self._score_differentiation(content),
            'overall': self._calculate_overall_score(content)
        }
    
    def _score_originality(self, content: str) -> float:
        """Score how original content is (0-100)"""
        score = 70
        
        common_phrases = ['best', 'amazing', 'great', 'good', 'nice']
        score -= len([p for p in common_phrases if p in content.lower()]) * 5
        
        return max(0, min(100, score))
    
    def _score_clarity(self, content: str) -> float:
        """Score content clarity"""
        words = content.split()
        sentences = content.split('.')
        
        if len(sentences) > 0:
            avg_sentence = len(words) / len(sentences)
            if 10 <= avg_sentence <= 20:
                return 95
            elif 5 <= avg_sentence <= 25:
                return 85
            else:
                return 70
        return 50
    
    def _score_emotional_appeal(self, content: str) -> float:
        """Score emotional appeal"""
        emotional_words = ['love', 'amazing', 'incredible', 'powerful', 'transform',
                          'exclusive', 'limited', 'urgent', 'life-changing']
        
        count = sum(1 for word in emotional_words if word in content.lower())
        return min(100, 50 + (count * 8))
    
    def _score_persuasiveness(self, content: str) -> float:
        """Score persuasiveness"""
        score = 50
        
        # Benefit statements
        if 'benefit' in content.lower() or 'will' in content.lower():
            score += 15
        
        # Social proof
        if any(word in content.lower() for word in ['proven', 'trusted', 'verified']):
            score += 15
        
        # CTA
        if any(word in content.lower() for word in ['click', 'join', 'get', 'learn']):
            score += 15
        
        return min(100, score)
    
    def _score_differentiation(self, content: str) -> float:
        """Score how differentiated the message is"""
        score = 60
        
        unique_angles = ['unique', 'only', 'exclusive', 'proprietary', 'patent']
        for angle in unique_angles:
            if angle in content.lower():
                score += 10
        
        return min(100, score)
    
    def _calculate_overall_score(self, content: str) -> float:
        """Calculate overall content score"""
        return (
            self._score_originality(content) * 0.15 +
            self._score_clarity(content) * 0.20 +
            self._score_emotional_appeal(content) * 0.20 +
            self._score_persuasiveness(content) * 0.25 +
            self._score_differentiation(content) * 0.20
        )
    
    def _find_advantages(self, your_content: str, competitor_content: str) -> List[str]:
        """Find competitive advantages in your content"""
        advantages = []
        
        your_score = self._calculate_overall_score(your_content)
        comp_score = self._calculate_overall_score(competitor_content)
        
        if your_score > comp_score:
            advantages.append(f"Overall higher content quality (+{your_score - comp_score:.0f} points)")
        
        if self._score_originality(your_content) > self._score_originality(competitor_content):
            advantages.append("More original message")
        
        if self._score_emotional_appeal(your_content) > self._score_emotional_appeal(competitor_content):
            advantages.append("Stronger emotional appeal")
        
        if self._score_clarity(your_content) > self._score_clarity(competitor_content):
            advantages.append("Clearer messaging")
        
        if not advantages:
            advantages.append("Competitive on most metrics")
        
        return advantages
    
    def _find_gaps(self, your_content: str, competitor_content: str) -> List[str]:
        """Find gaps in your positioning vs competitors"""
        gaps = []
        
        if self._score_persuasiveness(your_content) < self._score_persuasiveness(competitor_content):
            gaps.append("Improve persuasive elements")
        
        if self._score_differentiation(your_content) < self._score_differentiation(competitor_content):
            gaps.append("Need stronger differentiation")
        
        if 'you' not in your_content.lower() and 'you' in competitor_content.lower():
            gaps.append("Lack audience-focused language")
        
        if not gaps:
            gaps.append("Content is well-positioned")
        
        return gaps
    
    def _get_recommendations(self, your_content: str, competitor_content: str) -> List[str]:
        """Get recommendations for improvement"""
        recommendations = []
        
        gaps = self._find_gaps(your_content, competitor_content)
        if gaps:
            recommendations.extend(gaps)
        
        # Add specific improvements
        if len(your_content) < 100:
            recommendations.append("Expand content with more details")
        
        if '?' not in your_content:
            recommendations.append("Add questions to engage readers")
        
        if not any(word in your_content.lower() for word in ['exclusive', 'limited', 'only']):
            recommendations.append("Add scarcity or exclusivity messaging")
        
        return recommendations[:5]
    
    def _determine_positioning(self, your_content: str, competitor_content: str) -> str:
        """Determine market positioning strategy"""
        your_score = self._calculate_overall_score(your_content)
        comp_score = self._calculate_overall_score(competitor_content)
        
        if your_score > comp_score + 10:
            return "🥇 Premium Positioning - Lead on quality"
        elif your_score > comp_score:
            return "🥈 Competitive Positioning - Match or exceed competitor"
        elif your_score >= comp_score - 5:
            return "⚖️ Parity Positioning - Keep pace"
        else:
            return "🔄 Improvement Needed - Need to differentiate"


class MarketIntelligence:
    """Market intelligence and trend analysis"""
    
    def __init__(self):
        self.market_data = {}
        self.content_performance_benchmarks = self._get_benchmarks()
        
    def _get_benchmarks(self) -> Dict:
        """Industry benchmarks for different content types"""
        return {
            'twitter': {
                'avg_ctr': 2.5,
                'avg_engagement': 1.2,
                'optimal_length': 140,
                'best_time': 'Tuesday 9AM'
            },
            'instagram': {
                'avg_ctr': 3.5,
                'avg_engagement': 4.2,
                'optimal_length': 150,
                'best_time': 'Wednesday 6PM'
            },
            'linkedin': {
                'avg_ctr': 2.0,
                'avg_engagement': 1.8,
                'optimal_length': 150,
                'best_time': 'Thursday 8AM'
            },
            'facebook': {
                'avg_ctr': 1.8,
                'avg_engagement': 2.5,
                'optimal_length': 150,
                'best_time': 'Friday 1PM'
            },
            'tiktok': {
                'avg_ctr': 5.2,
                'avg_engagement': 8.5,
                'optimal_length': 50,
                'best_time': 'Evening'
            }
        }
    
    def analyze_market_opportunity(self, topic: str, platform: str) -> Dict:
        """Analyze market opportunity for a topic on a platform"""
        opportunity = {
            'topic': topic,
            'platform': platform,
            'market_saturation': self._estimate_saturation(topic),
            'growth_potential': self._estimate_growth(topic),
            'audience_size': self._estimate_audience(topic, platform),
            'competitive_landscape': self._analyze_competition(topic),
            'recommended_angle': self._suggest_angle(topic),
            'benchmark_metrics': self.content_performance_benchmarks.get(platform, {})
        }
        return opportunity
    
    def _estimate_saturation(self, topic: str) -> float:
        """Estimate market saturation (0-100)"""
        # Simple estimation based on common topics
        saturated_topics = ['ai', 'marketing', 'business', 'social media', 'startup']
        emerging_topics = ['web3', 'metaverse', 'blockchain', 'nft']
        
        if any(t in topic.lower() for t in saturated_topics):
            return 75
        elif any(t in topic.lower() for t in emerging_topics):
            return 40
        else:
            return 50
    
    def _estimate_growth(self, topic: str) -> float:
        """Estimate growth potential (0-100)"""
        growth_topics = ['ai', 'automation', 'sustainability', 'web3']
        stable_topics = ['marketing', 'business', 'productivity']
        
        if any(t in topic.lower() for t in growth_topics):
            return 85
        elif any(t in topic.lower() for t in stable_topics):
            return 60
        else:
            return 50
    
    def _estimate_audience(self, topic: str, platform: str) -> Dict:
        """Estimate potential audience"""
        platform_audiences = {
            'twitter': 300000000,
            'instagram': 2000000000,
            'linkedin': 900000000,
            'facebook': 3000000000,
            'tiktok': 1500000000
        }
        
        base_audience = platform_audiences.get(platform, 1000000000)
        
        # Estimate based on topic specificity
        niche_topics = ['quantum computing', 'blockchain', 'robotics']
        mainstream_topics = ['ai', 'marketing', 'productivity']
        
        if any(t in topic.lower() for t in niche_topics):
            reach_percentage = 0.05
        elif any(t in topic.lower() for t in mainstream_topics):
            reach_percentage = 0.20
        else:
            reach_percentage = 0.10
        
        return {
            'platform_total': base_audience,
            'estimated_reach': int(base_audience * reach_percentage),
            'reach_percentage': reach_percentage * 100
        }
    
    def _analyze_competition(self, topic: str) -> Dict:
        """Analyze competitive landscape"""
        return {
            'competition_level': 'High',  # Would be based on real data
            'opportunities': [
                'Niche down to specific audience',
                'Focus on unique angle',
                'Create unique value proposition'
            ],
            'barriers_to_entry': 'Moderate',
            'profit_potential': 'High'
        }
    
    def _suggest_angle(self, topic: str) -> str:
        """Suggest unique angle for topic"""
        angles = [
            'Focus on the untold story',
            'Take a contrarian view',
            'Deep dive into specifics',
            'Combine with unexpected topic',
            'Focus on emerging application'
        ]
        
        # Would use more sophisticated logic
        return angles[hash(topic) % len(angles)]
    
    def get_content_calendar_insights(self, platform: str) -> Dict:
        """Get insights for content calendar planning"""
        benchmark = self.content_performance_benchmarks.get(platform, {})
        
        return {
            'platform': platform,
            'best_posting_time': benchmark.get('best_time', 'N/A'),
            'optimal_frequency': self._get_frequency(platform),
            'content_mix': self._get_content_mix(platform),
            'growth_strategy': self._get_growth_strategy(platform)
        }
    
    def _get_frequency(self, platform: str) -> str:
        """Recommended posting frequency"""
        frequency_guide = {
            'twitter': '3-5 times daily',
            'instagram': '1-2 times daily',
            'linkedin': '1 time daily',
            'facebook': '1-3 times daily',
            'tiktok': '1-3 times daily'
        }
        return frequency_guide.get(platform, 'Once daily')
    
    def _get_content_mix(self, platform: str) -> List[str]:
        """Recommended content mix for platform"""
        mix_guide = {
            'twitter': ['News/Updates (40%)', 'Engagement (30%)', 'Thought leadership (30%)'],
            'instagram': ['Visual stories (50%)', 'Behind-the-scenes (30%)', 'Educational (20%)'],
            'linkedin': ['Thought leadership (40%)', 'Company news (30%)', 'Industry insights (30%)'],
            'facebook': ['Community engagement (40%)', 'Promotional (30%)', 'Educational (30%)'],
            'tiktok': ['Entertainment (50%)', 'Educational (30%)', 'Promotional (20%)']
        }
        return mix_guide.get(platform, ['Content (33%)', 'Engagement (34%)', 'Promotion (33%)'])
    
    def _get_growth_strategy(self, platform: str) -> str:
        """Growth strategy for platform"""
        strategy_guide = {
            'twitter': 'Consistent engagement and thread creation',
            'instagram': 'Visual consistency and hashtag strategy',
            'linkedin': 'Thought leadership and networking',
            'facebook': 'Community building and engagement',
            'tiktok': 'Trend participation and authenticity'
        }
        return strategy_guide.get(platform, 'Consistency and quality')

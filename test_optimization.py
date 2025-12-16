#!/usr/bin/env python3
"""
Test script for Omneky + Madgicx optimization features
Demonstrates creative optimization and campaign prediction
"""

from social_media_generator import (
    SocialMediaGenerator, 
    CreativeOptimizer, 
    CampaignAnalyzer,
    TrendAnalyzer
)
import json
from datetime import datetime

def test_omneky_optimization():
    """Test Omneky creative optimization"""
    print("\n" + "="*70)
    print("🎯 TESTING OMNEKY CREATIVE OPTIMIZATION")
    print("="*70)
    
    optimizer = CreativeOptimizer()
    
    # Test different content examples
    test_content = {
        'weak_hook': "Check out our new product. It's pretty good.",
        'strong_hook': "Discover the shocking AI breakthrough that's transforming marketing forever. This changes everything.",
        'emotional_appeal': "Transform your business with our revolutionary platform. Success has never been easier.",
        'weak_cta': "Let us know what you think about this.",
        'strong_cta': "Click here NOW to grab exclusive access before it's gone!"
    }
    
    for content_type, content in test_content.items():
        print(f"\n📌 Testing: {content_type}")
        print(f"Content: {content}")
        
        optimization = optimizer.optimize_creative(content, 'instagram')
        print(f"\nOptimization Scores:")
        print(f"  ✓ Hook Strength: {optimization['hook_strength']:.0f}/100")
        print(f"  ✓ Emotional Appeal: {optimization['emotional_appeal']:.0f}/100")
        print(f"  ✓ Clarity: {optimization['clarity_score']:.0f}/100")
        print(f"  ✓ CTA Effectiveness: {optimization['cta_effectiveness']:.0f}/100")
        print(f"  ✓ Platform Fit: {optimization['platform_fit']:.0f}/100")
        print(f"  🎯 OVERALL SCORE: {optimization['overall_score']:.0f}/100")


def test_madgicx_campaign_prediction():
    """Test Madgicx campaign performance prediction"""
    print("\n" + "="*70)
    print("📊 TESTING MADGICX CAMPAIGN PREDICTION")
    print("="*70)
    
    analyzer = CampaignAnalyzer()
    
    # Sample content with optimization scores
    content_examples = {
        'high_quality': {
            'platform': 'instagram',
            'topic': 'AI marketing tools',
            'tone': 'professional',
            'content': 'Discover the AI revolution transforming marketing. Get instant access.',
            'optimization_score': 85,
            'trend_aware': True,
            'context': {'is_weekend': False}
        },
        'medium_quality': {
            'platform': 'facebook',
            'topic': 'Digital transformation',
            'tone': 'professional',
            'content': 'Learn about digital transformation strategies.',
            'optimization_score': 65,
            'trend_aware': True,
            'context': {'is_weekend': True}
        },
        'low_quality': {
            'platform': 'twitter',
            'topic': 'Web3',
            'tone': 'casual',
            'content': 'Web3 is cool',
            'optimization_score': 45,
            'trend_aware': False,
            'context': {'is_weekend': False}
        }
    }
    
    audience = {
        'audience_size': 500000,
        'interest_match': 80,
        'preferred_tone': 'professional',
        'saturation': 0.3
    }
    
    for content_type, content in content_examples.items():
        print(f"\n📌 Analyzing: {content_type}")
        print(f"Quality Score: {content['optimization_score']}/100")
        
        prediction = analyzer.predict_performance(content, audience)
        
        print(f"\nCampaign Prediction:")
        print(f"  📈 Estimated CTR: {prediction['estimated_ctr']:.2f}%")
        print(f"  💰 Estimated CPC: ${prediction['estimated_cpc']:.2f}")
        print(f"  ⭐ Quality Score: {prediction['quality_score']:.0f}/100")
        print(f"  👥 Audience Alignment: {prediction['audience_alignment']:.0f}%")
        
        scaling = prediction['scaling_potential']
        print(f"\nScaling Analysis:")
        print(f"  🚀 Status: {scaling['status']}")
        print(f"  📊 Budget Multiplier: {scaling['budget_multiplier']}x")
        
        print(f"\nRecommendations:")
        for rec in prediction['recommendations']:
            print(f"  💡 {rec}")


def test_trend_analysis():
    """Test trend-aware context generation"""
    print("\n" + "="*70)
    print("📈 TESTING TREND-AWARE CONTEXT")
    print("="*70)
    
    analyzer = TrendAnalyzer()
    context = analyzer.get_current_context()
    
    print("\nCurrent Context:")
    print(f"  📅 Date: {context['current_date']}")
    print(f"  🗓️ Month: {context['month']}")
    print(f"  📆 Day: {context['day_of_week']}")
    print(f"  ❄️ Season: {context['season']}")
    print(f"  🏃 Weekend: {'Yes' if context['is_weekend'] else 'No'}")
    print(f"  ⏰ Hour: {context['hour']}:00")


def test_hashtag_strategies():
    """Test different hashtag strategies"""
    print("\n" + "="*70)
    print("#️⃣ TESTING HASHTAG STRATEGIES")
    print("="*70)
    
    generator = SocialMediaGenerator()
    
    platforms = ['twitter', 'instagram', 'linkedin']
    strategies = ['trending', 'niche', 'balanced']
    
    for platform in platforms:
        print(f"\n📱 {platform.upper()}:")
        for strategy in strategies:
            instruction = generator._get_hashtag_instruction(platform, strategy)
            print(f"  {strategy.capitalize()}: {instruction}")


def test_industry_trends():
    """Test industry-specific trending topics"""
    print("\n" + "="*70)
    print("🏭 TESTING INDUSTRY TRENDS")
    print("="*70)
    
    generator = SocialMediaGenerator()
    
    industries = ['technology', 'marketing', 'business', 'finance']
    
    for industry in industries:
        print(f"\n🎯 {industry.upper()}:")
        suggestions = generator.get_trending_suggestions(industry)
        for i, suggestion in enumerate(suggestions[:5], 1):
            print(f"  {i}. {suggestion}")


def create_sample_report():
    """Create a sample optimization report"""
    print("\n" + "="*70)
    print("📋 SAMPLE OPTIMIZATION REPORT")
    print("="*70)
    
    generator = SocialMediaGenerator()
    
    # Simulate generating posts
    print("\nGenerating sample posts with optimization...")
    
    # Create dummy posts with optimization data
    sample_posts = [
        {
            'platform': 'instagram',
            'topic': 'AI Marketing Tools',
            'content': 'Discover the AI breakthrough transforming social media marketing. Limited access available!',
            'optimization_score': 87,
            'optimization_details': {
                'hook_strength': 90,
                'emotional_appeal': 85,
                'clarity_score': 85,
                'cta_effectiveness': 90,
                'platform_fit': 85,
                'overall_score': 87
            }
        },
        {
            'platform': 'linkedin',
            'topic': 'Digital Transformation',
            'content': 'Digital transformation is reshaping enterprise strategy. Learn how leaders are adapting.',
            'optimization_score': 72,
            'optimization_details': {
                'hook_strength': 70,
                'emotional_appeal': 70,
                'clarity_score': 75,
                'cta_effectiveness': 70,
                'platform_fit': 75,
                'overall_score': 72
            }
        }
    ]
    
    print("\n✅ Generated Posts Summary:")
    print(f"  Total Posts: {len(sample_posts)}")
    avg_score = sum(p['optimization_score'] for p in sample_posts) / len(sample_posts)
    print(f"  Average Optimization Score: {avg_score:.0f}/100")
    
    print("\n📊 Detailed Analysis:")
    for i, post in enumerate(sample_posts, 1):
        print(f"\n  Post {i}: {post['topic']}")
        print(f"    Platform: {post['platform']}")
        print(f"    Overall Score: {post['optimization_score']:.0f}/100")
        details = post['optimization_details']
        print(f"    Hook Strength: {details['hook_strength']:.0f}/100")
        print(f"    Emotional Appeal: {details['emotional_appeal']:.0f}/100")
        print(f"    Clarity: {details['clarity_score']:.0f}/100")


if __name__ == "__main__":
    print("\n" + "🚀 "*35)
    print("OMNEKY + MADGICX OPTIMIZATION TEST SUITE")
    print("🚀 "*35)
    
    try:
        test_omneky_optimization()
        test_madgicx_campaign_prediction()
        test_trend_analysis()
        test_hashtag_strategies()
        test_industry_trends()
        create_sample_report()
        
        print("\n" + "="*70)
        print("✅ ALL TESTS COMPLETED SUCCESSFULLY!")
        print("="*70)
        print("\n📚 Next Steps:")
        print("  1. Run the Streamlit app: streamlit run app.py")
        print("  2. Start Ollama: ollama serve")
        print("  3. Generate optimized content with real performance predictions!")
        print("\n")
        
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback
        traceback.print_exc()

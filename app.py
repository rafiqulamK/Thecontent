import streamlit as st
import ollama
import json
import os
from datetime import datetime, timedelta
from social_media_generator import SocialMediaGenerator
from copywriting_engine import CopywritingEngine, ABTestFramework
from market_intelligence import CompetitorAnalysis, MarketIntelligence
from content_calendar import ContentCalendar, ContentScheduler
from analytics_dashboard import PerformanceAnalytics, CompetitiveIntelligence
from madgicx_advanced import MetaAdsOptimizer, AudienceIntelligence, PerformanceOptimization
from campaign_management import CampaignDashboard, MultiCampaignManager
from copywriting_engine import PlagiarismDetector, ToneDetector, ReadabilityAnalyzer, ContentTemplates
from lexi_advanced_features import EngagementScorer, BrandVoiceConsistency, GrammarChecker
from omneky_advanced_features import MultiVariateTestingFramework, CreativeVariationGenerator, PerformanceBenchmarking, CreativeFatigueDetector

# Page configuration
st.set_page_config(
    page_title="AI Content Generator Pro",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better UI
st.markdown("""
    <style>
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .score-good {
        color: #00b050;
        font-weight: bold;
    }
    .score-medium {
        color: #ffc000;
        font-weight: bold;
    }
    .score-poor {
        color: #e74c3c;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'generator' not in st.session_state:
    st.session_state.generator = SocialMediaGenerator()

if 'copywriting_engine' not in st.session_state:
    st.session_state.copywriting_engine = CopywritingEngine()

if 'ab_framework' not in st.session_state:
    st.session_state.ab_framework = ABTestFramework()

if 'competitor_analysis' not in st.session_state:
    st.session_state.competitor_analysis = CompetitorAnalysis()

if 'market_intel' not in st.session_state:
    st.session_state.market_intel = MarketIntelligence()

if 'content_calendar' not in st.session_state:
    st.session_state.content_calendar = ContentCalendar()

if 'content_scheduler' not in st.session_state:
    st.session_state.content_scheduler = ContentScheduler()

if 'analytics' not in st.session_state:
    st.session_state.analytics = PerformanceAnalytics()

if 'competitive_intel' not in st.session_state:
    st.session_state.competitive_intel = CompetitiveIntelligence()

if 'meta_ads_optimizer' not in st.session_state:
    st.session_state.meta_ads_optimizer = MetaAdsOptimizer()

if 'audience_intel' not in st.session_state:
    st.session_state.audience_intel = AudienceIntelligence()

if 'performance_optimization' not in st.session_state:
    st.session_state.performance_optimization = PerformanceOptimization()

if 'campaign_dashboard' not in st.session_state:
    st.session_state.campaign_dashboard = CampaignDashboard()

if 'multi_campaign_manager' not in st.session_state:
    st.session_state.multi_campaign_manager = MultiCampaignManager()

if 'generated_posts' not in st.session_state:
    st.session_state.generated_posts = []

if 'saved_posts' not in st.session_state:
    st.session_state.saved_posts = []
if 'plagiarism_detector' not in st.session_state:
    st.session_state.plagiarism_detector = PlagiarismDetector()

if 'tone_detector' not in st.session_state:
    st.session_state.tone_detector = ToneDetector()

if 'readability_analyzer' not in st.session_state:
    st.session_state.readability_analyzer = ReadabilityAnalyzer()

if 'content_templates' not in st.session_state:
    st.session_state.content_templates = ContentTemplates()

if 'engagement_scorer' not in st.session_state:
    st.session_state.engagement_scorer = EngagementScorer()

if 'brand_voice' not in st.session_state:
    st.session_state.brand_voice = BrandVoiceConsistency()

if 'grammar_checker' not in st.session_state:
    st.session_state.grammar_checker = GrammarChecker()

if 'multivariate_testing' not in st.session_state:
    st.session_state.multivariate_testing = MultiVariateTestingFramework()

if 'creative_variation_gen' not in st.session_state:
    st.session_state.creative_variation_gen = CreativeVariationGenerator()

if 'performance_benchmarking' not in st.session_state:
    st.session_state.performance_benchmarking = PerformanceBenchmarking()

if 'fatigue_detector' not in st.session_state:
    st.session_state.fatigue_detector = CreativeFatigueDetector()

st.title("🤖 AI Content Generator Pro")
st.markdown("**Complete Alternative to Omneky, Madgicx & Lexi AI**")
st.markdown("Generate, optimize, and schedule content with competitive intelligence")

# Main navigation tabs
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10 = st.tabs([
    "🎯 Content Generator",
    "✍️ Copywriting Assistant",
    "🧪 A/B Testing Lab",
    "📅 Content Calendar",
    "📊 Analytics Dashboard",
    "🎯 Competitor Analysis",
    "📱 Meta Ads Optimizer",
    "🚀 Campaign Manager",
    "🔍 Lexi AI Advanced",
    "🔬 Omneky Multivariate"
])

# ==================== TAB 1: CONTENT GENERATOR ====================
with tab1:
    st.header("Content Generation Engine (Omneky + Madgicx)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("⚙️ Configuration")
        
        model = st.selectbox(
            "Choose Model",
            ["gemma:2b", "mistral", "llama2", "phi"],
            help="Select which LLM to use"
        )
        
        platform = st.selectbox(
            "Platform",
            ["Twitter", "LinkedIn", "Instagram", "Facebook", "TikTok"],
            help="Target social media platform"
        )
        
        tone = st.select_slider(
            "Tone",
            options=["Casual", "Professional", "Funny", "Inspirational", "Urgent"],
            value="Professional"
        )
        
        temperature = st.slider(
            "Creativity",
            min_value=0.0,
            max_value=1.0,
            value=0.7,
            step=0.1
        )
        
        hashtag_strategy = st.selectbox(
            "Hashtag Strategy",
            ["Trending", "Niche", "Balanced", "Minimal"],
            help="How aggressive should hashtag usage be?"
        )
        
        audience = st.text_input(
            "Target Audience",
            value="Tech professionals",
            help="Who is this content for?"
        )
    
    with col2:
        st.subheader("📝 Content Input")
        
        topic = st.text_area(
            "Content Topic",
            height=100,
            placeholder="Enter your topic, idea, or content outline...",
            help="What do you want to create content about?"
        )
        
        keywords = st.text_input(
            "Keywords (comma-separated)",
            placeholder="keyword1, keyword2, keyword3",
            help="Include relevant keywords for better optimization"
        )
        
        max_posts = st.number_input(
            "Number of Variations",
            min_value=1,
            max_value=5,
            value=1,
            help="Generate multiple variations of the same content"
        )
    
    # Generate button
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        generate_btn = st.button("🚀 Generate Content", use_container_width=True)
    
    if generate_btn and topic:
        with st.spinner("🎨 Generating optimized content..."):
            try:
                # Generate content
                posts = []
                for i in range(max_posts):
                    post = st.session_state.generator.generate_post(
                        topic=topic,
                        platform=platform,
                        tone=tone,
                        model=model,
                        temperature=temperature,
                        keywords=keywords
                    )
                    
                    if post:
                        # Add metadata
                        post['id'] = len(st.session_state.generated_posts) + i
                        post['generated_at'] = datetime.now().isoformat()
                        post['platform'] = platform
                        post['tone'] = tone
                        post['audience'] = audience
                        posts.append(post)
                
                if posts:
                    st.session_state.generated_posts.extend(posts)
                    st.success(f"✅ Generated {len(posts)} post(s)")
                    
                    # Display results
                    for idx, post in enumerate(posts):
                        with st.expander(f"📄 Post {idx + 1}", expanded=(idx == 0)):
                            # Content
                            st.subheader("Generated Content")
                            st.info(post['content'])
                            
                            # Omneky Optimization Scores
                            st.subheader("🎯 Creative Optimization (Omneky)")
                            if 'optimization' in post:
                                opt = post['optimization']
                                cols = st.columns(5)
                                
                                metrics = [
                                    ('Hook', opt.get('hook_score', 0)),
                                    ('Emotion', opt.get('emotion_score', 0)),
                                    ('Clarity', opt.get('clarity_score', 0)),
                                    ('CTA', opt.get('cta_score', 0)),
                                    ('Platform', opt.get('platform_fit_score', 0))
                                ]
                                
                                for col, (label, score) in zip(cols, metrics):
                                    with col:
                                        st.metric(label, f"{score:.0f}/100")
                            
                            # Madgicx Predictions
                            st.subheader("📊 Performance Prediction (Madgicx)")
                            if 'campaign_analysis' in post:
                                analysis = post['campaign_analysis']
                                pred_cols = st.columns(3)
                                
                                with pred_cols[0]:
                                    st.metric("Est. CTR", f"{analysis.get('ctr_prediction', 0):.2f}%")
                                
                                with pred_cols[1]:
                                    st.metric("Quality Score", f"{analysis.get('quality_score', 0):.0f}/100")
                                
                                with pred_cols[2]:
                                    st.metric("Alignment", f"{analysis.get('audience_alignment', 0):.0f}%")
                            
                            # Action buttons
                            action_cols = st.columns(4)
                            with action_cols[0]:
                                if st.button("📋 Copy", key=f"copy_{idx}"):
                                    st.write(f"```\n{post['content']}\n```")
                                    st.success("Copied to clipboard!")
                            
                            with action_cols[1]:
                                if st.button("💾 Save", key=f"save_{idx}"):
                                    st.session_state.saved_posts.append(post)
                                    st.success("✅ Saved!")
                            
                            with action_cols[2]:
                                if st.button("📅 Schedule", key=f"schedule_{idx}"):
                                    st.info("✨ Scheduling feature coming soon!")
                            
                            with action_cols[3]:
                                if st.button("✨ Improve", key=f"improve_{idx}"):
                                    st.info("✨ Click 'Copywriting Assistant' tab for improvements")
            
            except Exception as e:
                st.error(f"❌ Error generating content: {str(e)}")
    
    # Recent posts summary
    if st.session_state.generated_posts:
        st.divider()
        st.subheader("📈 Session Summary")
        
        summary_cols = st.columns(4)
        with summary_cols[0]:
            st.metric("Posts Generated", len(st.session_state.generated_posts))
        with summary_cols[1]:
            st.metric("Saved Posts", len(st.session_state.saved_posts))
        with summary_cols[2]:
            avg_score = sum([
                p.get('optimization', {}).get('overall_score', 0)
                for p in st.session_state.generated_posts
            ]) / max(len(st.session_state.generated_posts), 1)
            st.metric("Avg Optimization", f"{avg_score:.0f}/100")
        with summary_cols[3]:
            st.metric("Top Platform", platform)


# ==================== TAB 2: COPYWRITING ASSISTANT ====================
with tab2:
    st.header("Copywriting Assistant (Lexi AI Alternative)")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("📝 Your Content")
        original_content = st.text_area(
            "Paste content to improve",
            height=200,
            placeholder="Paste your social media content here..."
        )
        
        writing_style = st.selectbox(
            "Desired Writing Style",
            ["Persuasive", "Narrative", "Technical", "Conversational", "Urgent"],
            help="Choose the writing style to apply"
        )
        
        improve_btn = st.button("✨ Improve Content")
    
    with col2:
        st.subheader("🎯 Improvement Options")
        
        improvement_type = st.multiselect(
            "What to improve",
            ["Power Words", "Readability", "Engagement", "CTAs", "Variations"],
            default=["Power Words", "Engagement", "CTAs"]
        )
        
        if improve_btn and original_content:
            with st.spinner("🔄 Analyzing and improving..."):
                improvements = st.session_state.copywriting_engine.improve_content(
                    original_content,
                    style=writing_style.lower()
                )
                
                st.success("✅ Content analyzed!")
                
                # Display improvements
                improvement_cols = st.columns(2)
                
                with improvement_cols[0]:
                    st.subheader("📊 Content Scores")
                    st.metric("Readability", f"{improvements['readability_score']:.1f}/10")
                    st.metric("Engagement", f"{improvements['engagement_score']:.1f}/10")
                
                with improvement_cols[1]:
                    st.subheader("🎯 Suggestions")
                    for suggestion in improvements.get('improvements', [])[:3]:
                        st.info(f"💡 {suggestion}")
                
                # Power words
                if "Power Words" in improvement_type:
                    st.subheader("⚡ Power Word Suggestions")
                    power_words = improvements.get('power_word_suggestions', [])
                    if power_words:
                        st.write("Replace generic words with these power words:")
                        for word in power_words[:5]:
                            st.write(f"• **{word}**")
                
                # CTA variations
                if "CTAs" in improvement_type:
                    st.subheader("🎬 CTA Variations")
                    cta_suggestions = improvements.get('cta_suggestions', [])
                    if cta_suggestions:
                        for i, cta in enumerate(cta_suggestions[:3]):
                            st.info(f"Option {i+1}: {cta}")
                
                # Rewritten versions
                if "Variations" in improvement_type:
                    st.subheader("📝 Rewritten Versions")
                    for i, version in enumerate(improvements.get('rewritten_versions', [])[:2]):
                        st.write(f"**Version {i+1}:**")
                        st.info(version)


# ==================== TAB 3: A/B TESTING LAB ====================
with tab3:
    st.header("A/B Testing Framework")
    
    st.subheader("🧪 Compare Content Variants")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        test_name = st.text_input("Test Name", value="Content Test")
    
    with col2:
        variant_count = st.number_input("Number of Variants", 2, 5, 2)
    
    # Input variants
    variants = []
    st.subheader("Enter Your Variants")
    
    for i in range(variant_count):
        variant_content = st.text_area(
            f"Variant {i+1}",
            key=f"variant_{i}",
            height=100,
            placeholder="Enter variant content..."
        )
        if variant_content:
            variants.append({
                'id': f'variant_{i+1}',
                'name': f'Variant {i+1}',
                'content': variant_content
            })
    
    if st.button("🔍 Analyze Variants"):
        if variants:
            with st.spinner("📊 Analyzing variants..."):
                # Analyze each variant
                st.subheader("📈 Variant Analysis")
                
                analysis_results = []
                for variant in variants:
                    analysis = st.session_state.ab_framework.analyze_variant(
                        variant,
                        audience={'type': 'general', 'size': 10000}
                    )
                    analysis_results.append(analysis)
                
                # Display comparison
                comparison_cols = st.columns(len(variants))
                
                for col, result in zip(comparison_cols, analysis_results):
                    with col:
                        st.write(f"### {result['variant_id']}")
                        st.metric("CTR", f"{result['metrics'].get('ctr', 0):.2f}%")
                        st.metric("Engagement", f"{result['metrics'].get('engagement', 0):.2f}%")
                        st.metric("Quality", f"{result['metrics'].get('quality_score', 0):.0f}/100")
                
                # Winner recommendation
                st.divider()
                st.subheader("🏆 Recommendation")
                
                best_variant = max(analysis_results, key=lambda x: x['metrics'].get('ctr', 0))
                st.success(f"**Winner: {best_variant['variant_id']}** - Predicted {best_variant['metrics'].get('ctr', 0):.2f}% CTR")
                
                # Strengths and weaknesses
                strengths_cols = st.columns(len(variants))
                for col, result in zip(strengths_cols, analysis_results):
                    with col:
                        st.write(f"**{result['variant_id']} Strengths:**")
                        for strength in result.get('strengths', [])[:2]:
                            st.write(f"✅ {strength}")


# ==================== TAB 4: CONTENT CALENDAR ====================
with tab4:
    st.header("📅 Content Calendar & Scheduling")
    
    st.subheader("Plan Your Content Strategy")
    
    col1, col2 = st.columns(2)
    
    with col1:
        calendar_platform = st.selectbox(
            "Select Platform",
            ["All", "Twitter", "LinkedIn", "Instagram", "Facebook", "TikTok"]
        )
        
        calendar_theme = st.selectbox(
            "Weekly Theme",
            ["Motivation Monday", "Tips Tuesday", "Wisdom Wednesday", "Throwback Thursday"]
        )
    
    with col2:
        weeks_ahead = st.number_input("Plan weeks ahead", 1, 12, 1)
        view_type = st.selectbox(
            "View Type",
            ["Weekly", "Monthly", "List"]
        )
    
    if st.button("📋 Generate Calendar"):
        # Create sample topics
        sample_topics = [
            "Industry trends and insights",
            "How-to guides and tutorials",
            "Team spotlights and stories",
            "Product updates and features",
            "Customer success stories",
            "Behind-the-scenes content",
            "Thought leadership pieces"
        ]
        
        # Plan weekly content
        with st.spinner("📅 Planning content..."):
            weekly_plan = st.session_state.content_calendar.plan_weekly_content(
                calendar_platform if calendar_platform != "All" else "Twitter",
                calendar_theme,
                sample_topics[:5],
                {
                    'monday': '9:00 AM',
                    'tuesday': '9:00 AM',
                    'wednesday': '9:00 AM',
                    'thursday': '9:00 AM',
                    'friday': '9:00 AM'
                }
            )
            
            st.success(f"✅ Planned {len(weekly_plan)} posts")
            
            # Display calendar
            for post in weekly_plan:
                with st.expander(f"{post['day']} - {post['topic']}", expanded=False):
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        st.write(f"**Date:** {post['date']}")
                        st.write(f"**Time:** {post['posting_time']}")
                    
                    with col2:
                        st.write(f"**Type:** {post['content_type']}")
                        st.write(f"**Platform:** {post['platform']}")
                    
                    with col3:
                        st.write(f"**Est. Reach:** {post['estimated_reach']} users")
                        st.write(f"**Status:** {post['status']}")


# ==================== TAB 5: ANALYTICS DASHBOARD ====================
with tab5:
    st.header("📊 Analytics Dashboard")
    
    st.subheader("Performance Tracking & Insights")
    
    col1, col2 = st.columns(2)
    
    with col1:
        analytics_period = st.selectbox(
            "Time Period",
            ["Last 7 days", "Last 30 days", "Last 90 days", "All time"]
        )
        
        analytics_metric = st.multiselect(
            "Metrics to Display",
            ["Engagement Rate", "Reach", "CTR", "Performance Score", "Top Performers"],
            default=["Engagement Rate", "Top Performers"]
        )
    
    with col2:
        platform_filter = st.multiselect(
            "Platforms",
            ["Twitter", "LinkedIn", "Instagram", "Facebook", "TikTok"],
            default=["Twitter", "LinkedIn"]
        )
    
    if st.button("📈 Load Analytics"):
        st.info("📊 Sample Analytics Dashboard")
        
        # Summary metrics
        st.subheader("Key Metrics")
        summary_cols = st.columns(4)
        
        with summary_cols[0]:
            st.metric("Total Posts", 42)
        
        with summary_cols[1]:
            st.metric("Avg Engagement", "3.2%", "↑ 0.5%")
        
        with summary_cols[2]:
            st.metric("Total Reach", "125.4K", "↑ 15%")
        
        with summary_cols[3]:
            st.metric("Trending Topics", 5)
        
        # Platform breakdown
        st.subheader("Performance by Platform")
        
        platform_data = {
            'Platform': ['Twitter', 'LinkedIn', 'Instagram', 'Facebook', 'TikTok'],
            'Posts': [8, 10, 7, 9, 8],
            'Avg Engagement': [2.1, 4.5, 5.2, 3.8, 8.1],
            'Total Reach': [25000, 35000, 28000, 22000, 15000]
        }
        
        platform_cols = st.columns(5)
        for i, platform in enumerate(platform_data['Platform']):
            with platform_cols[i]:
                st.metric(
                    platform,
                    f"{platform_data['Avg Engagement'][i]}%",
                    f"{platform_data['Posts'][i]} posts"
                )
        
        # Top performers
        st.subheader("🏆 Top Performing Content")
        
        top_posts = [
            {"platform": "LinkedIn", "engagement": 8.5, "reach": 15000},
            {"platform": "Instagram", "engagement": 7.2, "reach": 12000},
            {"platform": "TikTok", "engagement": 6.8, "reach": 10000}
        ]
        
        for i, post in enumerate(top_posts):
            st.info(f"{i+1}. {post['platform']}: {post['engagement']}% engagement, {post['reach']:,} reach")


# ==================== TAB 6: COMPETITOR ANALYSIS ====================
with tab6:
    st.header("🎯 Competitor Analysis")
    
    st.subheader("Market Intelligence & Positioning")
    
    col1, col2 = st.columns(2)
    
    with col1:
        competitor_name = st.text_input(
            "Competitor Name",
            placeholder="e.g., Brand X, Competitor Y"
        )
        
        your_content = st.text_area(
            "Your Content",
            height=150,
            placeholder="Paste your content..."
        )
    
    with col2:
        competitor_content = st.text_area(
            "Competitor's Content",
            height=150,
            placeholder="Paste competitor's content..."
        )
    
    if st.button("🔍 Analyze Competition"):
        if competitor_name and your_content and competitor_content:
            with st.spinner("🔎 Analyzing..."):
                analysis = st.session_state.competitor_analysis.analyze_competitor_content(
                    competitor_name,
                    competitor_content,
                    your_content
                )
                
                st.success("✅ Analysis complete!")
                
                # Positioning
                st.subheader("📊 Market Position")
                st.info(f"**Status:** {analysis['positioning']}")
                
                # Competitive advantage
                col1, col2 = st.columns(2)
                
                with col1:
                    st.subheader("✅ Your Advantages")
                    for adv in analysis['competitive_advantage']:
                        st.write(f"• {adv}")
                
                with col2:
                    st.subheader("⚠️ Gaps to Address")
                    for gap in analysis['gaps']:
                        st.write(f"• {gap}")
                
                # Recommendations
                st.subheader("💡 Recommendations")
                for i, rec in enumerate(analysis['recommendations'], 1):
                    st.info(f"{i}. {rec}")
    
    # Market opportunity analyzer
    st.divider()
    st.subheader("📈 Market Opportunity Analysis")
    
    opportunity_topic = st.text_input("Topic to analyze", placeholder="e.g., AI, Marketing, Startups")
    opportunity_platform = st.selectbox("Platform", ["Twitter", "LinkedIn", "Instagram", "Facebook", "TikTok"])
    
    if st.button("🎯 Analyze Opportunity"):
        if opportunity_topic:
            opportunity = st.session_state.market_intel.analyze_market_opportunity(
                opportunity_topic,
                opportunity_platform
            )
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                saturation = opportunity['market_saturation']
                st.metric(
                    "Market Saturation",
                    f"{saturation:.0f}%",
                    "🔴 High" if saturation > 70 else "🟡 Medium" if saturation > 40 else "🟢 Low"
                )
            
            with col2:
                growth = opportunity['growth_potential']
                st.metric("Growth Potential", f"{growth:.0f}%")
            
            with col3:
                audience = opportunity['audience_size']['estimated_reach']
                st.metric("Est. Audience", f"{audience:,}")
            
            st.subheader("💡 Recommended Angle")
            st.info(opportunity['recommended_angle'])


# ==================== TAB 7: META ADS OPTIMIZER ====================
with tab7:
    st.header("📱 Meta Ads Optimizer (Madgicx Advanced)")
    
    st.subheader("Facebook & Instagram Campaign Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        campaign_id = st.text_input("Campaign ID", "FB_CAMP_12345")
        daily_budget = st.number_input("Daily Budget ($)", 100, 10000, 500)
    
    with col2:
        platform = st.selectbox("Platform", ["Facebook", "Instagram", "Both"])
        objective = st.selectbox("Campaign Objective", ["Conversions", "Leads", "Traffic", "Engagement"])
    
    # Sample campaign metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        impressions = st.number_input("Impressions", 50000, 5000000, 150000)
    
    with col2:
        clicks = st.number_input("Clicks", 1000, 100000, 3000)
    
    with col3:
        conversions = st.number_input("Conversions", 50, 10000, 150)
    
    with col4:
        spend = st.number_input("Total Spend ($)", 100, 100000, 2500)
    
    revenue = st.number_input("Total Revenue ($)", 100, 500000, 7500)
    target_cpa = st.number_input("Target CPA ($)", 1, 1000, 25)
    
    if st.button("🔍 Analyze Campaign"):
        with st.spinner("📊 Analyzing campaign..."):
            campaign_metrics = {
                'campaign_id': campaign_id,
                'impressions': impressions,
                'clicks': clicks,
                'conversions': conversions,
                'spend': spend,
                'revenue': revenue,
                'target_cpa': target_cpa,
                'daily_budget': daily_budget,
                'days_running': 14,
                'quality_score': 8,
                'frequency': 2.5
            }
            
            analysis = st.session_state.meta_ads_optimizer.analyze_facebook_campaign(
                campaign_id,
                campaign_metrics
            )
            
            # Display analysis
            st.success("✅ Campaign Analysis Complete")
            
            # Performance grade
            st.subheader("🎯 Campaign Performance")
            perf = analysis['performance_metrics']
            
            grade_col1, grade_col2, grade_col3, grade_col4 = st.columns(4)
            
            with grade_col1:
                st.metric("Performance Grade", analysis['health_score'])
            
            with grade_col2:
                st.metric("CTR", f"{perf['ctr']:.2f}%")
            
            with grade_col3:
                st.metric("CPC", f"${perf['cpc']:.2f}")
            
            with grade_col4:
                st.metric("ROAS", f"{perf['roas']:.2f}x")
            
            # Scaling recommendations
            st.subheader("🚀 Scaling Strategy")
            scaling = analysis['scaling_recommendations']
            st.info(f"**Status:** {scaling['scaling_status']}")
            
            scaling_cols = st.columns(2)
            with scaling_cols[0]:
                st.write("**Recommended Methods:**")
                for method in scaling['scaling_method'][:3]:
                    st.write(f"• {method}")
            
            with scaling_cols[1]:
                st.write("**Audience Expansion:**")
                expansion = scaling['audience_expansion']
                st.write(f"• Strategy: {expansion['strategy']}")
                st.write(f"• Expected Impact: {expansion['expected_impact']}")
            
            # Creative optimization
            st.subheader("🎨 Creative Performance")
            creative = analysis['creative_performance']
            
            if creative['creative_fatigue_detected']:
                st.warning("⚠️ Creative fatigue detected - Refresh ads soon")
            else:
                st.success("✅ Creative performing well")
            
            st.write("**Recommendations:**")
            for rec in creative['creative_recommendations']:
                st.write(f"• {rec}")
            
            # Budget optimization
            st.subheader("💰 Budget Optimization")
            budget = analysis['budget_efficiency']
            
            budget_col1, budget_col2, budget_col3 = st.columns(3)
            
            with budget_col1:
                st.metric("Spend Efficiency", f"{budget['spend_efficiency']:.1f}%")
            
            with budget_col2:
                st.metric("CPA vs Target", f"{budget['cpa_vs_target']['variance']:+.1f}%")
            
            with budget_col3:
                st.metric("Daily Pacing", f"{budget['daily_pacing']:.1f}x")
            
            st.write(f"**Recommendation:** {budget['budget_optimization']['recommendation']}")
            st.metric("Optimal Daily Budget", f"${budget['budget_optimization']['optimal_daily_budget']:.0f}")
            
            # Action items
            st.subheader("✅ Priority Actions")
            for action in analysis['action_items']:
                if action['priority'] == 'CRITICAL':
                    st.error(f"🔴 [{action['priority']}] {action['action']} - {action['timeframe']}")
                elif action['priority'] == 'HIGH':
                    st.warning(f"🟠 [{action['priority']}] {action['action']} - {action['timeframe']}")
                else:
                    st.info(f"🔵 [{action['priority']}] {action['action']} - {action['timeframe']}")
    
    # Audience intelligence
    st.divider()
    st.subheader("👥 Audience Intelligence")
    
    if st.button("🎯 Analyze Audience Segments"):
        segments = st.session_state.audience_intel.analyze_audience_segments(
            campaign_id,
            {'reach': 50000, 'conversions': 150}
        )
        
        st.write("**Audience Breakdown:**")
        
        seg_cols = st.columns(3)
        with seg_cols[0]:
            high_intent = segments['segments']['high_intent']
            st.metric("High Intent CPA", f"${high_intent['cpa_estimate']}")
            st.write(f"Budget: {high_intent['budget_allocation']}")
        
        with seg_cols[1]:
            mid_intent = segments['segments']['mid_intent']
            st.metric("Mid Intent CPA", f"${mid_intent['cpa_estimate']}")
            st.write(f"Budget: {mid_intent['budget_allocation']}")
        
        with seg_cols[2]:
            low_intent = segments['segments']['low_intent']
            st.metric("Low Intent CPA", f"${low_intent['cpa_estimate']}")
            st.write(f"Budget: {low_intent['budget_allocation']}")
        
        st.write("**Segment Recommendations:**")
        for rec in segments['recommendations']:
            st.info(f"💡 {rec}")
    
    # Performance optimization tips
    st.divider()
    st.subheader("💡 Optimization Tips")
    
    opt_tabs = st.tabs(["Copy", "Landing Page", "Audience", "Bidding", "Timing"])
    
    with opt_tabs[0]:
        st.write("**Ad Copy Optimization:**")
        tips = st.session_state.performance_optimization.get_optimization_recommendations({})
        for tip in tips['ad_copy_optimization']:
            st.write(f"• {tip}")
    
    with opt_tabs[1]:
        st.write("**Landing Page Optimization:**")
        tips = st.session_state.performance_optimization.get_optimization_recommendations({})
        for tip in tips['landing_page_optimization']:
            st.write(f"• {tip}")
    
    with opt_tabs[2]:
        st.write("**Audience Optimization:**")
        tips = st.session_state.performance_optimization.get_optimization_recommendations({})
        for tip in tips['audience_optimization']:
            st.write(f"• {tip}")
    
    with opt_tabs[3]:
        st.write("**Bidding Optimization:**")
        tips = st.session_state.performance_optimization.get_optimization_recommendations({})
        for tip in tips['bid_optimization']:
            st.write(f"• {tip}")
    
    with opt_tabs[4]:
        st.write("**Timing Optimization:**")
        tips = st.session_state.performance_optimization.get_optimization_recommendations({})
        for tip in tips['timing_optimization']:
            st.write(f"• {tip}")


# ==================== TAB 8: CAMPAIGN MANAGER ====================
with tab8:
    st.header("🚀 Multi-Campaign Manager")
    
    st.subheader("Manage & Optimize Multiple Campaigns Simultaneously")
    
    # Sample campaigns
    campaigns = [
        {
            'name': 'Campaign A - Q4 Sales',
            'status': 'Active',
            'spend': 5000,
            'revenue': 15000,
            'roas': 3.0,
            'conversions': 200,
            'cpa': 25,
            'days_running': 14
        },
        {
            'name': 'Campaign B - Lead Gen',
            'status': 'Active',
            'spend': 3000,
            'revenue': 6000,
            'roas': 2.0,
            'conversions': 120,
            'cpa': 25,
            'days_running': 10
        },
        {
            'name': 'Campaign C - Testing',
            'status': 'Optimizing',
            'spend': 1500,
            'revenue': 1200,
            'roas': 0.8,
            'conversions': 30,
            'cpa': 50,
            'days_running': 5
        },
        {
            'name': 'Campaign D - Retargeting',
            'status': 'Active',
            'spend': 2000,
            'revenue': 8000,
            'roas': 4.0,
            'conversions': 100,
            'cpa': 20,
            'days_running': 20
        }
    ]
    
    if st.button("📊 Analyze Campaign Portfolio"):
        with st.spinner("📈 Analyzing portfolio..."):
            portfolio = st.session_state.multi_campaign_manager.analyze_portfolio(campaigns)
            
            # Portfolio overview
            st.subheader("📈 Portfolio Overview")
            
            port_cols = st.columns(4)
            
            with port_cols[0]:
                st.metric("Total Campaigns", portfolio['total_campaigns'])
            
            with port_cols[1]:
                st.metric("Total Spend", f"${portfolio['total_spend']:,.0f}")
            
            with port_cols[2]:
                st.metric("Total Revenue", f"${portfolio['total_revenue']:,.0f}")
            
            with port_cols[3]:
                st.metric("Portfolio ROAS", f"{portfolio['portfolio_roas']:.2f}x")
            
            # Campaign status
            st.subheader("📊 Campaign Status")
            
            status_col1, status_col2, status_col3 = st.columns(3)
            
            with status_col1:
                st.write("**Active Campaigns:**")
                for camp in portfolio['campaigns_by_status']['active']:
                    st.write(f"✅ {camp}")
            
            with status_col2:
                st.write("**Optimizing:**")
                for camp in portfolio['campaigns_by_status']['optimizing']:
                    st.write(f"🔄 {camp}")
            
            with status_col3:
                st.write("**Portfolio Health:**")
                st.info(portfolio['overall_health'])
            
            # Top performers
            st.subheader("🏆 Top Performers")
            
            for i, performer in enumerate(portfolio['high_performers'][:3], 1):
                st.success(f"{i}. **{performer['name']}** - ROAS: {performer['roas']:.2f}x | Revenue: ${performer['revenue']:,.0f}")
            
            # Underperformers
            if portfolio['underperformers']:
                st.subheader("⚠️ Underperformers - Action Needed")
                
                for underperformer in portfolio['underperformers']:
                    st.error(f"❌ **{underperformer['name']}**")
                    st.write(f"   Issue: {underperformer['issue']}")
                    st.write(f"   Action: {underperformer['recommendation']}")
            
            # Budget reallocation
            st.subheader("💰 Budget Reallocation Recommendation")
            
            realloc = portfolio['budget_allocation_recommendations']
            st.info(f"**Recommendation:** {realloc['recommendation']}")
            st.write(f"**Expected Impact:** {realloc['expected_impact']}")
            
            realloc_cols = st.columns(2)
            with realloc_cols[0]:
                st.write("**Scale These Campaigns:**")
                for camp in realloc['top_performers_to_scale']:
                    st.write(f"📈 {camp}")
            
            with realloc_cols[1]:
                st.write("**Pause These Campaigns:**")
                for camp in realloc['underperformers_to_pause']:
                    st.write(f"⏸️ {camp}")
    
    # Individual campaign reports
    st.divider()
    st.subheader("📋 Individual Campaign Reports")
    
    selected_campaign = st.selectbox(
        "Select Campaign to Review",
        [c['name'] for c in campaigns]
    )
    
    if st.button("📄 Generate Campaign Report"):
        selected = next(c for c in campaigns if c['name'] == selected_campaign)
        
        with st.spinner("📝 Generating report..."):
            report = st.session_state.campaign_dashboard.create_campaign_report(selected)
            
            # Campaign summary
            summary = report['campaign_summary']
            st.subheader(f"Campaign: {summary['campaign_name']}")
            
            summary_cols = st.columns(4)
            with summary_cols[0]:
                st.metric("Status", summary['status'])
            with summary_cols[1]:
                st.metric("Duration", f"{summary['days_running']} days")
            with summary_cols[2]:
                st.metric("Spent", f"${summary['spent']:.0f}")
            with summary_cols[3]:
                st.metric("Budget %", f"{summary['spend_percentage']:.1f}%")
            
            # Performance metrics
            st.subheader("📊 Performance Metrics")
            
            perf = report['performance_overview']
            perf_cols = st.columns(5)
            
            with perf_cols[0]:
                st.metric("Impressions", f"{perf['impressions']:,}")
            with perf_cols[1]:
                st.metric("Clicks", f"{perf['clicks']:,}")
            with perf_cols[2]:
                st.metric("CTR", f"{perf['ctr']:.2f}%")
            with perf_cols[3]:
                st.metric("Conversions", f"{perf['conversions']:,}")
            with perf_cols[4]:
                st.metric("CPA", f"${perf['cpa']:.2f}")
            
            # ROI Analysis
            st.subheader("💰 ROI Analysis")
            
            roi = report['roi_analysis']
            roi_cols = st.columns(4)
            
            with roi_cols[0]:
                st.metric("Revenue", f"${roi['total_revenue']:,.0f}")
            with roi_cols[1]:
                st.metric("Profit", f"${roi['profit']:,.0f}")
            with roi_cols[2]:
                st.metric("ROAS", f"{roi['roas']:.2f}x")
            with roi_cols[3]:
                st.metric("Grade", roi['profitability_grade'])
            
            # Alerts
            if report['alerts']:
                st.subheader("🚨 Alerts")
                for alert in report['alerts']:
                    if alert['severity'] == 'HIGH':
                        st.error(f"**{alert['alert']}** → {alert['recommendation']}")
                    else:
                        st.warning(f"**{alert['alert']}** → {alert['recommendation']}")
            
            # Recommendations
            st.subheader("💡 Recommendations")
            for rec in report['recommendations'][:3]:
                st.success(f"**[{rec['priority']}]** {rec['recommendation']}")
                st.write(f"Action: {rec['action']}")


# ==================== FOOTER ====================

# ==================== TAB 9: LEXI AI ADVANCED FEATURES ====================
with tab9:
    st.header("🔍 Lexi AI Advanced Features")
    st.markdown("Plagiarism detection, tone analysis, readability scoring, and brand consistency")
    
    lexi_feature = st.selectbox(
        "Select Advanced Feature",
        ["Plagiarism Detection", "Tone Detection", "Readability Analysis", 
         "Content Templates", "Engagement Scoring", "Brand Voice Consistency", "Grammar Check"]
    )
    
    # Text input for analysis
    text_to_analyze = st.text_area("Enter content to analyze:", height=150)
    
    if st.button("Analyze Content", key="lexi_analyze"):
        if text_to_analyze.strip():
            if lexi_feature == "Plagiarism Detection":
                st.subheader("📋 Plagiarism Detection Results")
                result = st.session_state.plagiarism_detector.detect_plagiarism(text_to_analyze)
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Originality Score", f"{result['originality_score']:.1f}/100")
                with col2:
                    st.metric("Plagiarism Risk", result['plagiarism_risk'])
                with col3:
                    st.metric("Risk Level", f"{result['risk_score']:.1f}/100")
                
                st.warning(result['recommendation'])
                
                if result['issues_found']:
                    st.subheader("Issues Found:")
                    for issue in result['issues_found']:
                        st.write(f"• {issue}")
            
            elif lexi_feature == "Tone Detection":
                st.subheader("🎭 Tone Detection Results")
                tone_result = st.session_state.tone_detector.detect_tone(text_to_analyze)
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Detected Tone", tone_result['detected_tone'])
                with col2:
                    st.metric("Confidence", f"{tone_result['tone_confidence']*100:.1f}%")
                with col3:
                    st.metric("Description", tone_result['tone_description'])
                
                # Tone breakdown
                st.subheader("Tone Score Breakdown")
                tone_scores = tone_result['all_tones']
                cols = st.columns(len(tone_scores))
                for idx, (tone_type, score) in enumerate(tone_scores.items()):
                    with cols[idx]:
                        st.metric(tone_type.title(), f"{score:.1f}")
                
                # Adjust tone
                target_tone = st.selectbox("Adjust to tone:", ["professional", "casual", "friendly", "urgent", "empathetic"])
                if st.button("Adjust Tone"):
                    adjusted = st.session_state.tone_detector.adjust_tone(text_to_analyze, target_tone)
                    st.subheader(f"Adjusted to {target_tone}:")
                    st.text_area("Adjusted content:", value=adjusted, disabled=True)
            
            elif lexi_feature == "Readability Analysis":
                st.subheader("📖 Readability Analysis")
                readability = st.session_state.readability_analyzer.analyze_readability(text_to_analyze)
                
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.metric("Word Count", readability['word_count'])
                with col2:
                    st.metric("Flesch Reading Ease", f"{readability['flesch_reading_ease']:.1f}")
                with col3:
                    st.metric("Grade Level", f"{readability['flesch_kincaid_grade']:.1f}")
                with col4:
                    st.metric("Readability Score", readability['readability_score'])
                
                st.info(f"**Level:** {readability['readability_level']}")
                
                st.subheader("📊 Reading Metrics")
                metrics_cols = st.columns(3)
                with metrics_cols[0]:
                    st.metric("Sentence Count", readability['sentence_count'])
                with metrics_cols[1]:
                    st.metric("Avg Words/Sentence", readability['avg_words_per_sentence'])
                with metrics_cols[2]:
                    st.metric("Avg Syllables/Word", readability['avg_syllables_per_word'])
                
                if readability['improvement_suggestions']:
                    st.subheader("💡 Improvement Suggestions")
                    for suggestion in readability['improvement_suggestions']:
                        st.write(f"• {suggestion}")
            
            elif lexi_feature == "Content Templates":
                st.subheader("📝 Content Templates")
                templates = st.session_state.content_templates.list_templates()
                selected_template = st.selectbox("Choose template:", templates)
                
                if selected_template:
                    template_data = st.session_state.content_templates.get_template(selected_template)
                    st.info(f"**Structure:** {template_data.get('structure', 'N/A')}")
                    st.markdown("**Template:**")
                    st.code(template_data.get('template', 'N/A'), language="text")
                    
                    # Template variables
                    st.subheader("Fill in variables:")
                    variables = {}
                    template_text = template_data.get('template', '')
                    
                    # Extract variable placeholders
                    import re
                    placeholders = re.findall(r'\[([^\]]+)\]', template_text)
                    for placeholder in set(placeholders):
                        variables[placeholder] = st.text_input(f"{placeholder}:")
                    
                    if st.button("Generate from Template"):
                        result = st.session_state.content_templates.apply_template(selected_template, variables)
                        st.success("Generated content:")
                        st.text_area("Result:", value=result, height=200)
            
            elif lexi_feature == "Engagement Scoring":
                st.subheader("⚡ Engagement Scoring")
                engagement = st.session_state.engagement_scorer.score_engagement(text_to_analyze)
                
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Overall Engagement Score", f"{engagement['engagement_score']:.1f}/100")
                    st.info(f"**Level:** {engagement['engagement_level']}")
                
                with col2:
                    st.subheader("Component Scores")
                    for component, score in engagement['component_scores'].items():
                        st.metric(component.replace('_', ' ').title(), f"{score:.1f}/100")
                
                st.subheader("📈 Strengths")
                for strength in engagement['strengths']:
                    st.success(f"✓ {strength}")
                
                st.subheader("⚠️ Weaknesses")
                for weakness in engagement['weaknesses']:
                    st.warning(f"✗ {weakness}")
                
                st.subheader("💡 Improvement Tips")
                for tip in engagement['improvement_tips']:
                    st.write(f"• {tip}")
            
            elif lexi_feature == "Brand Voice Consistency":
                st.subheader("🎨 Brand Voice Consistency")
                
                brand_type = st.selectbox(
                    "Select brand voice type:",
                    ["corporate", "startup", "friendly", "luxury", "educational"]
                )
                
                st.session_state.brand_voice.set_brand_attributes(brand_type)
                
                consistency = st.session_state.brand_voice.analyze_brand_consistency(text_to_analyze)
                
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Overall Consistency", f"{consistency['overall_consistency_score']:.1f}/100")
                    st.info(f"**Level:** {consistency['consistency_level']}")
                
                with col2:
                    st.subheader("Component Scores")
                    for component, score in consistency['component_scores'].items():
                        st.metric(component.replace('_', ' ').title(), f"{score:.1f}/100")
                
                if consistency['issues']:
                    st.subheader("⚠️ Issues Found")
                    for issue in consistency['issues']:
                        st.warning(f"• {issue}")
                
                st.subheader("🎯 Brand Attributes")
                for key, value in consistency['brand_attributes'].items():
                    if key not in ['avoid', 'examples']:
                        st.write(f"**{key}:** {value}")
            
            elif lexi_feature == "Grammar Check":
                st.subheader("✍️ Grammar & Style Check")
                grammar = st.session_state.grammar_checker.check_grammar(text_to_analyze)
                
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Grammar Score", f"{grammar['score']:.1f}/100")
                with col2:
                    st.metric("Issues Found", grammar['issues_found'])
                
                if grammar['issues']:
                    st.subheader("Issues Detected:")
                    for issue in grammar['issues']:
                        st.warning(f"• {issue}")
                
                if grammar['suggestions']:
                    st.subheader("Suggestions:")
                    for suggestion in grammar['suggestions']:
                        st.info(f"💡 {suggestion}")


# ==================== TAB 10: OMNEKY MULTIVARIATE TESTING ====================
with tab10:
    st.header("🔬 Omneky Multivariate Testing")
    st.markdown("Advanced A/B/N testing framework with statistical analysis")
    
    testing_mode = st.selectbox(
        "Select Mode",
        ["Create New Test", "View Test Results", "Creative Variations", "Performance Benchmarking", "Fatigue Detection"]
    )
    
    if testing_mode == "Create New Test":
        st.subheader("📊 Create Multivariate Test")
        
        test_name = st.text_input("Test Name:")
        hypothesis = st.text_area("Test Hypothesis:", height=80)
        
        num_variants = st.slider("Number of Variants", 2, 5, 3)
        
        variants = {}
        st.markdown("### Variant Content")
        var_cols = st.columns(num_variants)
        
        for i in range(num_variants):
            with var_cols[i % num_variants]:
                variants[f"Variant {i+1}"] = st.text_area(f"Variant {i+1} Content:", height=100, key=f"var_{i}")
        
        if st.button("Create Test"):
            if test_name and all(variants.values()):
                test = st.session_state.multivariate_testing.create_multivariate_test(
                    test_name, variants, hypothesis
                )
                st.success(f"Test created: {test['id']}")
                st.info(f"Minimum sample size: {test['minimum_sample_size']:,}")
                st.info(f"Estimated duration: {test['expected_duration_days']:.1f} days")
                st.session_state.current_test_id = test['id']
    
    elif testing_mode == "View Test Results":
        st.subheader("📈 Test Results & Analysis")
        
        # Simulate test data (in production, this would be from database)
        test_id = st.text_input("Enter Test ID:", value=st.session_state.get('current_test_id', ''))
        
        if test_id and st.button("Load Results"):
            # Simulate recording variant performance
            test = st.session_state.multivariate_testing.active_tests.get(test_id, {})
            if not test:
                st.warning("Test not found. Creating sample test...")
                # Create sample for demo
                test = st.session_state.multivariate_testing.create_multivariate_test(
                    "Sample Test",
                    {"Variant A": "Sample A", "Variant B": "Sample B"},
                    "Testing messaging approach"
                )
                test_id = test['id']
            
            # Record sample performance
            st.session_state.multivariate_testing.record_variant_performance(test_id, 0, 1000, 45, 15, 600)
            st.session_state.multivariate_testing.record_variant_performance(test_id, 1, 1000, 38, 10, 600)
            
            results = st.session_state.multivariate_testing.get_test_results(test_id)
            
            st.subheader(f"Test: {results['test_name']}")
            st.info(f"Hypothesis: {results['hypothesis']}")
            
            # Winner announcement
            st.subheader("🏆 Winner")
            winner_col, lift_col, significance_col = st.columns(3)
            
            with winner_col:
                st.metric("Winning Variant", results['winner'] or "TBD")
            with lift_col:
                st.metric("Lift vs Control", results['winner_lift'])
            with significance_col:
                st.metric("Statistical Significance", results['statistical_significance'])
            
            # Variant breakdown
            st.subheader("📊 Variant Performance")
            for variant in results['variant_results']:
                with st.expander(f"{variant['variant_name']} - Efficiency Score: {variant['efficiency_score']}/100"):
                    metric_cols = st.columns(6)
                    with metric_cols[0]:
                        st.metric("Impressions", f"{variant['impressions']:,}")
                    with metric_cols[1]:
                        st.metric("Clicks", f"{variant['clicks']:,}")
                    with metric_cols[2]:
                        st.metric("CTR", f"{variant['ctr']:.2f}%")
                    with metric_cols[3]:
                        st.metric("Conversions", f"{variant['conversions']:,}")
                    with metric_cols[4]:
                        st.metric("CVR", f"{variant['cvr']:.2f}%")
                    with metric_cols[5]:
                        st.metric("CPA", f"${variant['cpa']:.2f}")
            
            st.info(results['recommendation'])
    
    elif testing_mode == "Creative Variations":
        st.subheader("🎨 Generate Creative Variations")
        
        product_name = st.text_input("Product Name:")
        topic = st.text_input("Topic/Focus:")
        num_variations = st.slider("Number of Variations", 2, 5, 3)
        
        if st.button("Generate Variations"):
            if product_name and topic:
                variations = st.session_state.creative_variation_gen.create_variation_set(
                    product_name, topic, num_variations
                )
                
                for idx, var in enumerate(variations, 1):
                    with st.expander(f"**{var['name']}** - {var['testing_objective']}", expanded=(idx==1)):
                        st.subheader("Headline")
                        st.write(var['headline'])
                        
                        st.subheader("Body Copy")
                        st.write(var['body_copy'])
                        
                        st.subheader("Call-to-Action")
                        st.write(var['cta'])
                        
                        # Copy to clipboard option
                        full_variation = f"{var['headline']}\n\n{var['body_copy']}\n\n{var['cta']}"
                        st.code(full_variation)
    
    elif testing_mode == "Performance Benchmarking":
        st.subheader("📊 Benchmark Your Performance")
        
        industry = st.selectbox(
            "Select Industry",
            ["ecommerce", "saas", "lead_generation", "retail"]
        )
        
        # Input actual metrics
        metric_cols = st.columns(5)
        with metric_cols[0]:
            ctr = st.number_input("CTR (%):", min_value=0.0, value=1.5, step=0.1)
        with metric_cols[1]:
            cvr = st.number_input("CVR (%):", min_value=0.0, value=2.5, step=0.1)
        with metric_cols[2]:
            cpc = st.number_input("CPC ($):", min_value=0.0, value=0.75, step=0.05)
        with metric_cols[3]:
            cpa = st.number_input("CPA ($):", min_value=0.0, value=30.0, step=1.0)
        with metric_cols[4]:
            roas = st.number_input("ROAS:", min_value=0.0, value=3.5, step=0.1)
        
        if st.button("Compare to Benchmarks"):
            actual_metrics = {
                "ctr": ctr,
                "cvr": cvr,
                "cpc": cpc,
                "cpa": cpa,
                "roas": roas
            }
            
            comparison = st.session_state.performance_benchmarking.compare_to_benchmarks(
                actual_metrics, industry
            )
            
            st.subheader(f"Performance vs {industry.upper()} Benchmarks")
            st.info(f"Overall Performance: {comparison['overall_performance_vs_benchmark']}")
            
            # Detailed comparison
            for metric, data in comparison['metrics_comparison'].items():
                with st.expander(f"{metric.upper()} - {data['performance']}"):
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Your Performance", f"{data['actual']:.2f}")
                    with col2:
                        st.metric("Industry Benchmark", f"{data['benchmark']:.2f}")
                    with col3:
                        st.metric("Variance", data['variance'])
            
            st.subheader("Recommendations")
            for rec in comparison['recommendations']:
                st.info(f"💡 {rec}")
    
    elif testing_mode == "Fatigue Detection":
        st.subheader("😴 Creative Fatigue Detection")
        st.markdown("Monitor creative performance decline and fatigue signals")
        
        # Simulate metrics history
        st.markdown("### Enter Performance Data Over Time")
        
        period_cols = st.columns(2)
        with period_cols[0]:
            num_periods = st.slider("Number of time periods:", 2, 5, 3)
        
        metrics_history = []
        
        for period in range(num_periods):
            with st.expander(f"Period {period + 1}", expanded=(period==0)):
                metric_cols = st.columns(4)
                with metric_cols[0]:
                    ctr = st.number_input(f"CTR % (Period {period+1}):", min_value=0.0, value=1.5 if period==0 else 1.2-period*0.15, step=0.1, key=f"ctr_{period}")
                with metric_cols[1]:
                    cvr = st.number_input(f"CVR % (Period {period+1}):", min_value=0.0, value=2.5 if period==0 else 2.0-period*0.2, step=0.1, key=f"cvr_{period}")
                with metric_cols[2]:
                    cpc = st.number_input(f"CPC $ (Period {period+1}):", min_value=0.0, value=0.75 if period==0 else 0.75+period*0.1, step=0.05, key=f"cpc_{period}")
                with metric_cols[3]:
                    frequency = st.number_input(f"Avg Frequency (Period {period+1}):", min_value=0.0, value=2.5 if period==0 else 2.5+period*0.5, step=0.1, key=f"freq_{period}")
                
                metrics_history.append({
                    "ctr": ctr,
                    "cvr": cvr,
                    "cpc": cpc,
                    "avg_frequency": frequency
                })
        
        if st.button("Analyze Fatigue"):
            if len(metrics_history) >= 2:
                fatigue = st.session_state.fatigue_detector.detect_fatigue(metrics_history)
                
                col1, col2 = st.columns(2)
                with col1:
                    fatigue_level = fatigue['fatigue_level']
                    fatigue_color = {
                        "Critical": "🔴",
                        "High": "🟠",
                        "Moderate": "🟡",
                        "Low": "🟢"
                    }
                    st.metric("Fatigue Level", f"{fatigue_color.get(fatigue_level, '⚪')} {fatigue_level}")
                
                with col2:
                    st.info(fatigue['recommendation'])
                
                st.subheader("📊 Fatigue Indicators")
                indicator_cols = st.columns(4)
                indicators = fatigue['indicators']
                
                with indicator_cols[0]:
                    st.metric("CTR Decline", f"{indicators['ctr_decline']:.1f}%")
                with indicator_cols[1]:
                    st.metric("CVR Decline", f"{indicators['cvr_decline']:.1f}%")
                with indicator_cols[2]:
                    st.metric("Cost Increase", f"{indicators['cost_increase']:.1f}%")
                with indicator_cols[3]:
                    st.metric("Avg Frequency", f"{indicators['frequency_fatigue']:.2f}x")
                
                st.subheader("🎯 Recommended Actions")
                for i, action in enumerate(fatigue['suggested_actions'], 1):
                    st.write(f"{i}. {action}")
st.divider()

footer_cols = st.columns(3)

with footer_cols[0]:
    st.markdown("**📚 Core Features:**")
    st.markdown("✅ Content Generation (Omneky)")
    st.markdown("✅ Copywriting Engine (Lexi AI)")
    st.markdown("✅ A/B Testing Framework")
    st.markdown("✅ Madgicx Campaign Mgmt")

with footer_cols[1]:
    st.markdown("**🔬 Advanced Tools:**")
    st.markdown("✅ Multivariate Testing")
    st.markdown("✅ Plagiarism Detection")
    st.markdown("✅ Tone Detection")
    st.markdown("✅ Creative Variations")
    st.markdown("✅ Fatigue Detection")

with footer_cols[2]:
    st.markdown("**📊 Analytics & Insights:**")
    st.markdown("✅ Readability Analysis")
    st.markdown("✅ Engagement Scoring")
    st.markdown("✅ Brand Consistency")
    st.markdown("✅ Performance Benchmarking")

st.markdown("---")
st.markdown("🤖 **AI Content Generator Pro** | Complete Alternative to Omneky, Madgicx & Lexi AI")
st.markdown("Powered by Ollama | Built with Streamlit | v2.0")

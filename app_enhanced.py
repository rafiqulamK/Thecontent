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

if 'generated_posts' not in st.session_state:
    st.session_state.generated_posts = []

if 'saved_posts' not in st.session_state:
    st.session_state.saved_posts = []

st.title("🤖 AI Content Generator Pro")
st.markdown("**Complete Alternative to Omneky, Madgicx & Lexi AI**")
st.markdown("Generate, optimize, and schedule content with competitive intelligence")

# Main navigation tabs
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🎯 Content Generator",
    "✍️ Copywriting Assistant",
    "🧪 A/B Testing Lab",
    "📅 Content Calendar",
    "📊 Analytics Dashboard",
    "🎯 Competitor Analysis"
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


# ==================== FOOTER ====================
st.divider()

footer_cols = st.columns(3)

with footer_cols[0]:
    st.markdown("**📚 Features:**")
    st.markdown("✅ Content Generation")
    st.markdown("✅ Copywriting Engine")
    st.markdown("✅ A/B Testing")

with footer_cols[1]:
    st.markdown("**🛠️ Tools:**")
    st.markdown("✅ Content Calendar")
    st.markdown("✅ Analytics")
    st.markdown("✅ Competitor Analysis")

with footer_cols[2]:
    st.markdown("**🎯 Models:**")
    st.markdown("- Gemma 2B (Recommended)")
    st.markdown("- Mistral")
    st.markdown("- Llama2")

st.markdown("---")
st.markdown("🤖 **AI Content Generator Pro** | Complete Alternative to Omneky, Madgicx & Lexi AI")
st.markdown("Powered by Ollama | Built with Streamlit | v2.0")

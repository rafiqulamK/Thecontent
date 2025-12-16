import streamlit as st
import ollama
import json
import os
from datetime import datetime
from social_media_generator import SocialMediaGenerator

st.set_page_config(page_title="AI Content Generator Pro", page_icon="🤖", layout="wide")

st.title("🤖 AI Content Generator Pro")
st.markdown("**Powered by Omneky (Creative Optimization) + Madgicx (Campaign Analytics)**")
st.markdown("Generate optimized social media content with performance predictions")

# Sidebar configuration
with st.sidebar:
    st.header("⚙️ Settings")
    
    # Model selection
    model = st.selectbox(
        "Choose Model",
        ["gemma:2b", "mistral", "llama2", "phi"],
        index=0,
        help="Select which LLM to use. gemma:2b is best for Codespaces"
    )
    
    # Platform selection
    platform = st.selectbox(
        "Platform",
        ["Twitter", "LinkedIn", "Instagram", "Facebook", "TikTok"],
        help="Target social media platform"
    )
    
    # Tone selection
    tone = st.select_slider(
        "Tone",
        options=["Casual", "Professional", "Funny", "Inspirational", "Urgent"],
        value="Professional",
        help="Choose the tone of the content"
    )
    
    # Temperature control
    temperature = st.slider(
        "Creativity",
        min_value=0.0,
        max_value=1.0,
        value=0.7,
        step=0.1,
        help="Higher = more creative, Lower = more focused"
    )
    
    # Number of posts
    num_posts = st.slider("Generate variations", 1, 5, 3)
    
    # Hashtag strategy
    hashtag_strategy = st.selectbox(
        "Hashtag Strategy",
        ["trending", "niche", "balanced"],
        help="Omneky-style hashtag optimization"
    )

# Main content area
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📝 Content Generation")
    topic = st.text_input("Topic", "Artificial Intelligence", placeholder="Enter the topic for your content")

with col2:
    st.subheader("👥 Audience Settings")
    audience_size = st.number_input("Audience Size", min_value=10000, value=500000, step=10000)
    interest_match = st.slider("Interest Match %", 0, 100, 75)

# Generate button
generate_button = st.button("🚀 Generate & Optimize Content", use_container_width=True, type="primary")

# Initialize session state
if 'generator' not in st.session_state:
    st.session_state.generator = SocialMediaGenerator(model=model)

if 'generated_posts' not in st.session_state:
    st.session_state.generated_posts = []

# Generate content with Omneky + Madgicx optimization
if generate_button and topic:
    st.session_state.generator = SocialMediaGenerator(model=model)
    progress_bar = st.progress(0)
    posts = []
    
    try:
        for i in range(num_posts):
            prompt = f"""
Create a {platform} post about {topic}.
Tone: {tone}

Requirements:
1. Engaging opening that captures attention
2. Clear, concise message
3. Current and relevant context
4. Use {hashtag_strategy} hashtags
5. Strong call to action
6. Make it shareable and trendy

{platform} Post:
"""
            
            progress_bar.progress((i + 1) / num_posts)
            
            with st.spinner(f"Generating & optimizing post {i+1}/{num_posts}..."):
                response = ollama.generate(
                    model=model,
                    prompt=prompt,
                    options={'temperature': temperature}
                )
                
                content = response['response']
                
                # Omneky creative optimization
                optimization = st.session_state.generator.creative_optimizer.optimize_creative(content, platform)
                
                # Madgicx campaign analysis
                context = st.session_state.generator.trend_analyzer.get_current_context()
                post_data = {
                    'id': len(st.session_state.generated_posts) + i,
                    'platform': platform,
                    'topic': topic,
                    'content': content,
                    'tone': tone,
                    'model': model,
                    'timestamp': datetime.now().isoformat(),
                    'context': context,
                    'hashtag_strategy': hashtag_strategy,
                    'trend_aware': True,
                    'optimization_score': optimization['overall_score'] * 100,
                    'optimization_details': optimization
                }
                
                # Campaign prediction
                audience = {
                    'audience_size': audience_size,
                    'interest_match': interest_match,
                    'preferred_tone': tone.lower(),
                    'saturation': 0.3
                }
                
                performance = st.session_state.generator.campaign_analyzer.predict_performance(post_data, audience)
                post_data['performance_prediction'] = performance
                
                posts.append(post_data)
        
        st.session_state.generated_posts.extend(posts)
        st.success("✅ Content Generated & Optimized Successfully!")
        
        # Display results in tabs
        st.subheader(f"📄 Generated {platform} Posts")
        
        for i, post in enumerate(posts, 1):
            with st.expander(f"Post #{i} - Score: {post['optimization_score']:.0f}%", expanded=(i == 1)):
                col1, col2, col3 = st.columns([2, 1, 1])
                
                # Content
                with col1:
                    st.markdown("**📝 Content:**")
                    st.markdown(post['content'])
                
                # Omneky Optimization Score
                with col2:
                    st.markdown("**⚡ Omneky Optimization:**")
                    opt = post['optimization_details']
                    st.metric("Overall Score", f"{opt['overall_score']:.0f}/100")
                    st.metric("Hook Strength", f"{opt['hook_strength']:.0f}")
                    st.metric("Emotional Appeal", f"{opt['emotional_appeal']:.0f}")
                    st.metric("CTA Effectiveness", f"{opt['cta_effectiveness']:.0f}")
                
                # Madgicx Campaign Prediction
                with col3:
                    st.markdown("**📊 Madgicx Prediction:**")
                    perf = post['performance_prediction']
                    st.metric("Est. CTR %", f"{perf['estimated_ctr']:.2f}%")
                    st.metric("Est. CPC", f"${perf['estimated_cpc']:.2f}")
                    st.metric("Quality Score", f"{perf['quality_score']:.0f}")
                    st.metric("Audience Align", f"{perf['audience_alignment']:.0f}%")
                
                # Scaling Potential
                st.divider()
                scaling = post['performance_prediction']['scaling_potential']
                st.markdown("**🚀 Scaling Potential:**")
                col_scale1, col_scale2 = st.columns(2)
                with col_scale1:
                    st.info(f"Status: {scaling['status']}")
                with col_scale2:
                    st.info(f"Budget Multiplier: {scaling['budget_multiplier']}x")
                
                # Recommendations
                st.markdown("**💡 Optimization Recommendations:**")
                for rec in post['performance_prediction']['recommendations']:
                    st.write(f"• {rec}")
                
                # Action buttons
                col_btn1, col_btn2, col_btn3 = st.columns(3)
                with col_btn1:
                    if st.button(f"📋 Copy Post #{i}", key=f"copy_{i}", use_container_width=True):
                        st.code(post['content'], language=None)
                        st.info("Content copied!")
                with col_btn2:
                    if st.button(f"💾 Save Post #{i}", key=f"save_{i}", use_container_width=True):
                        save_content([post])
                        st.success("Post saved to library!")
                with col_btn3:
                    if st.button(f"📊 View Details #{i}", key=f"detail_{i}", use_container_width=True):
                        st.json(post)
    
    except Exception as e:
        st.error(f"❌ Error generating content: {str(e)}")
        st.info("Make sure Ollama is running with: `ollama serve`")

# Sidebar history and analytics
with st.sidebar:
    st.divider()
    st.subheader("📚 Content Library")
    
    if st.session_state.generated_posts:
        # Analytics
        recent_posts = st.session_state.generated_posts[-10:]
        avg_score = sum(p.get('optimization_score', 0) for p in recent_posts) / len(recent_posts) if recent_posts else 0
        
        st.metric("Recent Avg Score", f"{avg_score:.0f}%")
        st.metric("Posts Generated", len(st.session_state.generated_posts))
        
        st.divider()
        st.write("**Recent Posts:**")
        for i, post in enumerate(recent_posts[-5:], 1):
            score = post.get('optimization_score', 0)
            with st.expander(f"{post['platform']} - {score:.0f}% - {post['topic'][:15]}..."):
                st.write(post['content'][:200] + "...")
                st.caption(f"📅 {post['timestamp'][:10]}")
    else:
        st.info("No posts generated yet")

# Helper functions
def save_content(posts, filename="content_library.json"):
    """Save generated content to JSON"""
    try:
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                existing = json.load(f)
        else:
            existing = []
    except (FileNotFoundError, json.JSONDecodeError):
        existing = []
    
    existing.extend(posts)
    
    with open(filename, 'w') as f:
        json.dump(existing, f, indent=2)
    
    return len(existing)

def load_content(filename="content_library.json"):
    """Load saved content"""
    if not os.path.exists(filename):
        return []
    
    with open(filename, 'r') as f:
        return json.load(f)

# Footer
st.divider()
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Generated Posts", len(st.session_state.generated_posts))
with col2:
    if os.path.exists("content_library.json"):
        saved = len(load_content())
        st.metric("Saved Posts", saved)
    else:
        st.metric("Saved Posts", 0)
with col3:
    st.metric("Model", model)
with col4:
    st.metric("Optimization", "Omneky+Madgicx")

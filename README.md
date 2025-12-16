# Thecontent
Complete Guide to Using Ollama with GitHub Codespaces

Perfect! Using Ollama in GitHub Codespaces is an excellent way to get started with LLMs without heavy local setup. Here's a comprehensive guide:

1. Setting Up Ollama in GitHub Codespaces

Step 1: Create a New Codespace

1. Go to your GitHub repository
2. Click "Code" → "Codespaces" → "Create codespace on main"
3. Choose machine type (4-core, 8GB RAM minimum for LLMs)

Step 2: Install Ollama in Codespace

```bash
# In your codespace terminal
curl -fsSL https://ollama.ai/install.sh | sh

# Add Ollama to PATH
echo 'export PATH="$PATH:/home/codespace/.local/bin"' >> ~/.bashrc
source ~/.bashrc

# Verify installation
ollama --version
```

2. Basic Ollama Operations

Download and Run Models

```bash
# List available models (small ones work best in Codespaces)
ollama list

# Pull and run small models (Codespaces-friendly)
ollama pull gemma:2b  # 2B parameters - best for Codespaces
ollama pull phi        # 2.7B parameters
ollama pull mistral    # 7B parameters (might be heavy)
ollama pull qwen2.5:3b  # 3B parameters

# Run a model interactively
ollama run gemma:2b
# Then type prompts like: "Write a tweet about AI"
```

Create a Simple Python Script

```python
# main.py
import subprocess
import json

def run_ollama(prompt, model="gemma:2b"):
    """Run Ollama from Python"""
    result = subprocess.run(
        ["ollama", "run", model, prompt],
        capture_output=True,
        text=True,
        timeout=30
    )
    return result.stdout

# Test it
response = run_ollama("Write a social media post about renewable energy")
print(response)
```

3. Advanced Ollama Usage with Python API

Install Required Packages

```bash
pip install ollama requests streamlit gradio
```

Using Ollama Python Library

```python
# ollama_demo.py
import ollama
import json

# Pull a model
ollama.pull('gemma:2b')

# Simple generation
response = ollama.generate(
    model='gemma:2b',
    prompt='Create 3 Instagram captions for a coffee shop'
)
print(response['response'])

# Chat with context
response = ollama.chat(
    model='gemma:2b',
    messages=[
        {'role': 'system', 'content': 'You are a social media expert.'},
        {'role': 'user', 'content': 'Write a tweet about our new AI tool'}
    ]
)
print(response['message']['content'])
```

4. Building a Content Generation System

Create a Social Media Content Generator

```python
# social_media_generator.py
import ollama
import json
from datetime import datetime
import schedule
import time

class SocialMediaGenerator:
    def __init__(self, model='gemma:2b'):
        self.model = model
        self.content_history = []
        
    def generate_post(self, platform, topic, tone="professional"):
        prompt = f"""
        Create a {platform} post about {topic}.
        Tone: {tone}
        Requirements:
        1. Engaging opening
        2. Clear message
        3. Relevant hashtags
        4. Call to action
        
        {platform} Post:
        """
        
        response = ollama.generate(
            model=self.model,
            prompt=prompt,
            options={'temperature': 0.7, 'num_predict': 200}
        )
        
        post = {
            'platform': platform,
            'topic': topic,
            'content': response['response'],
            'timestamp': datetime.now().isoformat()
        }
        
        self.content_history.append(post)
        return post
    
    def batch_generate(self, content_calendar):
        """Generate content for the week"""
        generated = []
        for item in content_calendar:
            post = self.generate_post(
                platform=item['platform'],
                topic=item['topic'],
                tone=item.get('tone', 'professional')
            )
            generated.append(post)
        return generated

# Usage
generator = SocialMediaGenerator()

# Content calendar for the week
content_calendar = [
    {'platform': 'twitter', 'topic': 'AI in marketing', 'day': 'monday'},
    {'platform': 'linkedin', 'topic': 'Digital transformation', 'day': 'tuesday'},
    {'platform': 'instagram', 'topic': 'Behind the scenes', 'day': 'wednesday'},
]

# Generate content
posts = generator.batch_generate(content_calendar)
for post in posts:
    print(f"\n=== {post['platform'].upper()} ===")
    print(post['content'])
    print("-" * 50)
```

5. Creating a Web Interface with Streamlit

```python
# app.py
import streamlit as st
import ollama
import json

st.title("🤖 AI Content Generator")
st.sidebar.header("Settings")

# Model selection
model = st.sidebar.selectbox(
    "Choose Model",
    ["gemma:2b", "mistral", "llama2", "phi"],
    index=0
)

# Platform selection
platform = st.sidebar.selectbox(
    "Platform",
    ["Twitter", "LinkedIn", "Instagram", "Facebook", "TikTok"]
)

# Content parameters
topic = st.text_input("Topic", "Artificial Intelligence")
tone = st.select_slider(
    "Tone",
    options=["Casual", "Professional", "Funny", "Inspirational", "Urgent"]
)

num_posts = st.slider("Number of variations", 1, 5, 3)

if st.button("Generate Content"):
    with st.spinner(f"Generating {num_posts} {platform} posts..."):
        posts = []
        for i in range(num_posts):
            prompt = f"""
            Create a {platform} post about {topic}.
            Tone: {tone}
            Include relevant hashtags.
            Make it engaging and authentic.
            
            Post {i+1}:
            """
            
            response = ollama.generate(
                model=model,
                prompt=prompt,
                options={'temperature': 0.8}
            )
            
            posts.append(response['response'])
    
    # Display results
    st.success("Content Generated!")
    for i, post in enumerate(posts, 1):
        with st.expander(f"Post #{i}"):
            st.write(post)
            if st.button(f"Copy Post #{i}", key=f"copy_{i}"):
                st.code(post, language=None)

# Save history
if 'generated_posts' not in st.session_state:
    st.session_state.generated_posts = []

if posts:
    st.session_state.generated_posts.extend(posts)
    
    st.sidebar.subheader("History")
    for i, post in enumerate(st.session_state.generated_posts[-5:]):
        st.sidebar.text_area(f"Post {i+1}", post, height=100)
```

6. GitHub Codespace Configuration

Create .devcontainer/devcontainer.json

```json
{
  "name": "Ollama LLM Workspace",
  "image": "mcr.microsoft.com/devcontainers/base:ubuntu",
  "features": {
    "ghcr.io/devcontainers/features/python:1": {
      "version": "3.10"
    },
    "ghcr.io/devcontainers/features/docker-in-docker:2": {}
  },
  "postCreateCommand": "curl -fsSL https://ollama.ai/install.sh | sh && pip install -r requirements.txt",
  "postAttachCommand": "ollama pull gemma:2b",
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-python.python",
        "ms-toolsai.jupyter",
        "GitHub.copilot"
      ]
    }
  },
  "forwardPorts": [8501, 11434],
  "portsAttributes": {
    "8501": {
      "label": "Streamlit App",
      "onAutoForward": "openPreview"
    },
    "11434": {
      "label": "Ollama API"
    }
  }
}
```

Create requirements.txt

```
ollama
streamlit
schedule
requests
python-dotenv
pandas
numpy
```

7. Running Your Application

Start Ollama and Your App

```bash
# In one terminal
ollama serve

# In another terminal
# For Streamlit app
streamlit run app.py --server.port 8501

# Or for basic Python script
python social_media_generator.py
```

Access Your Application

· Streamlit app: Check the "Ports" tab in Codespace
· Ollama API: http://localhost:11434
· Test API: curl http://localhost:11434/api/tags

8. Saving and Loading Models

Save Generated Content

```python
import json
from datetime import datetime

def save_content(posts, filename="content_library.json"):
    """Save generated content to JSON"""
    try:
        with open(filename, 'r') as f:
            existing = json.load(f)
    except FileNotFoundError:
        existing = []
    
    existing.extend(posts)
    
    with open(filename, 'w') as f:
        json.dump(existing, f, indent=2)
    
    print(f"Saved {len(posts)} posts to {filename}")

# Save your generated posts
save_content(posts)
```

Load and Manage Content

```python
def load_content(filename="content_library.json"):
    """Load saved content"""
    with open(filename, 'r') as f:
        return json.load(f)

def search_content(keyword):
    """Search through saved content"""
    library = load_content()
    results = []
    for post in library:
        if keyword.lower() in post['content'].lower():
            results.append(post)
    return results
```

9. Tips for Codespaces

1. Memory Management: Use small models (2-7B parameters)
2. Persistence: Save important files in your repository
3. Port Forwarding: Use the ports tab to access web interfaces
4. Cost Control: Stop Codespace when not in use
5. Extensions: Use GitHub Copilot for help

10. Sample Repository Structure

```
your-repo/
├── .devcontainer/
│   └── devcontainer.json
├── .gitignore
├── requirements.txt
├── app.py                    # Streamlit interface
├── social_media_generator.py # Core logic
├── content_library.json      # Generated content
├── prompts/                  # Prompt templates
│   ├── twitter_prompts.txt
│   ├── instagram_prompts.txt
│   └── linkedin_prompts.txt
└── README.md
```

11. Quick Start Commands

```bash
# Clone and setup
git clone https://github.com/yourusername/llm-content-generator
cd llm-content-generator

# Open in Codespace (through GitHub UI)

# Once in Codespace:
ollama pull gemma:2b
pip install -r requirements.txt
streamlit run app.py
```

This setup gives you a complete, cloud-based LLM environment for content generation that you can access from anywhere with a browser!

# Developer Quick Reference Guide

## 🚀 Getting Started

### Clone & Setup
```bash
git clone https://github.com/yourusername/thecontent.git
cd thecontent
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Run Application
```bash
# Development with Streamlit
streamlit run app.py

# Production with REST API
uvicorn api_server:app --host 0.0.0.0 --port 8000
```

---

## 📁 Module Overview

### Core Modules

| Module | Purpose | Key Classes | Status |
|--------|---------|-----------|--------|
| `app.py` | Streamlit UI (10 tabs) | StreamlitApp | ✅ Active |
| `copywriting_engine.py` | Lexi AI core | CopywritingEngine | ✅ Active |
| `lexi_advanced_features.py` | Lexi advanced | EngagementScorer | ✅ Active |
| `omneky_advanced_features.py` | Omneky advanced | MultiVariateTestingFramework | ✅ Active |
| `madgicx_advanced.py` | Meta ads | MetaAdsOptimizer | ✅ Active |
| `campaign_management.py` | Campaign tracking | CampaignDashboard | ✅ Active |

### Infrastructure Modules (NEW)

| Module | Purpose | Key Classes | Status |
|--------|---------|-----------|--------|
| `auth_system.py` | Multi-user auth | AuthenticationManager | ✅ Ready |
| `platform_integrations.py` | Platform APIs | FacebookAdsAPI, etc | ✅ Ready |
| `workflow_engine.py` | Automation | WorkflowEngine | ✅ Ready |
| `analytics_engine.py` | Reports & forecasting | PerformanceReport | ✅ Ready |
| `ai_image_generator.py` | Image generation | AIImageManager | ✅ Ready |
| `rest_api.py` | REST API | RestAPIManager | ✅ Ready |

---

## 🔧 Common Tasks

### Task 1: Generate Content

```python
from copywriting_engine import CopywritingEngine

engine = CopywritingEngine()

# Generate headlines
headlines = engine.generate_power_headlines(
    topic="AI Marketing",
    audience="B2B CTOs",
    count=5
)

# Analyze plagiarism
plagiarism = engine.plagiarism_detector.check_plagiarism(text)

# Check tone
tone = engine.tone_detector.detect_tone(text)

# Analyze readability
readability = engine.readability_analyzer.analyze(text)
```

### Task 2: Create & Run Campaign

```python
from campaign_management import CampaignDashboard, Campaign
from platform_integrations import PlatformAPIManager

# Create campaign
campaign = Campaign(
    name="Q4 Sales Blitz",
    objective="CONVERSIONS",
    budget=5000,
    start_date="2024-12-01"
)

# Manage across platforms
platform_mgr = PlatformAPIManager()
platform_mgr.add_platform("facebook", access_token="...", app_id="...")
platform_mgr.add_platform("instagram", access_token="...", app_id="...")

# Publish
result = platform_mgr.publish_to_all(campaign, content)
```

### Task 3: Setup Automation

```python
from workflow_engine import WorkflowEngine, TriggerType, ActionType

engine = WorkflowEngine()

# Create daily posting workflow
trigger = WorkflowTrigger(
    TriggerType.SCHEDULE,
    {'schedule': {'interval': 'daily', 'time': '09:00'}}
)

workflow = engine.create_workflow("Daily Content Post", trigger)
workflow.add_action(WorkflowAction(
    ActionType.PUBLISH,
    {'platforms': ['facebook', 'instagram']}
))

# Enable it
engine.enable_workflow(workflow.workflow_id)

# When scheduled time comes, it auto-executes
```

### Task 4: Get Analytics Report

```python
from analytics_engine import PerformanceReport, CustomReportBuilder

builder = CustomReportBuilder()

# Generate executive summary
summary = builder.build_executive_summary(
    campaign_ids=['camp_123', 'camp_456']
)

# Get detailed report
report = builder.build_detailed_report(
    campaign_id='camp_123',
    include_forecast=True
)

# Export
json_export = builder.export_report(report, format='json')
csv_export = builder.export_report(report, format='csv')
```

### Task 5: Generate Campaign Images

```python
from ai_image_generator import AIImageManager

manager = AIImageManager()

# Single image
images = manager.generator.generate_image(
    prompt="Modern SaaS product interface",
    quantity=3
)

# Campaign images (hero + social variants)
campaign_brief = {
    'campaign_id': 'camp_789',
    'product': 'AI Marketing Tool',
    'benefits': ['Easy to use', 'Powerful analytics'],
    'theme': 'tech innovation'
}

variants = manager.generate_campaign_images(
    campaign_brief,
    quantity_per_variant=3
)
```

### Task 6: Access REST API

```bash
# Get API key
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"user_id":"user_123","name":"My App"}' \
  https://api.thecontent.ai/v1/users/api-keys

# Use API key in requests
API_KEY="tco_abc123def456..."

# List campaigns
curl -H "X-API-Key: $API_KEY" \
  https://api.thecontent.ai/v1/campaigns

# Create campaign
curl -X POST \
  -H "X-API-Key: $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name":"New Campaign",
    "budget":1000,
    "objective":"CONVERSIONS"
  }' \
  https://api.thecontent.api/v1/campaigns

# Get analytics
curl -H "X-API-Key: $API_KEY" \
  "https://api.thecontent.ai/v1/analytics/campaigns?campaign_id=camp_123&days=7"
```

### Task 7: Register & Use Webhooks

```python
from rest_api import WebhookManager

manager = WebhookManager()

# Register webhook
webhook = manager.register_webhook(
    user_id="user_123",
    url="https://yourserver.com/webhooks",
    events=[
        'campaign.created',
        'content.published',
        'analytics.metric_update'
    ]
)

# When events happen, webhook receives:
# POST /webhooks
# Body: {
#   "event": "campaign.created",
#   "data": {...campaign_data...},
#   "timestamp": "2024-01-15T10:30:00Z"
# }

# Your server responds with 2xx to confirm
```

---

## 📊 Data Models

### Campaign Model
```python
{
    'campaign_id': str,          # Unique ID
    'user_id': str,              # Owner
    'name': str,                 # Campaign name
    'objective': str,            # CONVERSIONS, TRAFFIC, etc
    'budget': float,             # Daily budget in USD
    'status': str,               # ACTIVE, PAUSED, COMPLETED
    'platforms': List[str],      # ['facebook', 'instagram']
    'audience': {                # Audience targeting
        'age_min': int,
        'age_max': int,
        'genders': List[str],
        'interests': List[str]
    },
    'created_at': datetime,
    'updated_at': datetime
}
```

### Content Model
```python
{
    'content_id': str,
    'campaign_id': str,
    'type': str,                 # 'image', 'video', 'carousel'
    'platform': str,             # 'facebook', 'instagram', etc
    'text': str,                 # Copy
    'media_url': str,            # Image/video URL
    'cta': str,                  # Call-to-action
    'performance': {
        'impressions': int,
        'clicks': int,
        'conversions': int,
        'spend': float,
        'roas': float
    },
    'created_at': datetime
}
```

### User Model
```python
{
    'user_id': str,
    'email': str,
    'password_hash': str,        # bcrypt hash
    'api_keys': List[str],
    'workspace_ids': List[str],
    'quota': {
        'monthly_generations': int,
        'api_calls': int,
        'storage_mb': int
    },
    'created_at': datetime
}
```

---

## 🔐 Authentication

### Get User Session
```python
from auth_system import AuthenticationManager

auth = AuthenticationManager()

# Login
user = auth.authenticate(email="user@example.com", password="pass123")

# Validate session
if auth.validate_session(user.session_token):
    print("Valid session")

# Get user details
user = auth.get_user(user_id)
```

### Create API Key
```python
# Generate key with specific permissions
api_key = auth.generate_api_key(
    user_id="user_123",
    permissions=[
        'read:campaigns',
        'write:campaigns',
        'read:analytics'
    ]
)
print(f"Key: {api_key.key}")  # tco_abc123...
```

### Multi-user Workspaces
```python
# Create team workspace
workspace = auth.create_workspace(
    owner_id="user_123",
    workspace_name="Acme Corp",
    members=[
        {'user_id': 'user_456', 'role': 'admin'},
        {'user_id': 'user_789', 'role': 'member'}
    ]
)

# Change member role
auth.update_workspace_member(
    workspace_id=workspace.workspace_id,
    user_id='user_789',
    new_role='owner'
)
```

---

## 🧪 Testing

### Unit Tests
```bash
# Run all tests
pytest

# Run specific file
pytest tests/test_copywriting_engine.py

# Run with coverage
pytest --cov=. --cov-report=html
```

### Manual Testing
```python
# In Python REPL
from copywriting_engine import CopywritingEngine

engine = CopywritingEngine()
result = engine.generate_power_headlines("Python", count=3)
print(result)
```

### API Testing
```bash
# Using curl
curl -X GET https://api.thecontent.ai/v1/campaigns \
  -H "X-API-Key: test_key"

# Using Python requests
import requests

headers = {'X-API-Key': 'test_key'}
response = requests.get(
    'https://api.thecontent.ai/v1/campaigns',
    headers=headers
)
print(response.json())
```

---

## 🐛 Debugging

### Enable Debug Mode
```python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

logger.debug("This will print in debug mode")
```

### Check Session State (Streamlit)
```python
# In app.py
if st.checkbox("Debug: Show session state"):
    st.write(st.session_state)
```

### View API Logs
```python
# Check request log
from rest_api import RestAPIManager

api_mgr = RestAPIManager()
logs = api_mgr.request_log[-10:]  # Last 10 requests
for log in logs:
    print(f"{log['method']} {log['endpoint']} -> {log['status_code']}")
```

### Database Connection Check
```python
from database import SessionLocal

try:
    db = SessionLocal()
    db.execute("SELECT 1")
    print("✅ Database connected")
except Exception as e:
    print(f"❌ Database error: {e}")
```

---

## 📈 Performance Tips

### Optimize Content Generation
```python
# Cache generated content
import functools

@functools.lru_cache(maxsize=100)
def generate_headlines(topic: str):
    engine = CopywritingEngine()
    return engine.generate_power_headlines(topic)
```

### Batch API Requests
```python
# Instead of:
for campaign in campaigns:
    metrics = get_analytics(campaign)  # Slow

# Do:
campaign_ids = [c.id for c in campaigns]
all_metrics = get_batch_analytics(campaign_ids)  # Fast
```

### Use Streaming for Long Operations
```python
# Long-running image generation
with st.spinner("Generating images..."):
    images = manager.generate_campaign_images(brief)
```

### Cache Database Queries
```python
@st.cache_resource
def get_campaigns():
    db = SessionLocal()
    return db.query(Campaign).all()
```

---

## 📚 Key Concepts

### Triggers (Workflow)
- **SCHEDULE**: Run at specific time (daily, weekly, monthly)
- **EVENT**: Run when action happens (post published, etc)
- **CONDITION**: Run when metric threshold crossed (high CPA, etc)
- **MANUAL**: Run on-demand

### Actions (Workflow)
- **PUBLISH**: Post content to platforms
- **PAUSE_CAMPAIGN**: Pause campaign
- **SCALE_BUDGET**: Increase/decrease budget
- **SEND_ALERT**: Email/SMS notification
- **GENERATE_CONTENT**: Create new content
- **SEND_WEBHOOK**: Call external service

### Report Types
- **PERFORMANCE**: Campaign metrics & trends
- **COMPARATIVE**: Multi-campaign comparison
- **EXECUTIVE**: One-page summary
- **FORECAST**: Future performance predictions
- **CUSTOM**: User-defined report

---

## 🚨 Common Errors & Fixes

### Error: "NameError: name 'Dict' not found"
**Fix**: Add to top of file:
```python
from typing import Dict, List, Optional
```

### Error: "ModuleNotFoundError: No module named 'streamlit'"
**Fix**: Install dependencies:
```bash
pip install -r requirements.txt
```

### Error: "API key validation failed"
**Fix**: Check API key format:
```python
# Valid format: tco_<32 hex chars>
# Check if key starts with tco_
api_key = "tco_abc123..."
```

### Error: "Rate limit exceeded"
**Solution**: Implement retry with backoff:
```python
import time

for attempt in range(3):
    try:
        result = api_call()
        break
    except RateLimitError:
        wait_time = 2 ** attempt
        time.sleep(wait_time)
```

---

## 📞 Getting Help

### Code Documentation
```bash
# View docstring
python -c "from module import Function; help(Function)"

# Example
python -c "from copywriting_engine import CopywritingEngine; help(CopywritingEngine.generate_power_headlines)"
```

### File Navigation
```bash
# Find files mentioning "campaign"
grep -r "class Campaign" .

# Find functions
grep -r "def create_campaign" .

# Find imports
grep -r "from campaign_management import" .
```

### Check Requirements
```bash
# See all installed packages
pip list

# Check specific package version
pip show streamlit
```

---

## ✅ Pre-Commit Checklist

Before committing code:

- [ ] Code follows PEP 8 style: `black .`
- [ ] No linting errors: `flake8 .`
- [ ] Type hints added: `mypy .`
- [ ] Docstrings present for functions
- [ ] No unused imports
- [ ] Tests pass: `pytest`
- [ ] No hardcoded credentials
- [ ] Comments explain "why", not "what"

---

## 🔗 Quick Links

- **Docs**: `/docs/` folder
- **Issues**: GitHub Issues
- **API Docs**: Run `fastapi docs` at http://localhost:8000/docs
- **Tests**: `/tests/` folder
- **Config**: `config/settings.json`

---

**Last Updated**: 2024-12-15  
**Version**: 2.0.0  
**Maintainer**: @thecontent-team

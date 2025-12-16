# System Architecture - AI Content Generator Pro

## Overview Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                      Streamlit Web Interface                    │
│                          (app.py)                               │
└───────────────┬─────────────────────────────────────────────────┘
                │
    ┌───────────┴───────────┬────────────────┐
    │                       │                │
    ▼                       ▼                ▼
┌─────────────┐    ┌──────────────────┐   ┌──────────────┐
│  TrendAnalyzer     │ CreativeOptimizer│   │CampaignAnalyzer
│  • Context         │ • Hook Analysis  │   │ • CTR Predict
│  • Seasonality     │ • Emotion Score  │   │ • CPC Estimate
│  • Time awareness  │ • Clarity Score  │   │ • Quality Score
│                    │ • CTA Strength   │   │ • Audience Align
│                    │ • Platform Fit   │   │ • Scaling Advice
└─────────────┘    └──────────────────┘   └──────────────┘
    │                       │                │
    └───────────────┬───────┴────────────────┘
                    │
                    ▼
        ┌─────────────────────────┐
        │ SocialMediaGenerator    │
        │ (Orchestrator)          │
        │ • generate_post()       │
        │ • batch_generate()      │
        │ • analyze_performance() │
        │ • get_trending_topics() │
        └────────┬────────────────┘
                 │
    ┌────────────┴────────────┐
    │                         │
    ▼                         ▼
┌──────────┐         ┌───────────────┐
│  Ollama  │         │   JSON Files  │
│  LLM     │         │  (Storage)    │
│ Models   │         │               │
└──────────┘         └───────────────┘
```

## Component Interactions

### 1. **Request Flow** (Content Generation)

```
User Input
    ↓
  Topic, Platform, Tone, Audience
    ↓
SocialMediaGenerator.generate_post()
    ├── TrendAnalyzer.get_current_context()
    │   └── Returns: date, season, day, timing context
    ├── Ollama.generate()
    │   └── Returns: Generated content from LLM
    ├── CreativeOptimizer.optimize_creative()
    │   └── Scores: Hook, Emotion, Clarity, CTA, Platform Fit
    ├── CampaignAnalyzer.predict_performance()
    │   └── Predicts: CTR, CPC, Quality, Alignment, Scaling
    └── Return: Full post with all scores + recommendations
        ↓
    Display in Streamlit UI
```

### 2. **Omneky Optimization Flow**

```
Generated Content
    ↓
CreativeOptimizer
    ├── Score Hook (0-100)
    │   └── Check for power words in opening
    ├── Score Emotion (0-100)
    │   └── Count emotional triggers
    ├── Score Clarity (0-100)
    │   └── Analyze word length and simplicity
    ├── Score CTA (0-100)
    │   └── Check for action words + placement
    ├── Score Platform Fit (0-100)
    │   └── Verify content length for platform
    └── Calculate Overall Score
        └── Average of 5 components
```

### 3. **Madgicx Campaign Analysis Flow**

```
Post Content + Audience Data
    ↓
CampaignAnalyzer
    ├── Estimate CTR
    │   └── Base 2% + quality factor + audience relevance + timing
    ├── Estimate CPC
    │   └── Platform base + quality factor + saturation
    ├── Calculate Quality Score
    │   └── Omneky score + trend awareness + variation
    ├── Score Audience Alignment
    │   └── Tone match + interest overlap
    ├── Evaluate Scaling Potential
    │   └── Quality + audience size → Status + multiplier
    └── Generate Recommendations
        └── Rules-based suggestions for improvement
```

## Data Structures

### Post Object

```python
{
    'id': 0,
    'platform': 'instagram',
    'topic': 'AI Marketing',
    'content': 'Generated post text...',
    'tone': 'professional',
    'model': 'gemma:2b',
    'timestamp': '2025-12-16T10:30:00',
    
    # Context & Trends
    'context': {
        'current_date': '2025-12-16',
        'month': 'December',
        'day_of_week': 'Tuesday',
        'season': 'Winter',
        'is_weekend': False,
        'hour': 10
    },
    'hashtag_strategy': 'trending',
    'trend_aware': True,
    
    # Omneky Optimization
    'optimization_score': 87,  # Overall 0-100
    'optimization_details': {
        'hook_strength': 88,
        'emotional_appeal': 85,
        'clarity_score': 82,
        'cta_effectiveness': 90,
        'platform_fit': 85,
        'overall_score': 87
    },
    
    # Madgicx Predictions
    'performance_prediction': {
        'estimated_ctr': 3.2,  # Percentage
        'estimated_cpc': 0.38,  # Dollars
        'quality_score': 86,  # 0-100
        'audience_alignment': 87,  # Percentage
        'scaling_potential': {
            'status': 'Ready to Scale',
            'budget_multiplier': 1.5,
            'recommendation': 'Start with 1-2x budget'
        },
        'recommendations': [
            'Content is well-optimized. Ready to launch!',
            'Consider increasing ad spend to 1.5x'
        ]
    }
}
```

### Audience Object

```python
{
    'audience_size': 500000,        # Total addressable
    'interest_match': 80,            # 0-100 percentage
    'preferred_tone': 'professional', # Matching tone
    'saturation': 0.3                # 0.0-1.0 saturation level
}
```

## Class Hierarchy

```
┌──────────────────────────────────────────┐
│          SocialMediaGenerator            │
│   (Main orchestrator & entry point)      │
├──────────────────────────────────────────┤
│ - model: str                             │
│ - content_history: List[Dict]            │
│ - trend_analyzer: TrendAnalyzer          │
│ - creative_optimizer: CreativeOptimizer  │
│ - campaign_analyzer: CampaignAnalyzer    │
├──────────────────────────────────────────┤
│ + generate_post()                        │
│ + batch_generate()                       │
│ + generate_with_keywords()               │
│ + analyze_content_performance()          │
│ + get_trending_suggestions()             │
│ + save_history()                         │
│ + load_content()                         │
│ + search_content()                       │
└──────────────────────────────────────────┘
         △              △              △
         │              │              │
         │              │              │
   ┌─────────┐  ┌──────────────┐  ┌──────────────┐
   │  Trend  │  │  Creative    │  │   Campaign   │
   │ Analyzer│  │  Optimizer   │  │   Analyzer   │
   └─────────┘  └──────────────┘  └──────────────┘
```

## Module Dependencies

```
app.py (Streamlit UI)
    ├── streamlit (UI framework)
    ├── ollama (LLM interface)
    ├── json (Data handling)
    └── social_media_generator.py
            ├── ollama (LLM calls)
            ├── json (Serialization)
            ├── datetime (Timing)
            ├── TrendAnalyzer class
            ├── CreativeOptimizer class
            └── CampaignAnalyzer class
                └── SocialMediaGenerator class
```

## Processing Pipeline

### Sequential Processing (Per Post)

```
1. Input Configuration (0-1ms)
   Platform, Topic, Tone, Temperature, Audience

2. Context Generation (1-2ms)
   TrendAnalyzer → Current date/season/timing

3. Prompt Building (2-3ms)
   Incorporate trends, platform specs, tone

4. LLM Generation (2000-5000ms) ⚠️ SLOWEST STEP
   Ollama → Generated content

5. Omneky Optimization (10-50ms)
   CreativeOptimizer → 5 component scores

6. Campaign Analysis (50-100ms)
   CampaignAnalyzer → Predictions + recommendations

7. Aggregation (5-10ms)
   Combine all data into post object

8. Display (1-2ms)
   Streamlit → Render results

Total: ~2000-5200ms per post
```

### Batch Processing (Multiple Posts)

```
┌─ Post 1 ─────────────────┐  ┌─ Post 2 ────────────────┐  ┌─ Post 3 ────────────────┐
│ Context → LLM → Optimize │  │ Context → LLM → Optimize│  │ Context → LLM → Optimize│
└──────────────────────────┘  └──────────────────────────┘  └──────────────────────────┘
         ~2s                           ~2s                           ~2s
         
Total time: ~6 seconds (sequential) vs ~2 seconds (if parallelizable)
```

## Storage Architecture

### File Structure

```
content_library.json
[
  {
    "id": 0,
    "platform": "instagram",
    "topic": "AI Marketing",
    "content": "...",
    "optimization_score": 87,
    ...
  },
  {
    "id": 1,
    ...
  }
]
```

### Session State (Streamlit)

```
st.session_state
├── generator: SocialMediaGenerator instance
├── generated_posts: List of posts in current session
└── [Metrics computed from generated_posts]
    ├── total_posts
    ├── average_score
    ├── platform_distribution
    └── recent_scores
```

## Performance Characteristics

### Time Complexity

| Operation | Time | Notes |
|-----------|------|-------|
| Single Post | O(n) | ~2-5s (mostly LLM) |
| Batch (k posts) | O(k×n) | Sequential processing |
| Optimization | O(m) | m = content length (~50ms) |
| Campaign Analysis | O(1) | Constant time calculations |
| Search | O(p) | p = posts in library |

### Space Complexity

| Component | Space |
|-----------|-------|
| Generator | ~1MB |
| Post (avg) | ~5-10KB |
| History (100 posts) | ~1MB |
| Library (1000 posts) | ~10MB |

## Error Handling

```
User Request
    │
    ├─ Validation
    │   └─ Check: topic, platform, audience params
    │
    ├─ Ollama Connection
    │   └─ Retry 3x, timeout 30s
    │
    ├─ Generation
    │   └─ Catch exceptions → Show error message
    │
    ├─ Optimization
    │   └─ Graceful degradation (fallback scores)
    │
    └─ Display
        └─ JSON serialization error handling
```

## Scalability Considerations

### Current Limitations
- Single-threaded (sequential processing)
- In-memory session state (per user)
- No database (file-based JSON)
- Local LLM (single GPU/CPU)

### Scaling Strategies
1. **Parallel Processing**: Batch posts with thread pool
2. **Distributed Computing**: Multiple Ollama instances
3. **Caching**: Store optimization scores for similar content
4. **Database**: Move from JSON to PostgreSQL
5. **API**: Convert to FastAPI backend

## Integration Points

### External Services
1. **Ollama** → LLM inference
2. **Facebook/Instagram API** → Content scheduling
3. **LinkedIn API** → Post publishing
4. **Google Analytics** → Performance tracking
5. **Twitter API** → Tweet posting

### Future Integrations
- Real performance data (ActualCTR, ActualCPC)
- A/B testing framework
- Content calendar management
- Team collaboration
- Performance reporting

---

**Architecture Version**: 2.0
**Last Updated**: December 2025
**Status**: Production Ready


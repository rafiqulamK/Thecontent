"""
Lexi AI-Inspired Copywriting Engine
Advanced AI-powered copywriting suggestions and content improvement
Includes: Plagiarism detection, tone detection, readability analysis, 
content templates, grammar checking, and engagement scoring
"""

import re
import string
from collections import Counter
from typing import List, Dict, Tuple, Optional

class PlagiarismDetector:
    """Advanced plagiarism detection and originality checking"""
    
    def __init__(self):
        self.common_phrases = self._get_common_phrases()
        self.plagiarism_patterns = self._get_plagiarism_patterns()
        
    def _get_common_phrases(self) -> List[str]:
        """Common phrases to check against"""
        return [
            "in today's world", "as we all know", "it is important",
            "in conclusion", "for example", "therefore", "in addition",
            "take the time", "all things considered", "for instance",
            "on the other hand", "the fact that", "based on the idea",
            "in my humble opinion", "last but not least", "needless to say"
        ]
    
    def _get_plagiarism_patterns(self) -> Dict[str, float]:
        """Patterns that indicate potential plagiarism"""
        return {
            "excessive_passive_voice": 0.6,
            "repeated_sentence_structure": 0.5,
            "clichéd_phrases": 0.4,
            "generic_templates": 0.3
        }
    
    def detect_plagiarism(self, text: str) -> Dict:
        """Detect potential plagiarism risk"""
        score = 0
        flags = []
        
        # Check for clichéd phrases
        cliche_count = 0
        for phrase in self.common_phrases:
            if phrase.lower() in text.lower():
                cliche_count += 1
                flags.append(f"Clichéd phrase detected: '{phrase}'")
        
        # Penalize for high cliché count
        score += min(cliche_count * 2, 25)
        
        # Check sentence structure repetition
        sentences = [s.strip() for s in text.split('.') if s.strip()]
        if len(sentences) > 3:
            sentence_lengths = [len(s.split()) for s in sentences]
            if len(set(sentence_lengths)) <= 2:
                score += 15
                flags.append("Repetitive sentence structure detected")
        
        # Check passive voice percentage
        passive_count = text.lower().count(" is ") + text.lower().count(" was ")
        passive_percentage = (passive_count / max(len(sentences), 1)) * 100
        if passive_percentage > 40:
            score += 10
            flags.append(f"High passive voice usage: {passive_percentage:.1f}%")
        
        originality = max(0, 100 - score)
        return {
            "originality_score": originality,
            "plagiarism_risk": "HIGH" if score > 60 else "MEDIUM" if score > 30 else "LOW",
            "risk_score": min(score, 100),
            "issues_found": flags,
            "recommendation": self._get_plagiarism_recommendation(score)
        }
    
    def _get_plagiarism_recommendation(self, score: float) -> str:
        """Get recommendation based on plagiarism score"""
        if score > 60:
            return "Rewrite content significantly. Reduce clichés and vary sentence structure."
        elif score > 30:
            return "Minor plagiarism risk. Consider rewording some phrases and varying structure."
        else:
            return "Content appears original. Good originality score."


class ToneDetector:
    """Detect and adjust tone of content"""
    
    def __init__(self):
        self.tone_indicators = self._get_tone_indicators()
        self.tone_words = self._get_tone_words()
        
    def _get_tone_indicators(self) -> Dict[str, Dict]:
        """Indicators for different tones"""
        return {
            "professional": {
                "keywords": ["thus", "furthermore", "accordingly", "whereas", "hereby"],
                "style": "formal, technical, business-focused",
                "exclamations": 0,
                "contractions": False,
                "avg_word_length": 5.5
            },
            "casual": {
                "keywords": ["so", "like", "really", "pretty", "totally"],
                "style": "relaxed, conversational, friendly",
                "exclamations": 2,
                "contractions": True,
                "avg_word_length": 4.2
            },
            "friendly": {
                "keywords": ["hey", "awesome", "cool", "love", "happy"],
                "style": "warm, approachable, conversational",
                "exclamations": 1,
                "contractions": True,
                "avg_word_length": 4.5
            },
            "urgent": {
                "keywords": ["immediately", "urgent", "critical", "now", "must"],
                "style": "compelling, time-sensitive, action-driven",
                "exclamations": 1,
                "contractions": False,
                "avg_word_length": 4.8
            },
            "empathetic": {
                "keywords": ["understand", "feel", "care", "support", "help"],
                "style": "compassionate, understanding, supportive",
                "exclamations": 0,
                "contractions": True,
                "avg_word_length": 4.6
            }
        }
    
    def _get_tone_words(self) -> Dict[str, List[str]]:
        """Words associated with different tones"""
        return {
            "positive": ["excellent", "amazing", "wonderful", "fantastic", "outstanding"],
            "negative": ["terrible", "awful", "horrible", "disgusting", "worst"],
            "neutral": ["significant", "notable", "important", "relevant", "key"],
            "emotional": ["love", "hate", "fear", "joy", "passion"],
            "logical": ["thus", "therefore", "clearly", "evidently", "logically"]
        }
    
    def detect_tone(self, text: str) -> Dict:
        """Detect the primary tone of content"""
        tone_scores = {}
        
        for tone, indicators in self.tone_indicators.items():
            score = 0
            words = text.lower().split()
            
            # Check for tone keywords
            for keyword in indicators['keywords']:
                score += text.lower().count(keyword) * 2
            
            # Check contractions
            contractions = len(re.findall(r"\b\w+n't\b|\b\w+'[ds]\b", text))
            if indicators['contractions'] and contractions > 0:
                score += contractions
            elif not indicators['contractions'] and contractions > 0:
                score -= contractions
            
            # Check exclamation marks
            exclamation_count = text.count('!')
            ideal_exclamations = indicators['exclamations']
            score += max(0, ideal_exclamations - abs(exclamation_count - ideal_exclamations))
            
            tone_scores[tone] = max(0, score)
        
        detected_tone = max(tone_scores, key=tone_scores.get)
        return {
            "detected_tone": detected_tone,
            "tone_confidence": tone_scores[detected_tone] / (sum(tone_scores.values()) + 0.1),
            "all_tones": tone_scores,
            "tone_description": self.tone_indicators[detected_tone]['style']
        }
    
    def adjust_tone(self, text: str, target_tone: str) -> str:
        """Adjust text to match target tone"""
        adjusted = text
        
        # Simple tone adjustment (would be more sophisticated with real NLP)
        if target_tone == "professional":
            adjusted = adjusted.replace("gonna", "going to").replace("wanna", "want to")
            adjusted = adjusted.replace("yeah", "yes").replace("nope", "no")
        elif target_tone == "casual":
            adjusted = adjusted.replace("going to", "gonna").replace("want to", "wanna")
            adjusted = adjusted.replace("very", "really").replace("extremely", "super")
        
        return adjusted


class ReadabilityAnalyzer:
    """Comprehensive readability and complexity analysis"""
    
    def __init__(self):
        self.readability_formulas = self._get_formulas()
    
    def _get_formulas(self) -> Dict:
        """Different readability formulas"""
        return {
            "flesch_kincaid": "Grade level (4.0-12.0+)",
            "flesch_reading_ease": "Ease score (0-100, higher=easier)",
            "gunning_fog": "Years of education needed",
            "smog": "Years of education needed (0-18)",
            "ari": "US grade level"
        }
    
    def analyze_readability(self, text: str) -> Dict:
        """Comprehensive readability analysis"""
        sentences = [s.strip() for s in text.split('.') if s.strip()]
        words = text.split()
        
        word_count = len(words)
        sentence_count = len(sentences)
        syllable_count = self._count_syllables(text)
        
        # Flesch Reading Ease
        if sentence_count > 0 and word_count > 0:
            fre = 206.835 - 1.015 * (word_count / sentence_count) - 84.6 * (syllable_count / word_count)
            fre = max(0, min(100, fre))
        else:
            fre = 50
        
        # Flesch-Kincaid Grade Level
        fkg = 0.39 * (word_count / sentence_count) + 11.8 * (syllable_count / word_count) - 15.59
        fkg = max(0, fkg)
        
        readability_grade = self._interpret_fre(fre)
        
        return {
            "word_count": word_count,
            "sentence_count": sentence_count,
            "avg_words_per_sentence": round(word_count / max(sentence_count, 1), 1),
            "avg_syllables_per_word": round(syllable_count / max(word_count, 1), 2),
            "flesch_reading_ease": round(fre, 1),
            "flesch_kincaid_grade": round(fkg, 1),
            "readability_level": readability_grade,
            "readability_score": self._calculate_readability_score(fre, fkg),
            "improvement_suggestions": self._get_readability_suggestions(fre, fkg)
        }
    
    def _count_syllables(self, text: str) -> int:
        """Estimate syllable count"""
        syllable_count = 0
        vowels = "aeiouy"
        previous_was_vowel = False
        
        for char in text.lower():
            is_vowel = char in vowels
            if is_vowel and not previous_was_vowel:
                syllable_count += 1
            previous_was_vowel = is_vowel
        
        # Adjust for silent e
        if text.lower().endswith('e'):
            syllable_count -= 1
        
        # Adjust for ed
        if text.lower().endswith('ed'):
            syllable_count += 1
        
        return max(1, syllable_count)
    
    def _interpret_fre(self, fre: float) -> str:
        """Interpret Flesch Reading Ease score"""
        if fre >= 90:
            return "Very Easy (5th grade)"
        elif fre >= 80:
            return "Easy (6th grade)"
        elif fre >= 70:
            return "Fairly Easy (7th grade)"
        elif fre >= 60:
            return "Standard (8-9th grade)"
        elif fre >= 50:
            return "Fairly Difficult (10-12th grade)"
        elif fre >= 30:
            return "Difficult (College)"
        else:
            return "Very Difficult (College+)"
    
    def _calculate_readability_score(self, fre: float, fkg: float) -> int:
        """Calculate overall readability score (0-100)"""
        fre_normalized = fre  # Already 0-100
        fkg_normalized = max(0, 100 - (fkg * 5))  # Convert grade to 0-100
        
        return round((fre_normalized + fkg_normalized) / 2)
    
    def _get_readability_suggestions(self, fre: float, fkg: float) -> List[str]:
        """Get suggestions for improving readability"""
        suggestions = []
        
        if fkg > 12:
            suggestions.append("Content is too complex. Use shorter words and simpler sentence structures.")
        elif fkg > 10:
            suggestions.append("Consider simplifying some complex words and longer sentences.")
        elif fkg < 6 and fkg > 4:
            suggestions.append("Consider adding more sophisticated vocabulary for target audience.")
        
        if fre < 50:
            suggestions.append("Break content into shorter paragraphs and sentences.")
        elif fre > 90:
            suggestions.append("Content is very simple. Consider slightly more sophisticated vocabulary.")
        
        return suggestions


class ContentTemplates:
    """Pre-built content templates for various industries and use cases"""
    
    def __init__(self):
        self.templates = self._get_templates()
    
    def _get_templates(self) -> Dict[str, Dict]:
        """Content templates by industry"""
        return {
            "email_sales": {
                "name": "Sales Email",
                "structure": "Subject → Hook → Problem → Solution → CTA",
                "template": "Subject: [Attention-grabbing headline]\n\n[Personalized greeting],\n\n[Problem statement]. This affects [audience] by [impact].\n\nUnfortunately, [current situation problem].\n\nBut here's the good news: [Solution]. [Proof/benefit].\n\n[Call to action]\n\nBest regards,\n[Your name]"
            },
            "blog_post": {
                "name": "Blog Post",
                "structure": "Intro → 3-5 Main Points → Conclusion → CTA",
                "template": "[Hook/Story]\n\n[Problem statement]\n\nHere are [number] ways to solve this:\n\n1. [Point 1]\n   - [Explanation]\n   - [Example]\n\n2. [Point 2]\n   - [Explanation]\n   - [Example]\n\n3. [Point 3]\n   - [Explanation]\n   - [Example]\n\n[Conclusion and summary]\n\n[Call to action]"
            },
            "social_media": {
                "name": "Social Media Post",
                "structure": "Hook → Value → CTA → Hashtags",
                "template": "[Hook - attention-grabbing opening]\n\n[Value proposition - what's in it for them]\n\n[Social proof or example]\n\n[Call to action - be specific]\n\n#[Hashtag1] #[Hashtag2] #[Hashtag3]"
            },
            "product_description": {
                "name": "Product Description",
                "structure": "Feature → Benefit → Use Case → CTA",
                "template": "[Product name and brief intro]\n\nKey Features:\n• [Feature 1] - [How it benefits user]\n• [Feature 2] - [How it benefits user]\n• [Feature 3] - [How it benefits user]\n\nPerfect for [Use case 1], [Use case 2], and [Use case 3].\n\n[Why customers love it]\n\n[Call to action with urgency]"
            },
            "press_release": {
                "name": "Press Release",
                "structure": "Headline → Summary → Quote → Details → Boilerplate → Contact",
                "template": "[HEADLINE]\n\n[City, Date] - [Company] today announced [Main announcement]. [1-2 sentence summary of significance].\n\n\"[Quote from key person about impact and vision]\"\n\n[Additional details - what, why, when]\n\n[Second quote with more details]\n\nAbout [Company]\n[Company boilerplate - 2-3 sentences]\n\nMedia Contact:\n[Name]\n[Email]\n[Phone]"
            },
            "ad_copy": {
                "name": "Advertisement Copy",
                "structure": "Attention → Interest → Desire → Action",
                "template": "[Attention-grabbing headline that stops scrolling]\n\n[Hook that speaks to a specific pain point or desire]\n\n[Problem agitation - why is this important?]\n\n[Solution with specific benefits]\n\n[Social proof - testimonial, stat, or guarantee]\n\n[Urgent call to action with benefit]\n\n[Bonus or incentive]\n\n[Final CTA button]"
            }
        }
    
    def get_template(self, template_type: str) -> Dict:
        """Get a specific template"""
        return self.templates.get(template_type, {})
    
    def list_templates(self) -> List[str]:
        """List all available templates"""
        return list(self.templates.keys())
    
    def apply_template(self, template_type: str, variables: Dict) -> str:
        """Apply a template with provided variables"""
        template = self.get_template(template_type)
        if not template:
            return ""
        
        content = template.get('template', '')
        for key, value in variables.items():
            content = content.replace(f"[{key}]", str(value))
        
        return content


class CopywritingEngine:
    """Lexi AI-inspired copywriting assistant for content improvement"""
    
    def __init__(self):
        self.writing_patterns = {
            'narrative': self._get_narrative_patterns(),
            'persuasive': self._get_persuasive_patterns(),
            'technical': self._get_technical_patterns(),
            'conversational': self._get_conversational_patterns(),
            'urgent': self._get_urgent_patterns()
        }
        self.power_word_library = self._get_power_words()
        self.headline_formulas = self._get_headline_formulas()
        self.cta_variations = self._get_cta_variations()
        
    def _get_narrative_patterns(self) -> List[str]:
        """Narrative writing patterns for storytelling"""
        return [
            "The Problem-Agitate-Solve (PAS) formula",
            "Hero's Journey structure",
            "STAR (Situation-Task-Action-Result) method",
            "Customer transformation narrative",
            "Before-After-Bridge pattern"
        ]
    
    def _get_persuasive_patterns(self) -> List[str]:
        """Persuasive writing patterns"""
        return [
            "AIDA (Attention-Interest-Desire-Action)",
            "PAS (Problem-Agitate-Solve)",
            "BAB (Before-After-Bridge)",
            "4Ps (Promise-Picture-Proof-Push)",
            "Curiosity-driven copy"
        ]
    
    def _get_technical_patterns(self) -> List[str]:
        """Technical writing patterns"""
        return [
            "Feature-Benefit structure",
            "Specification-driven format",
            "Process explanation method",
            "Data-backed assertions",
            "Comparative analysis format"
        ]
    
    def _get_conversational_patterns(self) -> List[str]:
        """Conversational writing patterns"""
        return [
            "Second-person perspective (you/your)",
            "Short sentences and fragments",
            "Casual language and contractions",
            "Questions to engage reader",
            "Personal anecdotes"
        ]
    
    def _get_urgent_patterns(self) -> List[str]:
        """Urgency-driven patterns"""
        return [
            "Scarcity: Limited supply/time",
            "Exclusivity: Members only",
            "Deadline-based: Act now",
            "FOMO: Don't miss out",
            "Opportunity-focused: Don't pass up"
        ]
    
    def _get_power_words(self) -> Dict[str, List[str]]:
        """Library of power words by category"""
        return {
            'action': ['Transform', 'Revolutionize', 'Unlock', 'Master', 'Dominate', 
                      'Accelerate', 'Amplify', 'Maximize', 'Optimize', 'Automate'],
            'emotional': ['Amazing', 'Incredible', 'Stunning', 'Powerful', 'Unbelievable',
                         'Remarkable', 'Fantastic', 'Awesome', 'Incredible', 'Mind-blowing'],
            'credibility': ['Proven', 'Verified', 'Certified', 'Award-winning', 'Trusted',
                           'Guaranteed', 'Tested', 'Backed by science', 'Expert-approved', 'Results-driven'],
            'urgency': ['Now', 'Today', 'Immediately', 'Limited', 'Exclusive', 'Last chance',
                       'Don\'t wait', 'Hurry', 'Only', 'While supplies last'],
            'value': ['Free', 'Save', 'Bargain', 'Deal', 'Worth', 'Investment', 'Premium',
                     'Exclusive', 'Special', 'Valuable'],
            'social': ['Everyone', 'Trending', 'Popular', 'Viral', 'Loved', 'Favorite',
                      'Celebrity-endorsed', 'Celebrity-approved', 'Millions choose', 'Join']
        }
    
    def _get_headline_formulas(self) -> Dict[str, str]:
        """Proven headline formulas"""
        return {
            'number_benefit': '[Number] Ways to [Benefit]',
            'how_to': 'How to [Desired Result] Without [Objection]',
            'curious_question': '[Interesting Question] Here\'s the answer...',
            'statement': '[Claim] This is why...',
            'list': '[Number] [Adjective] Ways to [Benefit]',
            'promise': 'Discover [Specific Benefit]',
            'secret': 'The [Adjective] Secret to [Result]',
            'warning': '[Warning] About [Topic]',
            'comparison': '[Your Solution] vs [Alternative]: The Difference',
            'testimonial': 'How [Person] [Achievement]'
        }
    
    def _get_cta_variations(self) -> Dict[str, List[str]]:
        """CTA variations for different platforms"""
        return {
            'twitter': [
                'Click the link to learn more',
                'Retweet if you agree',
                'Reply with your thoughts',
                'Follow for daily tips',
                'Check our latest thread'
            ],
            'instagram': [
                'Tap the link in bio',
                'DM us for details',
                'Like if you agree',
                'Comment your thoughts',
                'Save this for later'
            ],
            'linkedin': [
                'Comment your thoughts below',
                'Connect with me to discuss',
                'Share this with your network',
                'Learn more in my latest post',
                'Schedule a call'
            ],
            'facebook': [
                'Click to learn more',
                'Share with your friends',
                'Comment below',
                'React if you agree',
                'Visit our website'
            ],
            'generic': [
                'Get started today',
                'Learn more',
                'Join now',
                'Subscribe',
                'Get exclusive access'
            ]
        }
    
    def improve_content(self, content: str, style: str = 'persuasive') -> Dict:
        """
        Improve existing content with suggestions
        
        Args:
            content: Original content to improve
            style: Writing style (narrative, persuasive, technical, conversational, urgent)
        
        Returns:
            Suggestions for improvement
        """
        analysis = {
            'original': content,
            'improvements': [],
            'rewritten_versions': [],
            'power_word_suggestions': [],
            'cta_suggestions': [],
            'style': style,
            'readability_score': self._calculate_readability(content),
            'engagement_score': self._calculate_engagement(content)
        }
        
        # Power word suggestions
        for category in self.power_word_library:
            missing_words = [w for w in self.power_word_library[category] 
                           if w.lower() not in content.lower()]
            if missing_words:
                analysis['power_word_suggestions'].append({
                    'category': category,
                    'suggestions': missing_words[:3]
                })
        
        # Rewrite suggestions
        analysis['rewritten_versions'] = self._generate_variations(content, style)
        
        # CTA suggestions (if not present)
        if not self._has_strong_cta(content):
            analysis['cta_suggestions'] = self._get_cta_variations()['generic'][:3]
        
        return analysis
    
    def _calculate_readability(self, content: str) -> float:
        """Calculate readability score (0-100)"""
        words = content.split()
        sentences = content.split('.')
        
        # Flesch-Kincaid-like calculation
        if len(sentences) > 0 and len(words) > 0:
            avg_sentence_length = len(words) / len(sentences)
            avg_word_length = sum(len(w) for w in words) / len(words)
            
            readability = 206.835 - (1.015 * avg_sentence_length) - (84.6 * (avg_word_length / 5))
            return max(0, min(100, readability))
        return 50
    
    def _calculate_engagement(self, content: str) -> float:
        """Calculate engagement score (0-100)"""
        score = 50
        
        # Questions boost engagement
        score += content.count('?') * 5
        
        # Power words
        for category in self.power_word_library:
            for word in self.power_word_library[category]:
                score += content.lower().count(word.lower()) * 3
        
        # Exclamation marks
        score += content.count('!') * 4
        
        # Contractions (conversational)
        contractions = ['don\'t', 'can\'t', 'won\'t', 'it\'s', 'you\'re', 'i\'m']
        score += sum(content.lower().count(c) for c in contractions) * 2
        
        return min(100, score)
    
    def _generate_variations(self, content: str, style: str) -> List[str]:
        """Generate different variations of content"""
        variations = []
        
        if style == 'persuasive':
            # Add urgency
            variations.append(f"⏰ {content} Act now!")
            
            # Add proof element
            variations.append(f"✓ {content} Proven & trusted.")
        
        elif style == 'narrative':
            # Add story hook
            variations.append(f"Once upon a time... {content}")
        
        elif style == 'conversational':
            # Make more conversational
            variations.append(f"So here's the thing: {content}")
        
        elif style == 'urgent':
            # Add urgency markers
            variations.append(f"🚨 {content} Don't miss out!")
        
        return variations[:3]
    
    def _has_strong_cta(self, content: str) -> bool:
        """Check if content has a strong call-to-action"""
        cta_indicators = ['click', 'subscribe', 'join', 'get', 'buy', 'download',
                         'sign up', 'register', 'learn more', 'discover']
        return any(cta in content.lower() for cta in cta_indicators)


class ABTestFramework:
    """Advanced A/B Testing Framework for multiple variations"""
    
    def __init__(self):
        self.tests = {}
        self.results = {}
        
    def create_test(self, test_id: str, variants: List[Dict]) -> Dict:
        """
        Create A/B test with multiple variants
        
        Args:
            test_id: Unique test identifier
            variants: List of {name, content} dicts
        
        Returns:
            Test configuration
        """
        test_config = {
            'test_id': test_id,
            'variants': variants,
            'created_at': datetime.now().isoformat(),
            'status': 'active',
            'results': {}
        }
        
        self.tests[test_id] = test_config
        return test_config
    
    def analyze_variant(self, variant: Dict, audience: Dict) -> Dict:
        """Analyze single variant performance"""
        analysis = {
            'variant_name': variant.get('name'),
            'predicted_metrics': {
                'ctr': self._predict_ctr(variant['content']),
                'cpc': self._predict_cpc(variant['content']),
                'engagement': self._predict_engagement(variant['content']),
                'conversion': self._predict_conversion(variant['content'], audience)
            },
            'strengths': self._identify_strengths(variant['content']),
            'weaknesses': self._identify_weaknesses(variant['content']),
            'recommendation': self._get_variant_recommendation(variant['content'])
        }
        return analysis
    
    def _predict_ctr(self, content: str) -> float:
        """Predict CTR based on content"""
        base = 2.0
        if len(content) < 100:
            base += 0.5
        if '?' in content:
            base += 0.3
        if any(word in content.lower() for word in ['discover', 'learn', 'see']):
            base += 0.4
        return min(10, base)
    
    def _predict_cpc(self, content: str) -> float:
        """Predict CPC based on content quality"""
        base = 0.50
        quality = len(content) / 50
        return max(0.10, base / quality)
    
    def _predict_engagement(self, content: str) -> float:
        """Predict engagement (0-100)"""
        score = 50
        score += len(content.split('?')) * 10
        score += content.count('!') * 5
        return min(100, score)
    
    def _predict_conversion(self, content: str, audience: Dict) -> float:
        """Predict conversion rate"""
        base = 2.0
        
        if 'exclusive' in content.lower():
            base += 1.0
        if 'limited' in content.lower():
            base += 0.8
        if 'free' in content.lower():
            base += 1.2
        
        return min(15, base)
    
    def _identify_strengths(self, content: str) -> List[str]:
        """Identify content strengths"""
        strengths = []
        
        if any(w in content.lower() for w in ['discover', 'transform', 'exclusive']):
            strengths.append('Strong power words')
        
        if '?' in content:
            strengths.append('Engages with questions')
        
        if any(w in content.lower() for w in ['free', 'save', 'deal']):
            strengths.append('Value proposition clear')
        
        if len(content) > 100 and len(content) < 500:
            strengths.append('Optimal length')
        
        return strengths
    
    def _identify_weaknesses(self, content: str) -> List[str]:
        """Identify content weaknesses"""
        weaknesses = []
        
        if len(content) < 50:
            weaknesses.append('Too short - needs more detail')
        
        if len(content) > 1000:
            weaknesses.append('Too long - trim unnecessary words')
        
        if not any(cta in content.lower() for cta in ['click', 'learn', 'get', 'join']):
            weaknesses.append('Missing clear call-to-action')
        
        if not any(word in content.lower() for word in ['you', 'your']):
            weaknesses.append('Lacks audience focus (use "you")')
        
        return weaknesses
    
    def _get_variant_recommendation(self, content: str) -> str:
        """Get recommendation for variant"""
        strengths = len(self._identify_strengths(content))
        weaknesses = len(self._identify_weaknesses(content))
        
        if strengths >= 3 and weaknesses == 0:
            return "🏆 Highly recommended - Run this variant"
        elif strengths >= 2:
            return "✅ Good candidate - Worth testing"
        else:
            return "⚠️ Needs improvement - Revise before testing"
    
    def compare_variants(self, variants: List[Dict]) -> Dict:
        """Compare multiple variants and rank them"""
        comparison = {
            'variants': [],
            'winner': None,
            'recommendation': None
        }
        
        for variant in variants:
            analysis = self.analyze_variant(variant, {})
            comparison['variants'].append(analysis)
        
        # Rank by predicted metrics
        ranked = sorted(comparison['variants'], 
                       key=lambda x: x['predicted_metrics']['ctr'], 
                       reverse=True)
        
        comparison['winner'] = ranked[0]['variant_name']
        comparison['recommendation'] = ranked[0]['recommendation']
        
        return comparison

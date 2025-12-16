"""
Advanced Lexi AI Features
Plagiarism detection, tone detection, readability analysis, 
content templates, and brand voice consistency
"""

from typing import List, Dict, Tuple, Optional
import re
from collections import Counter


class EngagementScorer:
    """Analyze and score content engagement potential"""
    
    def __init__(self):
        self.engagement_factors = self._get_engagement_factors()
        self.cta_effectiveness_library = self._get_cta_library()
        
    def _get_engagement_factors(self) -> Dict[str, Dict]:
        """Factors that influence engagement"""
        return {
            "questions": {
                "weight": 15,
                "description": "Number of questions to engage reader",
                "ideal_range": (1, 3),
                "pattern": r"\?"
            },
            "numbers": {
                "weight": 12,
                "description": "Specific numbers and statistics",
                "ideal_count": 2,
                "pattern": r"\d+"
            },
            "line_breaks": {
                "weight": 10,
                "description": "Proper formatting with line breaks",
                "ideal_length": 60,
                "pattern": r"\n"
            },
            "lists": {
                "weight": 12,
                "description": "Use of bullet points or lists",
                "ideal_count": 1,
                "pattern": r"(•|-|\*|[0-9]+\.)"
            },
            "power_words": {
                "weight": 15,
                "description": "Use of high-impact power words",
                "ideal_count": 3,
                "examples": ["exclusive", "proven", "guaranteed", "unique", "limited"]
            },
            "cta_strength": {
                "weight": 15,
                "description": "Clear and compelling call-to-action",
                "ideal_count": 1,
                "examples": ["click here", "learn more", "get started", "join now"]
            },
            "readability": {
                "weight": 12,
                "description": "Overall readability score",
                "ideal_score": 70,
                "pattern": None
            },
            "word_variety": {
                "weight": 9,
                "description": "Unique words vs total words",
                "ideal_ratio": 0.5,
                "pattern": None
            }
        }
    
    def _get_cta_library(self) -> Dict[str, List[str]]:
        """Effective CTAs by type"""
        return {
            "urgent": [
                "Act now - limited time offer",
                "Don't miss out, claim yours today",
                "Join thousands who already have",
                "Get started in the next 24 hours",
                "Secure your spot before it's gone"
            ],
            "curiosity": [
                "Learn the secret most don't know",
                "Discover what we found",
                "See how this works",
                "Unlock the full story",
                "Find out what you've been missing"
            ],
            "benefit_focused": [
                "Start your transformation today",
                "Get results in 30 days",
                "Achieve your goals now",
                "Unlock your potential",
                "Get the advantage"
            ],
            "action_driven": [
                "Get started today",
                "Join our community",
                "Download now",
                "Sign up free",
                "Claim your access"
            ],
            "trust_building": [
                "See results risk-free",
                "Try it for 30 days",
                "Money-back guarantee",
                "Join verified users",
                "See what our clients say"
            ]
        }
    
    def score_engagement(self, text: str) -> Dict:
        """Comprehensive engagement score"""
        scores = {}
        total_weight = 0
        weighted_sum = 0
        
        # Questions score
        question_count = len(re.findall(r"\?", text))
        ideal_min, ideal_max = self.engagement_factors["questions"]["ideal_range"]
        q_score = 100 if ideal_min <= question_count <= ideal_max else max(0, 100 - (abs(question_count - ideal_min) * 20))
        scores["questions"] = q_score
        
        # Numbers/stats score
        numbers_count = len(re.findall(r"\d+", text))
        n_score = min(100, (numbers_count / 2) * 100)
        scores["numbers"] = n_score
        
        # Line breaks score (proper formatting)
        lines = text.split('\n')
        avg_line_length = sum(len(line) for line in lines) / max(len(lines), 1)
        ideal_length = self.engagement_factors["line_breaks"]["ideal_length"]
        if avg_line_length <= ideal_length:
            lb_score = 100
        else:
            lb_score = max(0, 100 - ((avg_line_length - ideal_length) / 10))
        scores["line_breaks"] = lb_score
        
        # Lists score
        lists_count = len(re.findall(r"(•|-|\*|[0-9]+\.)", text))
        l_score = 100 if lists_count >= 1 else 50
        scores["lists"] = l_score
        
        # Power words
        power_words = ["exclusive", "proven", "guaranteed", "unique", "limited", 
                      "special", "breakthrough", "revolutionary", "transform", "ultimate"]
        power_word_count = sum(1 for word in power_words if word in text.lower())
        pw_score = min(100, (power_word_count / 3) * 100)
        scores["power_words"] = pw_score
        
        # CTA strength
        cta_keywords = ["click", "learn", "get", "start", "join", "download", "discover"]
        cta_score = 100 if any(kw in text.lower() for kw in cta_keywords) else 0
        scores["cta_strength"] = cta_score
        
        # Word variety
        words = text.lower().split()
        unique_words = len(set(words))
        word_variety = unique_words / max(len(words), 1)
        wv_score = min(100, (word_variety / 0.5) * 100)
        scores["word_variety"] = wv_score
        
        # Calculate weighted average
        for factor, score in scores.items():
            if factor in self.engagement_factors:
                weight = self.engagement_factors[factor]["weight"]
                total_weight += weight
                weighted_sum += score * weight
        
        overall_score = (weighted_sum / total_weight) if total_weight > 0 else 0
        
        return {
            "engagement_score": round(overall_score, 1),
            "component_scores": {k: round(v, 1) for k, v in scores.items()},
            "engagement_level": self._interpret_engagement_score(overall_score),
            "strengths": self._get_engagement_strengths(scores),
            "weaknesses": self._get_engagement_weaknesses(scores),
            "improvement_tips": self._get_engagement_tips(scores)
        }
    
    def _interpret_engagement_score(self, score: float) -> str:
        """Interpret engagement score"""
        if score >= 85:
            return "Highly Engaging"
        elif score >= 70:
            return "Engaging"
        elif score >= 50:
            return "Moderately Engaging"
        elif score >= 30:
            return "Low Engagement"
        else:
            return "Very Low Engagement"
    
    def _get_engagement_strengths(self, scores: Dict) -> List[str]:
        """Get engagement strengths"""
        strengths = []
        for factor, score in scores.items():
            if score >= 75:
                strengths.append(f"Strong {factor}: {score:.1f}/100")
        return strengths if strengths else ["Content has room for engagement improvement"]
    
    def _get_engagement_weaknesses(self, scores: Dict) -> List[str]:
        """Get engagement weaknesses"""
        weaknesses = []
        for factor, score in scores.items():
            if score < 50:
                weaknesses.append(f"Weak {factor}: {score:.1f}/100")
        return weaknesses if weaknesses else ["No major weaknesses detected"]
    
    def _get_engagement_tips(self, scores: Dict) -> List[str]:
        """Get specific tips to improve engagement"""
        tips = []
        
        if scores.get("questions", 0) < 50:
            tips.append("Add 1-2 questions to engage readers")
        if scores.get("numbers", 0) < 50:
            tips.append("Include specific numbers, statistics, or data")
        if scores.get("line_breaks", 0) < 50:
            tips.append("Break content into shorter paragraphs")
        if scores.get("lists", 0) < 50:
            tips.append("Use bullet points or numbered lists")
        if scores.get("power_words", 0) < 50:
            tips.append("Add more power words like 'exclusive', 'proven', 'guaranteed'")
        if scores.get("cta_strength", 0) < 50:
            tips.append("Include a clear call-to-action")
        if scores.get("word_variety", 0) < 50:
            tips.append("Use more varied vocabulary")
        
        return tips if tips else ["Content is engaging - maintain current quality"]
    
    def recommend_cta(self, content: str, cta_type: str = "action_driven") -> str:
        """Recommend a CTA based on content and type"""
        import random
        if cta_type in self.cta_effectiveness_library:
            return random.choice(self.cta_effectiveness_library[cta_type])
        return random.choice(self.cta_effectiveness_library["action_driven"])


class BrandVoiceConsistency:
    """Ensure content maintains consistent brand voice"""
    
    def __init__(self):
        self.brand_attributes = {}
        self.voice_guidelines = self._get_voice_guidelines()
    
    def _get_voice_guidelines(self) -> Dict[str, Dict]:
        """Standard brand voice profiles"""
        return {
            "corporate": {
                "tone": "professional, formal, authoritative",
                "vocabulary": "sophisticated, technical, industry-specific",
                "contractions": False,
                "exclamations": 0,
                "sentence_length": "long, complex",
                "examples": ["we are committed", "our solutions", "industry leader"],
                "avoid": ["casual slang", "excessive punctuation", "overly simple language"]
            },
            "startup": {
                "tone": "innovative, energetic, approachable",
                "vocabulary": "modern, accessible, trend-aware",
                "contractions": True,
                "exclamations": 1,
                "sentence_length": "medium, varied",
                "examples": ["we're disrupting", "let's build", "game-changing"],
                "avoid": ["overly formal", "corporate jargon", "outdated language"]
            },
            "friendly": {
                "tone": "warm, conversational, supportive",
                "vocabulary": "simple, relatable, everyday",
                "contractions": True,
                "exclamations": 2,
                "sentence_length": "short, punchy",
                "examples": ["we love helping", "you've got this", "let's connect"],
                "avoid": ["technical jargon", "cold language", "formal structure"]
            },
            "luxury": {
                "tone": "exclusive, sophisticated, aspirational",
                "vocabulary": "elegant, refined, distinctive",
                "contractions": False,
                "exclamations": 0,
                "sentence_length": "varied, flowing",
                "examples": ["exceptional quality", "curated experience", "timeless elegance"],
                "avoid": ["casual language", "common clichés", "mass-market appeal"]
            },
            "educational": {
                "tone": "informative, clear, authoritative",
                "vocabulary": "precise, explanatory, structured",
                "contractions": Moderate,
                "exclamations": 0,
                "sentence_length": "medium, logical",
                "examples": ["research shows", "here's how", "understanding"],
                "avoid": ["overly casual", "unsupported claims", "vague language"]
            }
        }
    
    def set_brand_attributes(self, voice_type: str, custom_rules: Optional[Dict] = None):
        """Set brand voice attributes"""
        if voice_type in self.voice_guidelines:
            self.brand_attributes = self.voice_guidelines[voice_type].copy()
            if custom_rules:
                self.brand_attributes.update(custom_rules)
    
    def analyze_brand_consistency(self, text: str) -> Dict:
        """Analyze how well content matches brand voice"""
        if not self.brand_attributes:
            return {"error": "Brand attributes not set. Use set_brand_attributes() first."}
        
        consistency_scores = {}
        issues = []
        
        # Check tone keywords
        tone_keywords = self.brand_attributes.get("examples", [])
        tone_match = sum(1 for kw in tone_keywords if kw.lower() in text.lower())
        tone_score = min(100, (tone_match / len(tone_keywords) * 100) if tone_keywords else 50)
        consistency_scores["tone_alignment"] = tone_score
        
        # Check contractions
        contractions_count = len(re.findall(r"\b\w+n't\b|\b\w+'[ds]\b", text))
        should_have = self.brand_attributes.get("contractions", True)
        if should_have and contractions_count == 0:
            consistency_scores["contraction_style"] = 30
            issues.append("Brand voice uses contractions, but none found in content")
        elif not should_have and contractions_count > 0:
            consistency_scores["contraction_style"] = 40
            issues.append(f"Brand voice avoids contractions, but {contractions_count} found")
        else:
            consistency_scores["contraction_style"] = 100
        
        # Check exclamation marks
        exclamation_count = text.count('!')
        ideal_exclamations = self.brand_attributes.get("exclamations", 1)
        if exclamation_count <= ideal_exclamations + 1:
            consistency_scores["exclamation_usage"] = 100
        else:
            consistency_scores["exclamation_usage"] = max(0, 100 - (exclamation_count * 15))
            issues.append(f"Too many exclamation marks ({exclamation_count}) for brand voice")
        
        # Check avoided words
        avoided_words = self.brand_attributes.get("avoid", [])
        avoided_count = sum(1 for word in avoided_words if word.lower() in text.lower())
        if avoided_count > 0:
            consistency_scores["vocabulary_fit"] = max(0, 100 - (avoided_count * 20))
            for word in avoided_words:
                if word.lower() in text.lower():
                    issues.append(f"Avoided term detected: '{word}'")
        else:
            consistency_scores["vocabulary_fit"] = 100
        
        # Calculate overall consistency
        overall_score = sum(consistency_scores.values()) / len(consistency_scores) if consistency_scores else 50
        
        return {
            "overall_consistency_score": round(overall_score, 1),
            "component_scores": {k: round(v, 1) for k, v in consistency_scores.items()},
            "consistency_level": self._interpret_consistency(overall_score),
            "issues": issues,
            "brand_attributes": self.brand_attributes.copy()
        }
    
    def _interpret_consistency(self, score: float) -> str:
        """Interpret brand consistency score"""
        if score >= 85:
            return "Highly Consistent"
        elif score >= 70:
            return "Consistent"
        elif score >= 50:
            return "Moderately Consistent"
        elif score >= 30:
            return "Inconsistent"
        else:
            return "Very Inconsistent"
    
    def adjust_for_brand_voice(self, text: str) -> str:
        """Adjust text to match brand voice"""
        if not self.brand_attributes:
            return text
        
        adjusted = text
        
        # Adjust contractions
        if not self.brand_attributes.get("contractions", True):
            adjusted = adjusted.replace("'t", " not")
            adjusted = adjusted.replace("'ve", " have")
            adjusted = adjusted.replace("'d", " would")
        
        # Replace avoided words with suggestions
        avoided = self.brand_attributes.get("avoid", [])
        replacements = {
            "casual slang": "professional language",
            "jargon": "clear explanation",
            "outdated": "modern",
        }
        
        for word, replacement in replacements.items():
            if word in adjusted.lower():
                adjusted = adjusted.replace(word, replacement)
        
        return adjusted


class GrammarChecker:
    """Basic grammar and style checking"""
    
    def __init__(self):
        self.common_errors = self._get_common_errors()
        self.style_issues = self._get_style_issues()
    
    def _get_common_errors(self) -> Dict[str, Dict]:
        """Common grammar errors"""
        return {
            "its_vs_it's": {
                "pattern": r"\bits\b",
                "context": "possessive",
                "suggestion": "Check if 'it is' contraction needed"
            },
            "their_vs_there": {
                "pattern": r"\btheir\b",
                "context": "location",
                "suggestion": "Use 'there' for location, 'their' for possession"
            },
            "double_spaces": {
                "pattern": r"  +",
                "suggestion": "Replace double spaces with single space"
            },
            "comma_splice": {
                "pattern": r"[^,]\s*,\s*[^,]",
                "suggestion": "Check comma usage in compound sentences"
            }
        }
    
    def _get_style_issues(self) -> List[str]:
        """Common style issues to avoid"""
        return [
            "Starting multiple sentences with 'The'",
            "Using passive voice excessively",
            "Repeating the same word in consecutive sentences",
            "Using 'very' or 'really' (use stronger words)",
            "Run-on sentences (> 25 words)",
            "Unclear pronoun references",
            "Missing punctuation at end of sentences"
        ]
    
    def check_grammar(self, text: str) -> Dict:
        """Check for grammar and style issues"""
        issues = []
        suggestions = []
        
        sentences = [s.strip() for s in text.split('.') if s.strip()]
        
        # Check for run-on sentences
        long_sentences = [s for s in sentences if len(s.split()) > 25]
        if long_sentences:
            issues.append(f"Found {len(long_sentences)} run-on sentence(s)")
            suggestions.append("Break long sentences into shorter ones for clarity")
        
        # Check for repeated words
        words = text.lower().split()
        word_freq = Counter(words)
        repeated = [(w, c) for w, c in word_freq.items() if c > 3 and len(w) > 4]
        if repeated:
            for word, count in repeated[:3]:
                issues.append(f"Word '{word}' repeated {count} times")
        
        # Check for passive voice
        passive_indicators = text.lower().count(" is ") + text.lower().count(" was ")
        if passive_indicators > len(sentences) / 2:
            issues.append("High use of passive voice")
            suggestions.append("Use active voice for more engaging content")
        
        return {
            "issues_found": len(issues),
            "issues": issues,
            "suggestions": suggestions,
            "score": max(0, 100 - len(issues) * 10)
        }

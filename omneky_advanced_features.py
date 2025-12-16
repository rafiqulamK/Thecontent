"""
Advanced Omneky Features
Multivariate testing, performance benchmarking, creative variations,
and advanced AI-powered creative optimization
"""

from typing import List, Dict, Tuple, Optional
import random
from datetime import datetime, timedelta


class MultiVariateTestingFramework:
    """Advanced A/B/N testing framework (Omneky-style)"""
    
    def __init__(self):
        self.active_tests = {}
        self.test_results = {}
        self.statistical_confidence = 0.95
    
    def create_multivariate_test(
        self,
        test_name: str,
        variants: Dict[str, str],
        hypothesis: str = ""
    ) -> Dict:
        """Create a multivariate test with multiple variants"""
        
        if len(variants) < 2 or len(variants) > 5:
            return {"error": "Tests must have 2-5 variants"}
        
        test = {
            "id": f"test_{int(datetime.now().timestamp())}",
            "name": test_name,
            "hypothesis": hypothesis,
            "variants": variants,
            "created_at": datetime.now().isoformat(),
            "status": "active",
            "traffic_allocation": self._allocate_traffic(len(variants)),
            "minimum_sample_size": self._calculate_min_sample(len(variants)),
            "expected_duration_days": self._estimate_duration(len(variants))
        }
        
        self.active_tests[test["id"]] = test
        return test
    
    def _allocate_traffic(self, num_variants: int) -> Dict[int, int]:
        """Allocate traffic evenly across variants"""
        allocation = {}
        percentage_per = 100 // num_variants
        for i in range(num_variants):
            allocation[i] = percentage_per
        # Handle rounding
        allocation[0] += 100 - sum(allocation.values())
        return allocation
    
    def _calculate_min_sample(self, num_variants: int) -> int:
        """Calculate minimum sample size needed for statistical significance"""
        base_sample = 385  # For 95% confidence, 5% margin of error
        return base_sample * num_variants
    
    def _estimate_duration(self, num_variants: int) -> float:
        """Estimate test duration in days"""
        base_duration = 14
        return base_duration + (num_variants - 2) * 3
    
    def record_variant_performance(
        self,
        test_id: str,
        variant_index: int,
        impressions: int,
        clicks: int,
        conversions: int,
        spend: float = 0
    ) -> Dict:
        """Record performance data for a variant"""
        
        if test_id not in self.active_tests:
            return {"error": "Test not found"}
        
        test = self.active_tests[test_id]
        if variant_index >= len(test["variants"]):
            return {"error": "Invalid variant index"}
        
        if test_id not in self.test_results:
            self.test_results[test_id] = {}
        
        # Calculate metrics
        ctr = (clicks / impressions * 100) if impressions > 0 else 0
        cvr = (conversions / clicks * 100) if clicks > 0 else 0
        cpc = (spend / clicks) if clicks > 0 else 0
        cpa = (spend / conversions) if conversions > 0 else 0
        roas = (conversions * 100 / spend) if spend > 0 else 0
        
        variant_data = {
            "variant_index": variant_index,
            "variant_name": list(test["variants"].keys())[variant_index],
            "impressions": impressions,
            "clicks": clicks,
            "conversions": conversions,
            "spend": spend,
            "ctr": round(ctr, 2),
            "cvr": round(cvr, 2),
            "cpc": round(cpc, 3),
            "cpa": round(cpa, 2),
            "roas": round(roas, 2),
            "efficiency_score": self._calculate_efficiency(ctr, cvr, cpa)
        }
        
        self.test_results[test_id][variant_index] = variant_data
        return variant_data
    
    def _calculate_efficiency(self, ctr: float, cvr: float, cpa: float) -> int:
        """Calculate overall variant efficiency (0-100)"""
        ctr_score = min(100, ctr * 2)
        cvr_score = min(100, cvr * 5)
        cpa_score = 100 - min(100, cpa * 2)
        
        return int((ctr_score + cvr_score + cpa_score) / 3)
    
    def get_test_results(self, test_id: str) -> Dict:
        """Get comprehensive test results with winner recommendation"""
        if test_id not in self.active_tests:
            return {"error": "Test not found"}
        
        test = self.active_tests[test_id]
        results = self.test_results.get(test_id, {})
        
        if not results:
            return {
                "test_id": test_id,
                "test_name": test["name"],
                "status": "no_data",
                "message": "No performance data recorded yet"
            }
        
        # Calculate statistical significance
        variant_results = list(results.values())
        winner_data = self._determine_winner(variant_results)
        
        return {
            "test_id": test_id,
            "test_name": test["name"],
            "hypothesis": test["hypothesis"],
            "variants_tested": len(results),
            "variant_results": variant_results,
            "winner": winner_data["winner"],
            "winner_lift": winner_data["lift"],
            "statistical_significance": winner_data["significance"],
            "confidence_level": f"{self.statistical_confidence * 100}%",
            "recommendation": winner_data["recommendation"]
        }
    
    def _determine_winner(self, results: List[Dict]) -> Dict:
        """Determine winning variant with statistical analysis"""
        if not results:
            return {"winner": None, "lift": 0, "significance": "insufficient_data"}
        
        # Simple winner determination by conversion rate
        winner = max(results, key=lambda x: x.get("cvr", 0))
        
        if len(results) < 2:
            return {
                "winner": winner,
                "lift": 0,
                "significance": "need_comparison",
                "recommendation": "Need at least 2 variants for comparison"
            }
        
        # Calculate lift vs control (usually first variant)
        control = results[0]
        control_cvr = control.get("cvr", 0)
        winner_cvr = winner.get("cvr", 0)
        
        if control_cvr > 0:
            lift = ((winner_cvr - control_cvr) / control_cvr) * 100
        else:
            lift = 0
        
        # Determine if statistically significant (simplified)
        significance = "probable" if lift > 15 else "possible" if lift > 5 else "insufficient"
        
        recommendation = self._get_test_recommendation(winner, lift, significance)
        
        return {
            "winner": winner.get("variant_name"),
            "lift": f"{lift:+.1f}%",
            "significance": significance,
            "recommendation": recommendation
        }
    
    def _get_test_recommendation(self, winner: Dict, lift: float, significance: str) -> str:
        """Get recommendation based on test results"""
        if significance == "insufficient":
            return "Continue testing to reach statistical significance"
        elif lift > 25:
            return "Winner shows significant improvement. Recommend scaling this variant."
        elif lift > 10:
            return "Winner shows notable improvement. Consider rolling out gradually."
        elif lift > 0:
            return "Winner shows slight improvement. Monitor performance before deciding."
        else:
            return "No clear winner. Continue testing or investigate other variables."


class CreativeVariationGenerator:
    """Generate multiple creative variations for testing"""
    
    def __init__(self):
        self.variation_frameworks = self._get_variation_frameworks()
        self.creative_elements = self._get_creative_elements()
    
    def _get_variation_frameworks(self) -> Dict[str, List[str]]:
        """Different creative variation approaches"""
        return {
            "headline_variations": [
                "question_based",
                "benefit_focused",
                "curiosity_driven",
                "urgency_based",
                "stat_based",
                "how_to",
                "comparison"
            ],
            "image_variations": [
                "product_focused",
                "lifestyle",
                "problem_agitation",
                "solution_focused",
                "customer_testimonial",
                "before_after",
                "minimalist"
            ],
            "cta_variations": [
                "action_driven",
                "benefit_focused",
                "urgency_driven",
                "curiosity_driven",
                "value_focused",
                "risk_reversal",
                "social_proof"
            ],
            "copy_variations": [
                "problem_solution",
                "storytelling",
                "feature_benefit",
                "social_proof",
                "emotional_appeal",
                "logical_reasoning",
                "urgency_scarcity"
            ]
        }
    
    def _get_creative_elements(self) -> Dict[str, List[str]]:
        """Creative elements for variation"""
        return {
            "headlines": [
                "The Ultimate Guide to {topic}",
                "How to {action} {object} {result}",
                "{number} {adjective} Ways to {action}",
                "Discover the Secret of {topic}",
                "What {audience} Don't Know About {topic}",
                "{adjective} {noun}: The Complete {topic}",
                "Stop Wasting {resource} on {problem}"
            ],
            "ctas": [
                "Get Started Now",
                "Learn More Today",
                "Claim Your {offer}",
                "Join {number} Happy {noun}",
                "See Results in {timeframe}",
                "Start Your {journey} Now",
                "Access {resource} Free"
            ],
            "social_proof": [
                "Join {number}+ customers",
                "Trusted by {company} professionals",
                "Rated {rating}/5 by {count} users",
                "{percent}% satisfaction guarantee",
                "Used by leading {industry} brands"
            ]
        }
    
    def generate_headline_variations(
        self,
        topic: str,
        variation_type: str = "all"
    ) -> Dict[str, List[str]]:
        """Generate headline variations"""
        variations = {}
        
        if variation_type == "all":
            types = self.variation_frameworks["headline_variations"]
        else:
            types = [variation_type]
        
        templates = {
            "question_based": f"Are You Making These {topic} Mistakes?",
            "benefit_focused": f"How to Achieve Better {topic} Results",
            "curiosity_driven": f"The {topic} Secret Nobody Talks About",
            "urgency_based": f"Don't Wait: Master {topic} Today",
            "stat_based": f"95% of People Don't Know This About {topic}",
            "how_to": f"How to {topic}: A Step-by-Step Guide",
            "comparison": f"{topic} vs. Traditional Methods: Which Wins?"
        }
        
        for htype in types:
            variations[htype] = [templates.get(htype, f"Discover {topic}")]
        
        return variations
    
    def generate_cta_variations(self, offer: str = "offer") -> List[str]:
        """Generate call-to-action variations"""
        cta_templates = [
            f"Get {offer} Now",
            f"Claim Your {offer}",
            f"Start {offer} Free",
            f"Learn More About {offer}",
            f"Get Instant Access",
            f"Join Today",
            f"Limited Spots Available"
        ]
        return cta_templates
    
    def generate_copy_variations(self, product: str) -> Dict[str, str]:
        """Generate body copy variations"""
        return {
            "problem_solution": f"Most people struggle with {product}. Our solution makes it easy.",
            "storytelling": f"One founder discovered the perfect {product}. Now it's available to you.",
            "feature_benefit": f"{product} features cutting-edge technology that saves you time and money.",
            "social_proof": f"Thousands of users trust {product}. Join them today.",
            "emotional_appeal": f"You deserve the best {product}. That's why we created ours.",
            "logical_reasoning": f"Scientifically proven: {product} delivers results.",
            "urgency_scarcity": f"Limited availability: {product} is in high demand. Secure yours now."
        }
    
    def create_variation_set(
        self,
        product_name: str,
        topic: str,
        count: int = 3
    ) -> List[Dict]:
        """Create a complete set of variations for testing"""
        if count < 2 or count > 5:
            return []
        
        variations = []
        headlines = self.generate_headline_variations(topic)
        ctas = self.generate_cta_variations(product_name)
        copy = self.generate_copy_variations(product_name)
        
        for i in range(count):
            variation = {
                "id": f"var_{i+1}",
                "name": f"Variation {i+1}",
                "headline": list(headlines.values())[i % len(headlines)][0],
                "body_copy": list(copy.values())[i % len(copy)],
                "cta": ctas[i % len(ctas)],
                "testing_objective": self._get_test_objective(i)
            }
            variations.append(variation)
        
        return variations
    
    def _get_test_objective(self, index: int) -> str:
        """Get testing objective for this variation"""
        objectives = [
            "Test emotional vs. logical appeal",
            "Test urgency vs. benefit focus",
            "Test simple vs. detailed copy",
            "Test question-based vs. statement headlines",
            "Test social proof effectiveness"
        ]
        return objectives[index % len(objectives)]


class PerformanceBenchmarking:
    """Industry benchmarking and competitive analysis"""
    
    def __init__(self):
        self.industry_benchmarks = self._get_industry_benchmarks()
        self.platform_benchmarks = self._get_platform_benchmarks()
    
    def _get_industry_benchmarks(self) -> Dict[str, Dict]:
        """Industry average benchmarks"""
        return {
            "ecommerce": {
                "avg_ctr": 1.5,
                "avg_cvr": 2.5,
                "avg_cpc": 0.75,
                "avg_cpa": 30,
                "avg_roas": 3.5
            },
            "saas": {
                "avg_ctr": 1.2,
                "avg_cvr": 3.0,
                "avg_cpc": 1.50,
                "avg_cpa": 50,
                "avg_roas": 4.0
            },
            "lead_generation": {
                "avg_ctr": 1.8,
                "avg_cvr": 5.0,
                "avg_cpc": 0.50,
                "avg_cpa": 25,
                "avg_roas": 2.5
            },
            "retail": {
                "avg_ctr": 1.4,
                "avg_cvr": 2.0,
                "avg_cpc": 0.60,
                "avg_cpa": 40,
                "avg_roas": 3.0
            }
        }
    
    def _get_platform_benchmarks(self) -> Dict[str, Dict]:
        """Platform-specific benchmarks"""
        return {
            "facebook": {
                "avg_ctr": 1.1,
                "avg_cpc": 0.70,
                "avg_frequency": 2.5
            },
            "instagram": {
                "avg_ctr": 1.4,
                "avg_cpc": 0.80,
                "avg_frequency": 2.0
            },
            "google": {
                "avg_ctr": 2.5,
                "avg_cpc": 1.50,
                "avg_quality_score": 7
            },
            "linkedin": {
                "avg_ctr": 0.8,
                "avg_cpc": 3.50,
                "avg_cpa": 75
            }
        }
    
    def compare_to_benchmarks(
        self,
        actual_metrics: Dict,
        industry: str
    ) -> Dict:
        """Compare actual metrics to industry benchmarks"""
        if industry not in self.industry_benchmarks:
            return {"error": f"Industry '{industry}' not found"}
        
        benchmarks = self.industry_benchmarks[industry]
        comparison = {}
        
        for metric, benchmark_value in benchmarks.items():
            if metric in actual_metrics:
                actual_value = actual_metrics[metric]
                variance = ((actual_value - benchmark_value) / benchmark_value) * 100
                
                comparison[metric] = {
                    "actual": actual_value,
                    "benchmark": benchmark_value,
                    "variance": f"{variance:+.1f}%",
                    "performance": self._interpret_variance(metric, variance)
                }
        
        overall_score = self._calculate_benchmark_score(comparison)
        
        return {
            "industry": industry,
            "metrics_comparison": comparison,
            "overall_performance_vs_benchmark": overall_score,
            "recommendations": self._get_benchmark_recommendations(comparison)
        }
    
    def _interpret_variance(self, metric: str, variance: float) -> str:
        """Interpret variance from benchmark"""
        if metric.startswith("ctr") or metric.startswith("cvr"):
            # Higher is better for CTR/CVR
            if variance > 20:
                return "Excellent"
            elif variance > 0:
                return "Above Average"
            elif variance > -20:
                return "Below Average"
            else:
                return "Poor"
        else:
            # Lower is better for CPC/CPA
            if variance < -20:
                return "Excellent"
            elif variance < 0:
                return "Above Average"
            elif variance < 20:
                return "Below Average"
            else:
                return "Poor"
    
    def _calculate_benchmark_score(self, comparison: Dict) -> str:
        """Calculate overall performance score"""
        scores = []
        for metric, data in comparison.items():
            performance = data["performance"]
            score = {
                "Excellent": 95,
                "Above Average": 75,
                "Below Average": 50,
                "Poor": 25
            }.get(performance, 50)
            scores.append(score)
        
        avg_score = sum(scores) / len(scores) if scores else 50
        
        if avg_score >= 80:
            return "Excellent (Top 20% performers)"
        elif avg_score >= 60:
            return "Above Average"
        elif avg_score >= 40:
            return "Below Average"
        else:
            return "Poor (Needs improvement)"
    
    def _get_benchmark_recommendations(self, comparison: Dict) -> List[str]:
        """Get recommendations based on benchmark comparison"""
        recommendations = []
        
        for metric, data in comparison.items():
            if data["performance"] in ["Below Average", "Poor"]:
                if "ctr" in metric:
                    recommendations.append("Improve ad copy and creative to increase CTR")
                elif "cvr" in metric:
                    recommendations.append("Optimize landing page and conversion flow")
                elif "cpc" in metric:
                    recommendations.append("Improve ad quality scores and relevance")
                elif "cpa" in metric:
                    recommendations.append("Refine audience targeting and bidding strategy")
        
        return recommendations if recommendations else ["Performance is on track with benchmarks"]


class CreativeFatigueDetector:
    """Monitor and detect creative fatigue"""
    
    def __init__(self):
        self.fatigue_thresholds = self._get_fatigue_thresholds()
    
    def _get_fatigue_thresholds(self) -> Dict[str, Dict]:
        """Thresholds for detecting creative fatigue"""
        return {
            "frequency_cap": {
                "warning_threshold": 5,
                "critical_threshold": 10,
                "metric": "times shown to same user"
            },
            "ctr_decline": {
                "warning_threshold": 20,
                "critical_threshold": 40,
                "metric": "percent decrease from initial CTR"
            },
            "cvr_decline": {
                "warning_threshold": 15,
                "critical_threshold": 30,
                "metric": "percent decrease from initial CVR"
            },
            "cost_increase": {
                "warning_threshold": 25,
                "critical_threshold": 50,
                "metric": "percent increase in CPC/CPA"
            }
        }
    
    def detect_fatigue(self, metrics_history: List[Dict]) -> Dict:
        """Detect creative fatigue based on metrics over time"""
        if len(metrics_history) < 2:
            return {"status": "insufficient_data", "message": "Need at least 2 data points"}
        
        initial_metrics = metrics_history[0]
        current_metrics = metrics_history[-1]
        
        fatigue_indicators = {
            "ctr_decline": self._calculate_decline(initial_metrics.get("ctr", 0), current_metrics.get("ctr", 0)),
            "cvr_decline": self._calculate_decline(initial_metrics.get("cvr", 0), current_metrics.get("cvr", 0)),
            "cost_increase": self._calculate_increase(initial_metrics.get("cpc", 0), current_metrics.get("cpc", 0)),
            "frequency_fatigue": current_metrics.get("avg_frequency", 0)
        }
        
        fatigue_level = self._determine_fatigue_level(fatigue_indicators)
        
        return {
            "fatigue_level": fatigue_level,
            "indicators": fatigue_indicators,
            "recommendation": self._get_fatigue_recommendation(fatigue_level, fatigue_indicators),
            "suggested_actions": self._get_fatigue_actions(fatigue_level)
        }
    
    def _calculate_decline(self, initial: float, current: float) -> float:
        """Calculate percent decline"""
        if initial == 0:
            return 0
        return ((initial - current) / initial) * 100
    
    def _calculate_increase(self, initial: float, current: float) -> float:
        """Calculate percent increase"""
        if initial == 0:
            return 0
        return ((current - initial) / initial) * 100
    
    def _determine_fatigue_level(self, indicators: Dict) -> str:
        """Determine overall fatigue level"""
        severity_score = 0
        
        if indicators["ctr_decline"] > 20:
            severity_score += 2
        if indicators["cvr_decline"] > 15:
            severity_score += 2
        if indicators["cost_increase"] > 25:
            severity_score += 2
        if indicators["frequency_fatigue"] > 5:
            severity_score += 2
        
        if severity_score >= 6:
            return "Critical"
        elif severity_score >= 4:
            return "High"
        elif severity_score >= 2:
            return "Moderate"
        else:
            return "Low"
    
    def _get_fatigue_recommendation(self, fatigue_level: str, indicators: Dict) -> str:
        """Get recommendation based on fatigue level"""
        if fatigue_level == "Critical":
            return "Immediately refresh creative. Current ads are severely fatigued and losing effectiveness."
        elif fatigue_level == "High":
            return "Urgently create new creatives. Existing ads are showing significant fatigue signs."
        elif fatigue_level == "Moderate":
            return "Plan creative refresh soon. Early signs of fatigue detected."
        else:
            return "Current creatives performing well. Monitor for fatigue signs."
    
    def _get_fatigue_actions(self, fatigue_level: str) -> List[str]:
        """Get specific actions to combat fatigue"""
        if fatigue_level == "Critical":
            return [
                "Pause underperforming creatives immediately",
                "Increase frequency cap to reduce exposure",
                "Create 3-5 new ad variations for testing",
                "Rotate new creatives into campaigns",
                "Analyze top-performing elements from original ads"
            ]
        elif fatigue_level == "High":
            return [
                "Reduce budget allocation to fatigued creatives",
                "Create new creative variations with fresh angles",
                "Test different messaging and visuals",
                "Implement stricter frequency caps",
                "Monitor metrics closely for improvement"
            ]
        elif fatigue_level == "Moderate":
            return [
                "Prepare new creative variations",
                "Begin A/B testing new concepts",
                "Monitor frequency metrics",
                "Plan creative refresh schedule",
                "Document what's working for future reference"
            ]
        else:
            return [
                "Continue monitoring creative performance",
                "Maintain current successful ad creatives",
                "Plan for periodic creative refreshes",
                "Test variations to optimize further"
            ]

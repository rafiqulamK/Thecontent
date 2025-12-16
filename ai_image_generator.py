"""
AI Image Generation & Creative Assets System
Integration with DALL-E, Midjourney, Stable Diffusion
"""

from typing import Dict, List, Optional, Tuple
from enum import Enum
from datetime import datetime
import hashlib

class ImageModel(Enum):
    """Available image generation models"""
    DALL_E_3 = "dall-e-3"
    MIDJOURNEY = "midjourney"
    STABLE_DIFFUSION = "stable-diffusion"
    LEONARDO = "leonardo"


class ImageStyle(Enum):
    """Image style presets"""
    PHOTOREALISTIC = "photorealistic"
    ILLUSTRATION = "illustration"
    CARTOON = "cartoon"
    MINIMALIST = "minimalist"
    CINEMATIC = "cinematic"
    WATERCOLOR = "watercolor"
    ABSTRACT = "abstract"
    VINTAGE = "vintage"


@staticmethod
def build_prompt_from_brief(brief: Dict) -> str:
    """Build image generation prompt from content brief"""
    product = brief.get('product', '')
    tone = brief.get('tone', 'professional')
    style = brief.get('style', 'modern')
    target_audience = brief.get('target_audience', '')
    key_message = brief.get('key_message', '')
    
    prompt = f"""
    Generate {style} {ImageStyle.PHOTOREALISTIC.value} image:
    Product: {product}
    Tone: {tone}
    Key Message: {key_message}
    Target Audience: {target_audience}
    High quality, professional, trending on ArtStation
    """
    
    return prompt.strip()


class AIImageGenerator:
    """Generate images using AI models"""
    
    def __init__(self):
        self.images_generated = 0
        self.credits_used = 0
        self.generation_history: List[Dict] = []
    
    def generate_image(self, prompt: str, model: ImageModel = ImageModel.DALL_E_3,
                       style: ImageStyle = ImageStyle.PHOTOREALISTIC, quantity: int = 1) -> List[Dict]:
        """Generate images from text prompt"""
        results = []
        
        for i in range(quantity):
            result = {
                'image_id': self._generate_id(prompt),
                'prompt': prompt,
                'model': model.value,
                'style': style.value,
                'generated_at': datetime.now().isoformat(),
                'status': 'completed',
                'url': f"https://images.example.com/{self._generate_id(prompt)}-{i}.png",
                'metadata': {
                    'size': '1024x1024',
                    'quality': 'high',
                    'seed': self._generate_seed(prompt, i)
                }
            }
            
            results.append(result)
            self.images_generated += 1
            self.credits_used += self._get_credits_for_model(model)
            self.generation_history.append(result)
        
        return results
    
    def generate_variations(self, image_id: str, variations: int = 3) -> List[Dict]:
        """Generate variations of existing image"""
        results = []
        
        for i in range(variations):
            result = {
                'parent_image_id': image_id,
                'variation_id': f"var_{image_id}_{i}",
                'generated_at': datetime.now().isoformat(),
                'url': f"https://images.example.com/var_{image_id}_{i}.png",
                'variation_type': ['color', 'composition', 'style'][i % 3]
            }
            results.append(result)
            self.images_generated += 1
        
        return results
    
    def upscale_image(self, image_url: str, scale_factor: int = 4) -> Dict:
        """Upscale image resolution"""
        return {
            'original_url': image_url,
            'upscaled_url': f"https://images.example.com/upscaled_{hashlib.md5(image_url.encode()).hexdigest()}.png",
            'scale_factor': f"{scale_factor}x",
            'upscaled_at': datetime.now().isoformat()
        }
    
    def edit_image(self, image_url: str, edit_description: str) -> Dict:
        """Edit image using AI"""
        return {
            'original_url': image_url,
            'edit_description': edit_description,
            'edited_url': f"https://images.example.com/edited_{hashlib.md5(edit_description.encode()).hexdigest()}.png",
            'edited_at': datetime.now().isoformat()
        }
    
    def _generate_id(self, prompt: str) -> str:
        """Generate unique image ID"""
        return hashlib.md5(f"{prompt}{datetime.now()}".encode()).hexdigest()[:12]
    
    def _generate_seed(self, prompt: str, index: int) -> int:
        """Generate consistent seed for reproducibility"""
        base = hashlib.md5(prompt.encode()).hexdigest()
        return int(base, 16) % 100000 + index
    
    def _get_credits_for_model(self, model: ImageModel) -> float:
        """Get credit cost for model"""
        costs = {
            ImageModel.DALL_E_3: 0.020,  # $0.020 per image
            ImageModel.MIDJOURNEY: 0.15,  # $0.15 per image
            ImageModel.STABLE_DIFFUSION: 0.005,  # $0.005 per image
            ImageModel.LEONARDO: 0.010  # $0.010 per image
        }
        return costs.get(model, 0.01)


class CreativeAssetLibrary:
    """Manage generated and uploaded creative assets"""
    
    def __init__(self):
        self.assets: Dict[str, Dict] = {}
        self.categories: List[str] = []
        self.tags: Dict[str, List[str]] = {}
    
    def add_asset(self, asset_type: str, url: str, metadata: Dict) -> Dict:
        """Add asset to library"""
        asset_id = hashlib.md5(url.encode()).hexdigest()[:12]
        
        asset = {
            'asset_id': asset_id,
            'type': asset_type,  # 'image', 'video', 'audio'
            'url': url,
            'uploaded_at': datetime.now().isoformat(),
            'usage_count': 0,
            'metadata': metadata
        }
        
        self.assets[asset_id] = asset
        return asset
    
    def tag_asset(self, asset_id: str, tags: List[str]) -> None:
        """Tag asset for search"""
        if asset_id not in self.tags:
            self.tags[asset_id] = []
        self.tags[asset_id].extend(tags)
    
    def search_assets(self, query: str, asset_type: Optional[str] = None) -> List[Dict]:
        """Search assets by tags or metadata"""
        results = []
        query_lower = query.lower()
        
        for asset_id, asset in self.assets.items():
            # Check tags
            if asset_id in self.tags:
                if any(query_lower in tag.lower() for tag in self.tags[asset_id]):
                    results.append(asset)
                    continue
            
            # Check metadata
            if asset_type and asset.get('type') != asset_type:
                continue
            
            # Check metadata fields
            metadata = asset.get('metadata', {})
            if any(query_lower in str(v).lower() for v in metadata.values()):
                results.append(asset)
        
        return results
    
    def get_assets_by_category(self, category: str) -> List[Dict]:
        """Get assets in specific category"""
        return [
            asset for asset in self.assets.values()
            if asset.get('metadata', {}).get('category') == category
        ]
    
    def track_asset_usage(self, asset_id: str) -> None:
        """Track when asset is used"""
        if asset_id in self.assets:
            self.assets[asset_id]['usage_count'] += 1
    
    def get_most_used_assets(self, limit: int = 10) -> List[Dict]:
        """Get most frequently used assets"""
        sorted_assets = sorted(
            self.assets.values(),
            key=lambda x: x['usage_count'],
            reverse=True
        )
        return sorted_assets[:limit]


class PromptEngineering:
    """Build effective AI image prompts"""
    
    @staticmethod
    def build_product_image_prompt(product: str, benefits: List[str],
                                   style: ImageStyle = ImageStyle.PHOTOREALISTIC) -> str:
        """Build prompt for product image"""
        benefits_str = ", ".join(benefits[:3])
        
        prompt = f"""
        Professional product photography of {product}
        Highlighting: {benefits_str}
        Style: {style.value}
        Lighting: studio lighting, soft shadows
        Background: clean white background
        Quality: high quality, detailed, professional, trending on Dribbble
        """
        
        return prompt.strip()
    
    @staticmethod
    def build_social_media_prompt(platform: str, theme: str,
                                  dimensions: Tuple[int, int] = (1080, 1080)) -> str:
        """Build prompt for social media content"""
        platform_specs = {
            'instagram': '1080x1080, square format',
            'facebook': '1200x628, landscape',
            'twitter': '1024x512, wide',
            'tiktok': '1080x1920, vertical',
            'linkedin': '1200x627, article'
        }
        
        spec = platform_specs.get(platform, f'{dimensions[0]}x{dimensions[1]}')
        
        prompt = f"""
        {platform} content image
        Theme: {theme}
        Format: {spec}
        Eye-catching, engaging, on-brand
        Ready to post, high quality
        """
        
        return prompt.strip()
    
    @staticmethod
    def build_ad_creative_prompt(headline: str, cta: str,
                                  product: str = None) -> str:
        """Build prompt for ad creative"""
        prompt = f"""
        Compelling ad creative
        Headline: {headline}
        Call-to-action: {cta}
        """
        
        if product:
            prompt += f"\nProduct focus: {product}"
        
        prompt += """
        Modern, clean design
        High contrast, attention-grabbing
        Professional marketing quality
        """
        
        return prompt.strip()
    
    @staticmethod
    def add_style_modifiers(base_prompt: str, style: ImageStyle,
                           quality: str = 'high') -> str:
        """Add style and quality modifiers to prompt"""
        modifiers = {
            ImageStyle.PHOTOREALISTIC: "ultra realistic, 8k, professional photography",
            ImageStyle.ILLUSTRATION: "digital illustration, vector art style",
            ImageStyle.CARTOON: "cartoon style, playful, colorful",
            ImageStyle.MINIMALIST: "minimalist design, clean lines, simple",
            ImageStyle.CINEMATIC: "cinematic lighting, movie quality, dramatic",
            ImageStyle.WATERCOLOR: "watercolor painting, artistic, soft",
            ImageStyle.ABSTRACT: "abstract art, modern, geometric",
            ImageStyle.VINTAGE: "vintage style, retro, nostalgic"
        }
        
        quality_map = {
            'high': ", masterpiece, award-winning",
            'medium': ", professional quality",
            'low': ", basic quality"
        }
        
        modifier = modifiers.get(style, "")
        quality_mod = quality_map.get(quality, "")
        
        return f"{base_prompt}\n{modifier}{quality_mod}"


class AIImageManager:
    """Unified image management system"""
    
    def __init__(self):
        self.generator = AIImageGenerator()
        self.library = CreativeAssetLibrary()
        self.prompt_engineer = PromptEngineering()
    
    def generate_campaign_images(self, campaign_brief: Dict,
                                quantity_per_variant: int = 3) -> List[Dict]:
        """Generate complete set of images for campaign"""
        campaign_images = {
            'campaign_id': campaign_brief.get('campaign_id'),
            'generated_at': datetime.now().isoformat(),
            'variants': []
        }
        
        # Generate hero image
        hero_prompt = self.prompt_engineer.build_product_image_prompt(
            campaign_brief.get('product', ''),
            campaign_brief.get('benefits', [])
        )
        hero_images = self.generator.generate_image(hero_prompt, quantity=1)
        campaign_images['variants'].append({
            'name': 'Hero Image',
            'images': hero_images
        })
        
        # Generate social variants
        for platform in ['instagram', 'facebook', 'twitter']:
            social_prompt = self.prompt_engineer.build_social_media_prompt(
                platform,
                campaign_brief.get('theme', 'product promotion')
            )
            social_images = self.generator.generate_image(
                social_prompt,
                quantity=quantity_per_variant
            )
            campaign_images['variants'].append({
                'name': f'{platform.title()} Variant',
                'images': social_images
            })
        
        # Add all to library
        for variant in campaign_images['variants']:
            for image in variant['images']:
                self.library.add_asset('image', image['url'], image)
        
        return campaign_images['variants']
    
    def get_usage_stats(self) -> Dict:
        """Get image generation usage statistics"""
        return {
            'total_images_generated': self.generator.images_generated,
            'total_credits_used': self.generator.credits_used,
            'library_size': len(self.library.assets),
            'most_used_assets': self.library.get_most_used_assets(5)
        }

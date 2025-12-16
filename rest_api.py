"""
REST API & Webhook System
FastAPI-based REST endpoints for programmatic access and external integrations
"""

from typing import Dict, List, Optional, Any
from enum import Enum
from datetime import datetime, timedelta
import hashlib
import json

class APIVersion(Enum):
    """API versions"""
    V1 = "v1"
    V2 = "v2"


class APIEndpointCategory(Enum):
    """API endpoint categories"""
    CAMPAIGNS = "campaigns"
    CONTENT = "content"
    ANALYTICS = "analytics"
    PLATFORMS = "platforms"
    WORKFLOWS = "workflows"
    ASSETS = "assets"
    WEBHOOKS = "webhooks"
    USERS = "users"


class APIKey:
    """API Key management"""
    
    def __init__(self, user_id: str, name: str, permissions: List[str]):
        self.user_id = user_id
        self.name = name
        self.key = self._generate_key()
        self.permissions = permissions
        self.created_at = datetime.now()
        self.last_used = None
        self.rate_limit = 1000  # requests per hour
        self.requests_used = 0
    
    def _generate_key(self) -> str:
        """Generate unique API key"""
        key_material = f"{self.user_id}{datetime.now().isoformat()}{hashlib.urandom(16)}"
        return "tco_" + hashlib.sha256(key_material.encode()).hexdigest()[:32]
    
    def validate_permission(self, required_permission: str) -> bool:
        """Check if key has required permission"""
        return required_permission in self.permissions or 'admin' in self.permissions
    
    def check_rate_limit(self) -> bool:
        """Check if rate limit exceeded"""
        return self.requests_used < self.rate_limit
    
    def record_usage(self) -> None:
        """Record API key usage"""
        self.requests_used += 1
        self.last_used = datetime.now()


class RESTAPIEndpoint:
    """Base API endpoint"""
    
    def __init__(self, path: str, method: str, category: APIEndpointCategory):
        self.path = path
        self.method = method
        self.category = category
        self.description = ""
        self.parameters: List[Dict] = []
        self.request_schema: Dict = {}
        self.response_schema: Dict = {}
        self.rate_limit_per_hour = 1000
    
    def to_openapi_spec(self) -> Dict:
        """Generate OpenAPI specification"""
        return {
            'path': self.path,
            'method': self.method.lower(),
            'summary': self.description,
            'parameters': self.parameters,
            'requestBody': {'schema': self.request_schema},
            'responses': {
                '200': {'description': 'Success', 'schema': self.response_schema},
                '401': {'description': 'Unauthorized'},
                '429': {'description': 'Rate limit exceeded'}
            }
        }


class RestAPIManager:
    """Manage REST API endpoints and access"""
    
    def __init__(self):
        self.endpoints: List[RESTAPIEndpoint] = []
        self.api_keys: Dict[str, APIKey] = {}
        self.webhooks: List[Dict] = []
        self.request_log: List[Dict] = []
    
    def register_endpoints(self) -> List[RESTAPIEndpoint]:
        """Register all available endpoints"""
        endpoints = []
        
        # Campaign endpoints
        endpoints.extend([
            self._create_endpoint('/campaigns', 'GET', APIEndpointCategory.CAMPAIGNS,
                                 'List all campaigns'),
            self._create_endpoint('/campaigns/{campaign_id}', 'GET', APIEndpointCategory.CAMPAIGNS,
                                 'Get campaign details'),
            self._create_endpoint('/campaigns', 'POST', APIEndpointCategory.CAMPAIGNS,
                                 'Create new campaign'),
            self._create_endpoint('/campaigns/{campaign_id}', 'PUT', APIEndpointCategory.CAMPAIGNS,
                                 'Update campaign'),
            self._create_endpoint('/campaigns/{campaign_id}', 'DELETE', APIEndpointCategory.CAMPAIGNS,
                                 'Delete campaign'),
        ])
        
        # Content endpoints
        endpoints.extend([
            self._create_endpoint('/content/generate', 'POST', APIEndpointCategory.CONTENT,
                                 'Generate content'),
            self._create_endpoint('/content/optimize', 'POST', APIEndpointCategory.CONTENT,
                                 'Optimize content'),
            self._create_endpoint('/content/variations', 'POST', APIEndpointCategory.CONTENT,
                                 'Generate content variations'),
            self._create_endpoint('/content/analyze', 'POST', APIEndpointCategory.CONTENT,
                                 'Analyze content'),
        ])
        
        # Analytics endpoints
        endpoints.extend([
            self._create_endpoint('/analytics/campaigns', 'GET', APIEndpointCategory.ANALYTICS,
                                 'Get campaign analytics'),
            self._create_endpoint('/analytics/metrics/{metric_name}', 'GET',
                                 APIEndpointCategory.ANALYTICS, 'Get specific metric'),
            self._create_endpoint('/analytics/forecast', 'POST', APIEndpointCategory.ANALYTICS,
                                 'Forecast performance'),
            self._create_endpoint('/analytics/report', 'GET', APIEndpointCategory.ANALYTICS,
                                 'Generate report'),
        ])
        
        # Platform endpoints
        endpoints.extend([
            self._create_endpoint('/platforms', 'GET', APIEndpointCategory.PLATFORMS,
                                 'List connected platforms'),
            self._create_endpoint('/platforms/{platform_id}', 'GET', APIEndpointCategory.PLATFORMS,
                                 'Get platform details'),
            self._create_endpoint('/platforms/{platform_id}/publish', 'POST',
                                 APIEndpointCategory.PLATFORMS, 'Publish to platform'),
        ])
        
        # Workflow endpoints
        endpoints.extend([
            self._create_endpoint('/workflows', 'GET', APIEndpointCategory.WORKFLOWS,
                                 'List workflows'),
            self._create_endpoint('/workflows', 'POST', APIEndpointCategory.WORKFLOWS,
                                 'Create workflow'),
            self._create_endpoint('/workflows/{workflow_id}', 'GET', APIEndpointCategory.WORKFLOWS,
                                 'Get workflow'),
            self._create_endpoint('/workflows/{workflow_id}', 'PUT', APIEndpointCategory.WORKFLOWS,
                                 'Update workflow'),
            self._create_endpoint('/workflows/{workflow_id}/execute', 'POST',
                                 APIEndpointCategory.WORKFLOWS, 'Execute workflow'),
        ])
        
        self.endpoints = endpoints
        return endpoints
    
    def _create_endpoint(self, path: str, method: str,
                        category: APIEndpointCategory, description: str) -> RESTAPIEndpoint:
        """Create endpoint definition"""
        endpoint = RESTAPIEndpoint(path, method, category)
        endpoint.description = description
        return endpoint
    
    def create_api_key(self, user_id: str, name: str,
                       permissions: List[str] = None) -> APIKey:
        """Create new API key"""
        if permissions is None:
            permissions = ['read:campaigns', 'read:analytics']
        
        api_key = APIKey(user_id, name, permissions)
        self.api_keys[api_key.key] = api_key
        return api_key
    
    def validate_api_key(self, key: str) -> Optional[APIKey]:
        """Validate and retrieve API key"""
        return self.api_keys.get(key)
    
    def record_request(self, api_key_str: str, endpoint: str, method: str,
                      status_code: int, response_time_ms: float) -> None:
        """Log API request"""
        api_key = self.api_keys.get(api_key_str)
        if api_key:
            api_key.record_usage()
        
        self.request_log.append({
            'timestamp': datetime.now().isoformat(),
            'api_key': api_key_str[:16] + '...',
            'endpoint': endpoint,
            'method': method,
            'status_code': status_code,
            'response_time_ms': response_time_ms
        })
    
    def get_api_stats(self, api_key: str) -> Dict:
        """Get API key usage statistics"""
        key_obj = self.api_keys.get(api_key)
        if not key_obj:
            return {}
        
        recent_requests = [
            req for req in self.request_log
            if req['api_key'] == api_key[:16] + '...'
        ]
        
        return {
            'key_name': key_obj.name,
            'created_at': key_obj.created_at.isoformat(),
            'last_used': key_obj.last_used.isoformat() if key_obj.last_used else None,
            'requests_used_this_hour': key_obj.requests_used,
            'rate_limit': key_obj.rate_limit,
            'recent_requests': recent_requests[-10:]
        }
    
    def get_openapi_spec(self, version: APIVersion = APIVersion.V1) -> Dict:
        """Generate OpenAPI specification"""
        return {
            'openapi': '3.0.0',
            'info': {
                'title': 'Thecontent API',
                'version': version.value,
                'description': 'REST API for content marketing and campaign management'
            },
            'paths': {
                endpoint.path: {
                    endpoint.method.lower(): endpoint.to_openapi_spec()
                }
                for endpoint in self.endpoints
            },
            'servers': [
                {'url': 'https://api.thecontent.ai', 'description': 'Production'},
                {'url': 'https://staging-api.thecontent.ai', 'description': 'Staging'}
            ],
            'components': {
                'securitySchemes': {
                    'apiKey': {
                        'type': 'apiKey',
                        'in': 'header',
                        'name': 'X-API-Key'
                    }
                }
            }
        }


class WebhookManager:
    """Manage webhooks for event notifications"""
    
    def __init__(self):
        self.webhooks: Dict[str, Dict] = {}
        self.events: List[Dict] = []
    
    def register_webhook(self, user_id: str, url: str, events: List[str]) -> Dict:
        """Register webhook endpoint"""
        webhook_id = f"wh_{hashlib.md5(f'{user_id}{url}{datetime.now()}'.encode()).hexdigest()[:16]}"
        
        webhook = {
            'webhook_id': webhook_id,
            'user_id': user_id,
            'url': url,
            'events': events,
            'active': True,
            'registered_at': datetime.now().isoformat(),
            'last_triggered': None,
            'trigger_count': 0,
            'secret': hashlib.sha256(f"{webhook_id}{user_id}".encode()).hexdigest()
        }
        
        self.webhooks[webhook_id] = webhook
        return webhook
    
    def trigger_webhook(self, event_type: str, event_data: Dict) -> List[str]:
        """Trigger webhooks for event"""
        triggered_webhooks = []
        
        for webhook_id, webhook in self.webhooks.items():
            if not webhook['active']:
                continue
            
            if event_type not in webhook['events']:
                continue
            
            # In production, would actually POST to webhook URL
            webhook['last_triggered'] = datetime.now().isoformat()
            webhook['trigger_count'] += 1
            triggered_webhooks.append(webhook_id)
            
            self.events.append({
                'event_type': event_type,
                'webhook_id': webhook_id,
                'triggered_at': datetime.now().isoformat(),
                'event_data': event_data
            })
        
        return triggered_webhooks
    
    def get_webhook(self, webhook_id: str) -> Optional[Dict]:
        """Get webhook details"""
        return self.webhooks.get(webhook_id)
    
    def delete_webhook(self, webhook_id: str) -> bool:
        """Delete webhook"""
        if webhook_id in self.webhooks:
            del self.webhooks[webhook_id]
            return True
        return False
    
    def list_webhooks(self, user_id: str) -> List[Dict]:
        """List user's webhooks"""
        return [
            wh for wh in self.webhooks.values()
            if wh['user_id'] == user_id
        ]
    
    def get_webhook_events(self, webhook_id: str, hours: int = 24) -> List[Dict]:
        """Get recent webhook events"""
        cutoff = datetime.now() - timedelta(hours=hours)
        
        return [
            event for event in self.events
            if event['webhook_id'] == webhook_id and
            datetime.fromisoformat(event['triggered_at']) > cutoff
        ]
    
    def get_available_events(self) -> List[str]:
        """Get list of subscribable events"""
        return [
            'campaign.created',
            'campaign.updated',
            'campaign.deleted',
            'campaign.paused',
            'content.generated',
            'content.published',
            'analytics.metric_update',
            'workflow.executed',
            'alert.triggered'
        ]


class ThirdPartyIntegration:
    """Manage third-party integrations"""
    
    def __init__(self):
        self.integrations: Dict[str, Dict] = {}
    
    def register_integration(self, name: str, auth_method: str,
                           config: Dict) -> Dict:
        """Register third-party integration"""
        integration_id = f"int_{hashlib.md5(f'{name}{datetime.now()}'.encode()).hexdigest()[:16]}"
        
        integration = {
            'integration_id': integration_id,
            'name': name,
            'auth_method': auth_method,  # 'oauth', 'api_key', 'webhook'
            'config': config,
            'connected_at': datetime.now().isoformat(),
            'last_sync': None,
            'status': 'active'
        }
        
        self.integrations[integration_id] = integration
        return integration
    
    def get_integration(self, integration_id: str) -> Optional[Dict]:
        """Get integration details"""
        return self.integrations.get(integration_id)
    
    def list_integrations(self) -> List[Dict]:
        """List all integrations"""
        return list(self.integrations.values())
    
    def sync_integration(self, integration_id: str) -> Dict:
        """Sync integration data"""
        if integration_id not in self.integrations:
            return {'error': 'Integration not found'}
        
        integration = self.integrations[integration_id]
        integration['last_sync'] = datetime.now().isoformat()
        
        return {
            'integration_id': integration_id,
            'sync_status': 'completed',
            'records_synced': 150,
            'synced_at': integration['last_sync']
        }

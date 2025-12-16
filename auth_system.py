"""
User Authentication & Team Management System
Enables multi-user support, role-based access, workspace management
"""

from typing import Dict, List, Optional, Tuple
from datetime import datetime, timedelta
import json
import hashlib

class User:
    """User account management"""
    
    def __init__(self, user_id: str, email: str, name: str, hashed_password: str):
        self.user_id = user_id
        self.email = email
        self.name = name
        self.hashed_password = hashed_password
        self.created_at = datetime.now()
        self.api_keys = []
        self.preferences = {}
        self.quota = {
            'monthly_generations': 10000,
            'monthly_api_calls': 50000,
            'storage_gb': 10,
            'team_members': 5
        }
        self.current_usage = {
            'generations_this_month': 0,
            'api_calls_this_month': 0,
            'storage_used_gb': 0
        }
    
    def verify_password(self, password: str) -> bool:
        """Verify password matches hash"""
        return hashlib.sha256(password.encode()).hexdigest() == self.hashed_password
    
    def generate_api_key(self) -> str:
        """Generate new API key for user"""
        api_key = hashlib.sha256(f"{self.user_id}{datetime.now().isoformat()}".encode()).hexdigest()
        self.api_keys.append({
            'key': api_key,
            'created_at': datetime.now().isoformat(),
            'last_used': None,
            'active': True
        })
        return api_key
    
    def has_quota(self, resource: str, amount: int = 1) -> bool:
        """Check if user has quota for resource"""
        allowed = self.quota.get(resource, 0)
        used = self.current_usage.get(f"{resource.split('_')[0]}_this_month", 0)
        return (used + amount) <= allowed
    
    def use_quota(self, resource: str, amount: int = 1):
        """Deduct from user quota"""
        key = f"{resource.split('_')[0]}_this_month"
        if key in self.current_usage:
            self.current_usage[key] += amount
    
    def to_dict(self) -> Dict:
        """Serialize user (excluding password)"""
        return {
            'user_id': self.user_id,
            'email': self.email,
            'name': self.name,
            'created_at': self.created_at.isoformat(),
            'quota': self.quota,
            'current_usage': self.current_usage
        }


class TeamWorkspace:
    """Team workspace with members and permissions"""
    
    def __init__(self, workspace_id: str, name: str, owner_id: str):
        self.workspace_id = workspace_id
        self.name = name
        self.owner_id = owner_id
        self.members = {owner_id: {'role': 'owner', 'joined_at': datetime.now()}}
        self.created_at = datetime.now()
        self.settings = {
            'allow_api_access': True,
            'allow_integrations': True,
            'require_approval': False,
            'audit_logging': True
        }
        self.api_keys = []
        self.data_storage = {}
    
    def add_member(self, user_id: str, role: str = 'member') -> bool:
        """Add member to workspace"""
        if role not in ['owner', 'admin', 'member', 'viewer']:
            return False
        if user_id not in self.members:
            self.members[user_id] = {
                'role': role,
                'joined_at': datetime.now().isoformat(),
                'active': True
            }
            return True
        return False
    
    def remove_member(self, user_id: str) -> bool:
        """Remove member from workspace"""
        if user_id == self.owner_id:
            return False  # Can't remove owner
        if user_id in self.members:
            del self.members[user_id]
            return True
        return False
    
    def change_member_role(self, user_id: str, new_role: str) -> bool:
        """Change member role"""
        if user_id == self.owner_id and new_role != 'owner':
            return False  # Owner must stay owner
        if user_id in self.members:
            self.members[user_id]['role'] = new_role
            return True
        return False
    
    def has_permission(self, user_id: str, action: str) -> bool:
        """Check if user has permission for action"""
        if user_id not in self.members:
            return False
        
        role = self.members[user_id]['role']
        
        permissions = {
            'owner': ['view', 'create', 'edit', 'delete', 'publish', 'manage_team', 'manage_api'],
            'admin': ['view', 'create', 'edit', 'delete', 'publish', 'manage_api'],
            'member': ['view', 'create', 'edit', 'publish'],
            'viewer': ['view']
        }
        
        return action in permissions.get(role, [])
    
    def get_members(self) -> List[Dict]:
        """Get all members"""
        return [
            {'user_id': uid, **data} 
            for uid, data in self.members.items()
        ]
    
    def to_dict(self) -> Dict:
        """Serialize workspace"""
        return {
            'workspace_id': self.workspace_id,
            'name': self.name,
            'owner_id': self.owner_id,
            'created_at': self.created_at.isoformat(),
            'members_count': len(self.members),
            'settings': self.settings
        }


class AuthenticationManager:
    """Manage user authentication and sessions"""
    
    def __init__(self):
        self.users: Dict[str, User] = {}
        self.sessions: Dict[str, Dict] = {}
        self.workspaces: Dict[str, TeamWorkspace] = {}
    
    def register_user(self, email: str, name: str, password: str) -> Tuple[bool, str]:
        """Register new user"""
        if any(u.email == email for u in self.users.values()):
            return False, "Email already registered"
        
        user_id = hashlib.sha256(email.encode()).hexdigest()[:8]
        hashed_pwd = hashlib.sha256(password.encode()).hexdigest()
        
        user = User(user_id, email, name, hashed_pwd)
        self.users[user_id] = user
        
        # Create default workspace
        workspace = TeamWorkspace(f"ws_{user_id}", f"{name}'s Workspace", user_id)
        self.workspaces[workspace.workspace_id] = workspace
        
        return True, f"User {email} registered successfully"
    
    def login(self, email: str, password: str) -> Tuple[bool, Optional[str], Optional[str]]:
        """Authenticate user and create session"""
        user = None
        for u in self.users.values():
            if u.email == email:
                user = u
                break
        
        if not user or not user.verify_password(password):
            return False, None, "Invalid email or password"
        
        session_id = hashlib.sha256(f"{user.user_id}{datetime.now().isoformat()}".encode()).hexdigest()
        self.sessions[session_id] = {
            'user_id': user.user_id,
            'created_at': datetime.now().isoformat(),
            'expires_at': (datetime.now() + timedelta(hours=24)).isoformat(),
            'active': True
        }
        
        return True, session_id, f"Welcome {user.name}"
    
    def logout(self, session_id: str) -> bool:
        """End user session"""
        if session_id in self.sessions:
            self.sessions[session_id]['active'] = False
            return True
        return False
    
    def validate_session(self, session_id: str) -> Tuple[bool, Optional[str]]:
        """Validate session is still active"""
        if session_id not in self.sessions:
            return False, None
        
        session = self.sessions[session_id]
        if not session['active']:
            return False, None
        
        expires = datetime.fromisoformat(session['expires_at'])
        if datetime.now() > expires:
            session['active'] = False
            return False, None
        
        return True, session['user_id']
    
    def create_workspace(self, user_id: str, workspace_name: str) -> Tuple[bool, Optional[str]]:
        """Create new team workspace"""
        if user_id not in self.users:
            return False, None
        
        workspace_id = hashlib.sha256(f"{user_id}{workspace_name}{datetime.now().isoformat()}".encode()).hexdigest()[:8]
        workspace = TeamWorkspace(f"ws_{workspace_id}", workspace_name, user_id)
        self.workspaces[workspace.workspace_id] = workspace
        
        return True, workspace.workspace_id
    
    def get_user_workspaces(self, user_id: str) -> List[Dict]:
        """Get all workspaces user is member of"""
        user_workspaces = []
        for ws_id, ws in self.workspaces.items():
            if user_id in ws.members:
                user_workspaces.append(ws.to_dict())
        return user_workspaces
    
    def get_workspace(self, workspace_id: str) -> Optional[TeamWorkspace]:
        """Get workspace by ID"""
        return self.workspaces.get(workspace_id)
    
    def invite_to_workspace(self, workspace_id: str, user_email: str, role: str = 'member') -> Tuple[bool, str]:
        """Invite user to workspace"""
        workspace = self.workspaces.get(workspace_id)
        if not workspace:
            return False, "Workspace not found"
        
        # Find user by email
        user = None
        for u in self.users.values():
            if u.email == user_email:
                user = u
                break
        
        if not user:
            return False, "User not found"
        
        if workspace.add_member(user.user_id, role):
            return True, f"{user_email} added to workspace"
        
        return False, "User already in workspace"


class AuditLogger:
    """Track all user actions for compliance"""
    
    def __init__(self):
        self.audit_logs: List[Dict] = []
    
    def log_action(self, user_id: str, workspace_id: str, action: str, details: Dict) -> None:
        """Log user action"""
        self.audit_logs.append({
            'timestamp': datetime.now().isoformat(),
            'user_id': user_id,
            'workspace_id': workspace_id,
            'action': action,
            'details': details,
            'ip_address': details.get('ip_address')  # Should be captured from request
        })
    
    def get_logs(self, workspace_id: str, days: int = 30) -> List[Dict]:
        """Get audit logs for workspace"""
        cutoff_date = datetime.now() - timedelta(days=days)
        return [
            log for log in self.audit_logs
            if log['workspace_id'] == workspace_id and 
            datetime.fromisoformat(log['timestamp']) > cutoff_date
        ]
    
    def export_logs(self, workspace_id: str) -> str:
        """Export logs as JSON"""
        logs = self.get_logs(workspace_id)
        return json.dumps(logs, indent=2)

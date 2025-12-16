"""
Workflow & Automation Engine
Enable trigger-based actions, scheduled tasks, and conditional logic
"""

from typing import Dict, List, Optional, Callable, Any
from datetime import datetime, timedelta
from enum import Enum
import json

class TriggerType(Enum):
    """Types of triggers for workflows"""
    SCHEDULE = "schedule"  # Time-based
    EVENT = "event"        # Action-based (post published, etc)
    CONDITION = "condition"  # Performance condition (high CPA, etc)
    MANUAL = "manual"      # Manual trigger


class ActionType(Enum):
    """Types of actions workflows can perform"""
    PUBLISH = "publish"
    PAUSE_CAMPAIGN = "pause_campaign"
    SCALE_BUDGET = "scale_budget"
    SEND_ALERT = "send_alert"
    UPDATE_AUDIENCE = "update_audience"
    GENERATE_CONTENT = "generate_content"
    SEND_WEBHOOK = "send_webhook"


class WorkflowTrigger:
    """Defines when a workflow should execute"""
    
    def __init__(self, trigger_type: TriggerType, config: Dict):
        self.trigger_type = trigger_type
        self.config = config
        self.last_triggered = None
        self.trigger_count = 0
    
    def should_trigger(self, context: Dict) -> bool:
        """Check if trigger conditions are met"""
        if self.trigger_type == TriggerType.SCHEDULE:
            return self._check_schedule(context)
        elif self.trigger_type == TriggerType.EVENT:
            return self._check_event(context)
        elif self.trigger_type == TriggerType.CONDITION:
            return self._check_condition(context)
        return False
    
    def _check_schedule(self, context: Dict) -> bool:
        """Check if scheduled time has arrived"""
        schedule = self.config.get('schedule', {})
        interval = schedule.get('interval')  # 'daily', 'weekly', 'monthly'
        time_of_day = schedule.get('time', '08:00')
        
        if not self.last_triggered:
            return True
        
        now = datetime.now()
        last = datetime.fromisoformat(self.last_triggered)
        
        if interval == 'daily' and (now - last).days >= 1:
            return now.strftime('%H:%M') >= time_of_day
        elif interval == 'weekly' and (now - last).days >= 7:
            return True
        elif interval == 'monthly' and (now - last).days >= 30:
            return True
        
        return False
    
    def _check_event(self, context: Dict) -> bool:
        """Check if event condition is met"""
        event_type = self.config.get('event_type')
        return context.get('event_type') == event_type
    
    def _check_condition(self, context: Dict) -> bool:
        """Check if performance condition is met"""
        metric = self.config.get('metric')  # 'cpa', 'roas', 'ctr', etc
        operator = self.config.get('operator')  # '>', '<', '==', etc
        threshold = self.config.get('threshold')
        
        actual_value = context.get(metric, 0)
        
        if operator == '>':
            return actual_value > threshold
        elif operator == '<':
            return actual_value < threshold
        elif operator == '>=':
            return actual_value >= threshold
        elif operator == '<=':
            return actual_value <= threshold
        elif operator == '==':
            return actual_value == threshold
        
        return False


class WorkflowAction:
    """Defines what happens when workflow is triggered"""
    
    def __init__(self, action_type: ActionType, config: Dict):
        self.action_type = action_type
        self.config = config
        self.executed_at = None
        self.execution_count = 0
        self.last_result = None
    
    def execute(self, context: Dict, executor: Callable = None) -> Dict:
        """Execute the action"""
        result = {
            'action': self.action_type.value,
            'executed_at': datetime.now().isoformat(),
            'success': False,
            'details': {}
        }
        
        try:
            if self.action_type == ActionType.PUBLISH:
                result = self._execute_publish(context)
            elif self.action_type == ActionType.PAUSE_CAMPAIGN:
                result = self._execute_pause(context)
            elif self.action_type == ActionType.SCALE_BUDGET:
                result = self._execute_scale_budget(context)
            elif self.action_type == ActionType.SEND_ALERT:
                result = self._execute_alert(context)
            elif self.action_type == ActionType.GENERATE_CONTENT:
                result = self._execute_generate_content(context)
            elif self.action_type == ActionType.SEND_WEBHOOK:
                result = self._execute_webhook(context)
            
            result['success'] = True
            self.execution_count += 1
            self.executed_at = datetime.now().isoformat()
            self.last_result = result
        except Exception as e:
            result['success'] = False
            result['error'] = str(e)
        
        return result
    
    def _execute_publish(self, context: Dict) -> Dict:
        """Publish content"""
        return {
            'action': 'publish',
            'post_id': f"post_{int(datetime.now().timestamp())}",
            'platforms': self.config.get('platforms', ['facebook', 'instagram']),
            'content_id': context.get('content_id'),
            'scheduled_for': context.get('scheduled_time')
        }
    
    def _execute_pause(self, context: Dict) -> Dict:
        """Pause campaign"""
        return {
            'action': 'pause_campaign',
            'campaign_id': context.get('campaign_id'),
            'reason': self.config.get('reason', 'Automated pause'),
            'paused_at': datetime.now().isoformat()
        }
    
    def _execute_scale_budget(self, context: Dict) -> Dict:
        """Scale campaign budget"""
        current_budget = context.get('current_budget', 1000)
        scale_percentage = self.config.get('scale_percentage', 10)
        new_budget = current_budget * (1 + scale_percentage / 100)
        
        return {
            'action': 'scale_budget',
            'campaign_id': context.get('campaign_id'),
            'old_budget': current_budget,
            'new_budget': new_budget,
            'scale_percentage': scale_percentage
        }
    
    def _execute_alert(self, context: Dict) -> Dict:
        """Send alert notification"""
        return {
            'action': 'send_alert',
            'alert_type': self.config.get('alert_type'),
            'recipient': self.config.get('recipient_email'),
            'subject': self.config.get('subject'),
            'sent_at': datetime.now().isoformat()
        }
    
    def _execute_generate_content(self, context: Dict) -> Dict:
        """Generate new content"""
        return {
            'action': 'generate_content',
            'topic': self.config.get('topic'),
            'platform': self.config.get('platform'),
            'content_id': f"gen_{int(datetime.now().timestamp())}",
            'generated_at': datetime.now().isoformat()
        }
    
    def _execute_webhook(self, context: Dict) -> Dict:
        """Send webhook to external service"""
        return {
            'action': 'send_webhook',
            'webhook_url': self.config.get('webhook_url'),
            'payload': context,
            'sent_at': datetime.now().isoformat()
        }


class Workflow:
    """Automated workflow with triggers and actions"""
    
    def __init__(self, workflow_id: str, name: str, trigger: WorkflowTrigger):
        self.workflow_id = workflow_id
        self.name = name
        self.trigger = trigger
        self.actions: List[WorkflowAction] = []
        self.enabled = True
        self.created_at = datetime.now()
        self.execution_history: List[Dict] = []
    
    def add_action(self, action: WorkflowAction) -> None:
        """Add action to workflow"""
        self.actions.append(action)
    
    def should_execute(self, context: Dict) -> bool:
        """Check if workflow should execute"""
        return self.enabled and self.trigger.should_trigger(context)
    
    def execute(self, context: Dict) -> Dict:
        """Execute all actions in workflow"""
        execution_record = {
            'workflow_id': self.workflow_id,
            'workflow_name': self.name,
            'executed_at': datetime.now().isoformat(),
            'actions_executed': []
        }
        
        for action in self.actions:
            result = action.execute(context)
            execution_record['actions_executed'].append(result)
        
        self.execution_history.append(execution_record)
        self.trigger.trigger_count += 1
        self.trigger.last_triggered = datetime.now().isoformat()
        
        return execution_record
    
    def to_dict(self) -> Dict:
        """Serialize workflow"""
        return {
            'workflow_id': self.workflow_id,
            'name': self.name,
            'enabled': self.enabled,
            'created_at': self.created_at.isoformat(),
            'trigger_type': self.trigger.trigger_type.value,
            'actions_count': len(self.actions),
            'execution_count': self.trigger.trigger_count
        }


class WorkflowEngine:
    """Manage and execute workflows"""
    
    def __init__(self):
        self.workflows: Dict[str, Workflow] = {}
        self.execution_log: List[Dict] = []
    
    def create_workflow(self, name: str, trigger: WorkflowTrigger) -> Workflow:
        """Create new workflow"""
        workflow_id = f"wf_{int(datetime.now().timestamp())}"
        workflow = Workflow(workflow_id, name, trigger)
        self.workflows[workflow_id] = workflow
        return workflow
    
    def get_workflow(self, workflow_id: str) -> Optional[Workflow]:
        """Get workflow by ID"""
        return self.workflows.get(workflow_id)
    
    def delete_workflow(self, workflow_id: str) -> bool:
        """Delete workflow"""
        if workflow_id in self.workflows:
            del self.workflows[workflow_id]
            return True
        return False
    
    def enable_workflow(self, workflow_id: str) -> bool:
        """Enable workflow"""
        if workflow_id in self.workflows:
            self.workflows[workflow_id].enabled = True
            return True
        return False
    
    def disable_workflow(self, workflow_id: str) -> bool:
        """Disable workflow"""
        if workflow_id in self.workflows:
            self.workflows[workflow_id].enabled = False
            return True
        return False
    
    def process_event(self, event: Dict) -> List[Dict]:
        """Process event and execute triggered workflows"""
        results = []
        for workflow in self.workflows.values():
            if workflow.should_execute(event):
                result = workflow.execute(event)
                results.append(result)
                self.execution_log.append(result)
        
        return results
    
    def get_workflow_templates(self) -> List[Dict]:
        """Get pre-built workflow templates"""
        return [
            {
                'name': 'Daily Content Publishing',
                'description': 'Publish pre-generated content daily at specific time',
                'trigger_type': 'schedule',
                'actions': ['publish']
            },
            {
                'name': 'High CPA Alert & Pause',
                'description': 'Alert if CPA exceeds threshold and pause campaign',
                'trigger_type': 'condition',
                'actions': ['send_alert', 'pause_campaign']
            },
            {
                'name': 'Successful Campaign Scaling',
                'description': 'Scale budget when ROAS exceeds target',
                'trigger_type': 'condition',
                'actions': ['scale_budget', 'send_alert']
            },
            {
                'name': 'Content Refresh On Low Performance',
                'description': 'Generate new content when CTR drops below threshold',
                'trigger_type': 'condition',
                'actions': ['generate_content', 'publish']
            },
            {
                'name': 'Weekly Performance Report',
                'description': 'Send weekly performance summary via email/webhook',
                'trigger_type': 'schedule',
                'actions': ['send_alert', 'send_webhook']
            }
        ]
    
    def get_execution_history(self, workflow_id: Optional[str] = None, hours: int = 24) -> List[Dict]:
        """Get execution history"""
        cutoff = datetime.now() - timedelta(hours=hours)
        history = [
            log for log in self.execution_log
            if (workflow_id is None or log['workflow_id'] == workflow_id) and
            datetime.fromisoformat(log['executed_at']) > cutoff
        ]
        return history
    
    def get_workflow_stats(self) -> Dict:
        """Get workflow statistics"""
        return {
            'total_workflows': len(self.workflows),
            'enabled_workflows': sum(1 for w in self.workflows.values() if w.enabled),
            'total_executions': len(self.execution_log),
            'last_execution': self.execution_log[-1]['executed_at'] if self.execution_log else None
        }

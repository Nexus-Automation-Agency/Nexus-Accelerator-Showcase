from abc import ABC, abstractmethod
from typing import Dict, Any

class WorkflowContract(ABC):
    """Public enterprise workflow contract."""

    @abstractmethod
    def execute(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Route workflow through the automation platform."""
        raise NotImplementedError

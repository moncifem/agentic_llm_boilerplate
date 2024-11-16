from typing import Any, Dict
from pydantic import BaseModel, Field

class BaseTool(BaseModel):
    """Simple base class for all tools."""
    
    name: str = Field(..., description="The name of the tool")
    description: str = Field(..., description="A description of what the tool does")

    async def run(self, input_data: str) -> Dict[str, Any]:
        """Execute the tool's primary function."""
        raise NotImplementedError
from typing import Any, Dict
from pydantic import Field
from .base import BaseTool

class EchoTool(BaseTool):
    """A simple tool that echoes back the input."""
    
    name: str = Field(
        default="echo",
        description="Echo Tool"
    )
    description: str = Field(
        default="Repeats back whatever input it receives"
    )
    
    async def run(self, input_data: str) -> Dict[str, Any]:
        """Simply return the input."""
        return {
            "result": f"You said: {input_data}"
        }
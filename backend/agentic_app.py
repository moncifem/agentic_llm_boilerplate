from fastapi import FastAPI
from agent.tools import available_tools

app = FastAPI(title="Simple Agent API")

@app.post("/echo")
async def echo(message: str):
    """Simple endpoint that echoes the message."""
    tool = available_tools["echo"]
    result = await tool.run(message)
    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
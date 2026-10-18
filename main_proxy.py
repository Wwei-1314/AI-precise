from fastapi import FastAPI
import requests
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 允许你的github.io前端域名跨域访问
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://wwei-1314.github.io"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 请求体结构
class ChatRequest(BaseModel):
    api_key: str
    prompt: str
    model: str = "deepseek-chat"

@app.post("/api/chat")
async def chat(req: ChatRequest):
    url = "https://api.deepseek.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {req.api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": req.model,
        "messages": [{"role": "user", "content": req.prompt}]
    }
    resp = requests.post(url, headers=headers, json=payload)
    return resp.json()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main_proxy:app", host="0.0.0.0", port=8000)

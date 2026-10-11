from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import chat_router
import uvicorn

app = FastAPI(
    title="ChatBot LangChain API",
    description="FastAPI + LangChain + OpenAI 챗봇 서비스",
    version="1.0.0"
)

# CORS 설정 — Django 앱에서의 요청 허용
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000", "http://127.0.0.1:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우터 등록 — /chat/ 이하 모든 URL을 chat_router에서 처리
app.include_router(chat_router.router, prefix="/chat", tags=["chat"])


@app.get("/")
async def root():
    return {"message": "ChatBot LangChain API is running!", "docs": "/docs"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
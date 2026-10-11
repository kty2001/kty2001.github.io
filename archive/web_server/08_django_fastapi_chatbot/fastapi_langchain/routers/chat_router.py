from fastapi import APIRouter, HTTPException
from models.chat_models import ChatRequest, ChatResponse, SetHistoryRequest
from services.langchain_service import chat_service
import logging

logger = logging.getLogger(__name__)
router = APIRouter()


@router.post("/", response_model=ChatResponse)
async def send_message(chat_request: ChatRequest):
    """사용자 메시지를 받아 AI 응답 반환"""
    try:
        response = await chat_service.get_chat_response(
            message=chat_request.message,
            session_id=chat_request.session_id
        )
        return ChatResponse(response=response, session_id=chat_request.session_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/history/{session_id}")
async def get_chat_history(session_id: str):
    """특정 세션의 대화 이력 조회"""
    history = chat_service.get_chat_history_for_display(session_id)
    return {"session_id": session_id, "history": history}


@router.delete("/session/{session_id}")
async def clear_session(session_id: str):
    """특정 세션의 대화 이력 삭제"""
    success = chat_service.clear_session_memory(session_id)
    if success:
        return {"message": f"세션 {session_id} 삭제 완료"}
    return {"message": f"세션 {session_id}를 찾을 수 없음"}


@router.get("/sessions")
async def list_active_sessions():
    """활성 세션 목록 조회"""
    sessions = chat_service.get_active_sessions()
    return {"active_sessions": sessions, "count": len(sessions)}


@router.get("/test")
async def test_endpoint():
    """라우터 동작 확인용 테스트 엔드포인트"""
    return {"message": "Chat router is working!", "service_status": "active"}


@router.post("/history/set")
async def set_history(request: SetHistoryRequest):
    """DB에서 불러온 이력을 FastAPI 세션에 주입"""
    session_id = request.session_id or "default"
    loaded = chat_service.set_history(
        session_id=session_id,
        items=[{"type": item.type, "content": item.content} for item in request.history]
    )
    return {"message": "이력 주입 완료", "session_id": session_id, "loaded": loaded}
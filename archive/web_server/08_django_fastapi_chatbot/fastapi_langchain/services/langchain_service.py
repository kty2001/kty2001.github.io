import os
from typing import List, Dict, Optional
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory, BaseChatMessageHistory
import logging

load_dotenv()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class LangChainChatService:
    def __init__(self):
        self.api_key = os.getenv('OPENAI_API_KEY')
        if not self.api_key:
            raise ValueError('OPENAI_API_KEY 등록 필요')

        self.model_name = os.getenv('OPENAI_MODEL', 'gpt-5.6-luna')
        self.llm = ChatOpenAI(api_key=self.api_key, model=self.model_name)

        self.prompt = ChatPromptTemplate.from_messages([
            ('system', "You are a helpful AI assistant. You provide clear, accurate, and helpful responses. You can communicate in Korean or English based on the user's preference. Be conversational and friendly."),
            MessagesPlaceholder(variable_name='history'),
            ('human', '{input}')
        ])

        self.chain = self.prompt | self.llm

        self.session_stores: Dict[str, InMemoryChatMessageHistory] = {}

        self.runnable_with_history = RunnableWithMessageHistory(
            self.chain,
            self.get_session_history,
            input_messages_key='input',
            history_messages_key='history'
        )

        logger.info(f'Langchain service init complete = model: {self.model_name}')

    def get_session_history(self, session_id: str) -> BaseChatMessageHistory:
        if session_id not in self.session_stores:
            self.session_stores[session_id] = InMemoryChatMessageHistory()
            logger.info(f'Create session conversation log: {session_id}')

        return self.session_stores[session_id]

    async def get_chat_response(self, message: str, session_id: str = 'default') -> str:
        try:
            logger.info(f'Session {session_id} OPENAI message: {message[:50]}...')

            response = await self.runnable_with_history.ainvoke(
                {'input': message},
                config={'configurable': {'session_id': session_id}}
            )
            bot_response = response.content
            logger.info(f'Session {session_id} response: {bot_response[:50]}...')

            return bot_response
        
        except Exception as e:
            logger.error(f'Chat response Error {str(e)}')
            raise Exception(f'AI response fail: {str(e)}')

    def clear_session_memory(self, session_id: str) -> bool:
        if session_id in self.session_stores:
            del self.session_stores[session_id]
            logger.info(f'Delete session conversation log: {session_id}')
            return True
        return False

    def get_chat_history_for_display(self, session_id: str) -> List[Dict]:
        if session_id not in self.session_stores:
            return []
        
        chat_history = self.session_stores[session_id]
        messages = chat_history.messages

        history = []
        for msg in messages:
            if msg.type == 'human':
                history.append({'type': 'user', 'content': msg.content})
            if msg.type == 'ai':
                history.append({'type': 'assistant', 'content': msg.content})
        
        return history

    def set_history(self, session_id: str, items: List[dict]) -> int:
        """DB에서 불러온 대화 이력을 세션에 주입 (페이지 새로고침 후 연속 대화 지원)"""
        self.session_stores[session_id] = InMemoryChatMessageHistory()
        loaded = 0
        for item in items:
            try:
                msg_type = (item.get("type") or "").lower()
                content = item.get("content") or ""
                if not content:
                    continue
                if msg_type in ("human", "user"):
                    self.session_stores[session_id].add_user_message(content)
                    loaded += 1
                elif msg_type in ("ai", "assistant"):
                    self.session_stores[session_id].add_ai_message(content)
                    loaded += 1
            except Exception as e:
                logger.warning(f'Pass wrong session {session_id} log: {str(e)}')
        logger.info(f'Complete loading {loaded} message session {session_id}')
        return loaded


chat_service = LangChainChatService()
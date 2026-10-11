from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chat_models import init_chat_model
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.messages import AIMessage, HumanMessage, BaseMessage

from dotenv import load_dotenv
import os

from .models import ChatMessage

load_dotenv()

class DatabaseChatMessageHistory(BaseChatMessageHistory):
    def __init__(self, session_id):
        self.session_id = session_id

    @property
    def messages(self):
        chat_messages: list[ChatMessage] = ChatMessage.objects.filter(session_id=self.session_id)

        messages = []
        for chat_message in chat_messages:
            if chat_message.message_type == 'human':
                messages.append(HumanMessage(content=chat_message.content))
            else:
                messages.append(AIMessage(content=chat_message.content))

        return messages

    def add_message(self, message: BaseMessage):
        if isinstance(message, HumanMessage):
            message_type = 'human'
        else:
            message_type = 'ai'

        ChatMessage.objects.create(
            session_id=self.session_id,
            message_type=message_type,
            content=message.content
        )

    def clear(self):
        ChatMessage.objects.filter(session_id=self.session_id).delete()


prompt = ChatPromptTemplate.from_messages([
    ('system', '넌 IT분야의 직업상담사 챗봇임'),
    MessagesPlaceholder(variable_name='history'),
    ('human', '{query}')
])

def get_by_session_id(session_id):
    return DatabaseChatMessageHistory(session_id)

llm = init_chat_model('gpt-5.6-luna')
chain = prompt | llm
chain_with_history = RunnableWithMessageHistory(
    chain,
    get_session_history=get_by_session_id,
    input_messages_key='query',
    history_messages_key='history'
)

def invoke_chain_with_history(session_id, query):
    return chain_with_history.invoke({
        'query': query
    }, config = {
        'configurable': {
            'session_id': session_id
        }
    })
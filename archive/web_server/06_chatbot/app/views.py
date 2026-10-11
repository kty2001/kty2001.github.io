import uuid
import json
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET, require_http_methods
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseNotFound, Http404
from django.shortcuts import render
from .models import ChatMessage
from .chatbot_service import get_by_session_id, invoke_chain_with_history

def index(request):
    return render(request, 'app/index.html')

@csrf_exempt
@require_POST
def init_conversation(request):
    session_id = str(uuid.uuid4())
    return JsonResponse({
        'session_id': session_id
    })

@csrf_exempt
@require_POST
def chatbot(request):
    session_id = request.POST.get('session_id')
    print(session_id)
    query = request.POST.get('query')

    if not session_id or not query:
        return HttpResponseBadRequest('Required session_id or question')

    response = invoke_chain_with_history(session_id, query)
    return JsonResponse({
        'content': response.content
    })

@csrf_exempt
@require_http_methods(['DELETE'])
def remove_conversation(request):
    try:
        body = json.loads(request.body)
        session_id = body.get('session_id')
    except json.JSONDecodeError:
        return HttpResponseBadRequest('Wrong Json body format')

    if not ChatMessage.objects.filter(session_id=session_id).exists():
        raise Http404('Not Found session_id')

    history = get_by_session_id(session_id)
    history.clear()

    return JsonResponse({
        'result': 'success',
        'message': f'Del conversation session_id: {session_id}'
    })

@require_GET
def get_session_list(request):
    from django.db.models import Min, Max, Count

    sessions = ChatMessage.objects.values('session_id').annotate(
        first_message_time = Min('created_at'),
        last_message_time = Max('created_at'),
        message_count = Count('id'),
    )

    session_list = []
    for session in sessions:
        first_message = ChatMessage.objects.filter(session_id=session['session_id']).first()

        session_list.append({
            'session_id': session['session_id'],
            'first_message_preview': first_message.content,
        })

    return JsonResponse({
        'sessions': session_list,
        'total_sessions': len(session_list),
    })

@csrf_exempt
@require_POST
def restore_conversation(request):
    try:
        body = json.loads(request.body)
        session_id = body.get('session_id')
    except json.JSONDecodeError:
        return HttpResponseBadRequest('Wrong json format')

    if not ChatMessage.objects.filter(session_id=session_id).exists():
        return HttpResponseNotFound('Not existed session')

    history = get_by_session_id(session_id)
    conversation_history = []
    for message in history.messages:
        conversation_history.append({
            'type': message.type,
            'content': message.content
        })

    return JsonResponse({
        'session_id': session_id,
        'conversation_history': conversation_history,
        'message_count': len(conversation_history)
    })
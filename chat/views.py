from django.shortcuts import render
from django.http import JsonResponse
from .models import Message
from django.views.decorators.csrf import csrf_exempt
import json

def chat_view(request):
    return render(request, 'chat.html')

def get_messages(request):
    messages = Message.objects.order_by('-timestamp')[:50]
    data = [
        {"user": m.username, "message": m.content, "timestamp": m.timestamp.strftime('%H:%M:%S')}
        for m in reversed(messages)
    ]
    return JsonResponse(data, safe=False)

@csrf_exempt
def post_message(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        Message.objects.create(username=data['username'], content=data['message'])
        return JsonResponse({'status': 'ok'})

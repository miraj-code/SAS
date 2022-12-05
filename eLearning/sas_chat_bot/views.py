from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt
import json
from sas_chat_bot.chat import get_response
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request, 'base.html')

@csrf_exempt
@xframe_options_exempt
def bot(request):
    data=json.loads(request.body)
    text = data['message']
    response = get_response(text)
    message = {"answer": response}
    
    return JsonResponse(message)
    

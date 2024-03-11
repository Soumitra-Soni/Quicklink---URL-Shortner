from django.shortcuts import render, redirect
from django.http import JsonResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def url_get(request):
    return JsonResponse('its working', safe=False)

def go(request, pk):
    return redirect('/')
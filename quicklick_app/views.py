from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest, JsonResponse
from .models import QuicklinkApp
import uuid
import json

# Create your views here.

# def index(request):
#     return render(request, 'index.html')

# def url_get(request):
#     if request.method == 'POST':
#         link = request.POST.get('link')
#         uid = str(uuid.uuid4())[0:5]

#         fetch_input = json.loads(request.body)
#         new_fetch_input = fetch_input['new_input_feild']
 
#         link = new_fetch_input
#         url_data = QuicklinkApp(link=link, uid=uid)

#         url_data.save()
#         return JsonResponse(uid, safe=False)
#     else:
#         return JsonResponse('Error', safe=False)

# def go(request, pk):
#     out_put = QuicklinkApp.objects.get(id=pk)
#     new_out_put = str(out_put.link)
#     return redirect('https://'+new_out_put)

def index(request):
    return render(request, 'index.html')

def url_get(request):
    if request.method == 'POST':
        try:
            fetch_input = json.loads(request.body)
            new_fetch_input = fetch_input.get('new_input_feild') 

            if new_fetch_input is None:
                return HttpResponseBadRequest("Invalid input")

            uid = str(uuid.uuid4())[:5]

            url_data = QuicklinkApp(link=new_fetch_input, uid=uid)
            url_data.save()

            return JsonResponse({'uid': uid})
        
        except json.JSONDecodeError:
            return HttpResponseBadRequest("Invalid JSON data")
        
    else:
        return HttpResponseBadRequest("Only POST method allowed")

def go(request, pk):
    try:
        out_put = QuicklinkApp.objects.get(uid=pk)
        new_out_put = str(out_put.link)
        return redirect('https://' + new_out_put)
    except QuicklinkApp.DoesNotExist:
        return HttpResponseBadRequest("Invalid ID")
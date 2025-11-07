from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.

def sample(request):
    return HttpResponse('hi')
def sample1(request):
    return HttpResponse('My Name is Sai Amruth')
def sample2(request):
    data={"name":"saiamruth","age":25,"place":"hyd"}
    return JsonResponse(data)
def sample3(request):
    data={"result":[2,4,6,8]}
    return JsonResponse(data)
def dynamic(request):
    name=request.GET.get("name",'')
    city=request.GET.get("city",'hyd')
    return HttpResponse(f"{name} from {city}")
 
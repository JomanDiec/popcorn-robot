from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.
def traverse(request):

    return render(request,'javascript/traverse.html')

def ajax(request):

    # name = request.POST["name"]
    # print(name)

    return render(request, 'ajax.html')

def name(request):
    names = json.loads(request.POST["names"])
    print(names[1])
    return HttpResponse(names[1])

def name_2(request):
  names = ["Lesley", "Emily"]
  return HttpResponse(json.dumps(names))

# def haunted_mansion(request):

#     return render(request,'javascript/haunted_mansion.html')
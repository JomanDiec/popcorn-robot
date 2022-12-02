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

def sally(request):
    person = json.loads(request.POST["person"])
    print(person['age'])
    return HttpResponse(person['age'])

def click_me(request):
    title = ["And change it to an AJAX title!"]

    return HttpResponse(json.dumps(title))

def make_list(request):
    animals = ["Elephant", "Giraffe", "Lion", "Pika"]

    return HttpResponse(json.dumps(animals))

def ajax_me(request):

    return HttpResponse()

# def haunted_mansion(request):

#     return render(request,'javascript/haunted_mansion.html')
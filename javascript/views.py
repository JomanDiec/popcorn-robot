from django.shortcuts import render
from django.http import HttpResponse
from javascript.models import *
import json

# Create your views here.
def traverse(request):

    return render(request,'javascript/traverse.html')

def ajax(request):
    ajax_check = AjaxMe.objects.get(id=1).checkbox

    context = { 'ajax_check' : ajax_check}
    return render(request, 'ajax.html', context)
    

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
    checkbox = AjaxMe.objects.get(id=1)
    if checkbox.checkbox == False:
        checkbox.checkbox = True
    else:
        checkbox.checkbox = False
    
    checkbox.save()
    print(checkbox.checkbox)

    return HttpResponse(json.dumps(checkbox.checkbox))

# function not in use
def ajax_check(request):
    ajax_check = AjaxMe.objects.get(id=1).checkbox
    print(ajax_check)
    
    return HttpResponse(json.dumps(ajax_check))

# def haunted_mansion(request):

#     return render(request,'javascript/haunted_mansion.html')
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):
    return HttpResponse('test')

def haunted_mansion(request):

    return render(request,'haunted_mansion/haunted_mansion.html')
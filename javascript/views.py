from django.shortcuts import render

# Create your views here.
def traverse(request):

    return render(request,'javascript/traverse.html')

def ajax(request):

    return render(request, 'ajax.html')

# def haunted_mansion(request):

#     return render(request,'javascript/haunted_mansion.html')
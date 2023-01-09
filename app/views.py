from django.shortcuts import render

# Create your views here.

def parent(request):
    return render(request,'parent.html')

def child1(request):
    return render(request,'child1.html')

def child2(request):
    return render(request,'child2.html')
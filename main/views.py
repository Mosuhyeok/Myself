from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def gs(request):
    return render(request,'gs.html')

def hiphop(request):
    return render(request,'hiphop.html')

def bal(request):
    return render(request,'bal.html')

    
def dance(request):
    return render(request,'dance.html')

def about(request):
    return render(request, 'about.html')
from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')
def register(request):
    return render(request, 'main/register.html')
def avtoris(request):
    return render(request, 'main/avtoris.html')
def game2(request):
    return render(request, 'main/game2.html')
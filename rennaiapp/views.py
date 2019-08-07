from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def indexfunc(request):
    return HttpResponse('Hello')

def signupfunc(request):
    return render(request, 'index.html', {'some':100})
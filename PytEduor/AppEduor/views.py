from urllib import request
from django.shortcuts import render

# Create your views here.
def inicioSeccion(request):
    return render(request , 'login.html')
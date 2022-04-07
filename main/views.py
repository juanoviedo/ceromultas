from django.http import response
from django.shortcuts import render

def inicio(response):
    return render(response, 'main/inicio.html', {})
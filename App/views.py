from django.shortcuts import render
from django.http import HttpResponse

def inprogres(request):
    return(HttpResponse("Página en construcción"))
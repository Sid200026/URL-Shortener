from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, reverse

# Create your views here.
def home(request):
    return render(request, 'urlgen/base.html')

def redirect(request, detail):
    return HttpResponse("Redirect")

def error(request):
    return HttpResponse("Error")


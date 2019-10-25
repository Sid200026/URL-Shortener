from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, reverse, redirect
import string 
import random
from .models import url

# Create your views here.
def home(request):
    if request.method == 'POST':
        bigurl = request.POST.get('bigurl')
        shorturl = request.POST.get('shorturl') # None if empty
        if shorturl == None:
            if url.objects.filter(big_url = bigurl).exists():
                urlobj = url.objects.filter(big_url = bigurl)[0]
                return HttpResponseRedirect('{0}'.format(urlobj.short_url))
        else:
            if not url.objects.filter(short_url = shortcut).exists():
                url.objects.create(big_url = bigurl, short_url = shortcut)
                return HttpResponseRedirect('{0}'.format(shortcut))
        notunique = True
        while(notunique):
            res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 5)) 
            if url.objects.filter(short_url = res).exists():
                pass
            else:
                shortcut = res
                break
        url.objects.create(big_url = bigurl, short_url = shortcut)
        return HttpResponseRedirect('{0}'.format(shortcut))
    return render(request, 'urlgen/home.html')

def redirect(request, detail):
    return render(request, 'urlgen/redirect.html')

def error(request):
    return render(request, 'urlgen/error.html')


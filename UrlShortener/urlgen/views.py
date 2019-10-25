from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, reverse, redirect
import string 
import random
from .models import url

# Create your views here.
def home(request):
    if request.method == 'POST':
        urltest = None
        try:
            bigurl = request.POST.get('bigurl')
            if bigurl[0:5]!='https':
                bigurl = 'https://'+bigurl
            shortcut = request.POST.get('preferred') # None if empty
            if not shortcut:
                if url.objects.filter(big_url = bigurl).exists():
                    urlobj = url.objects.filter(big_url = bigurl)[0]
                    return HttpResponseRedirect('redirect/{0}'.format(urlobj.short_url))
            else:
                if not url.objects.filter(short_url = shortcut).exists():
                    url.objects.create(big_url = bigurl, short_url = shortcut)
                    urltest = url.objects.get(short_url = shortcut)
                    urltest.full_clean()
                    return HttpResponseRedirect('redirect/{0}'.format(shortcut))
                else:
                    print(shortcut)
                    return render(request, 'urlgen/home.html', {'error':'The path has already been taken'})
            notunique = True
            while(notunique):
                res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 5)) 
                if url.objects.filter(short_url = res).exists():
                    pass
                else:
                    shortcut = res
                    break
            url.objects.create(big_url = bigurl, short_url = shortcut)
            urltest = url.objects.get(short_url = shortcut)
            urltest.full_clean()
            return HttpResponseRedirect('redirect/{0}'.format(shortcut))
        except:
            urltest.delete()
            return render(request, 'urlgen/home.html', {'error':'Not an URL'})
    return render(request, 'urlgen/home.html')

def redirect(request, detail):
    shorturl = detail
    urlobj = url.objects.get(short_url = shorturl)
    return render(request, 'urlgen/redirect.html', {'url':urlobj})

def error(request):
    return render(request, 'urlgen/error.html')

def bigredirect(request, detail):
    if not url.objects.filter(short_url = detail).exists():
        return HttpResponseRedirect(reverse('urlgen:error'))
    else:
        urlobj = url.objects.get(short_url = detail)
        return HttpResponseRedirect("{0}".format(urlobj.big_url))

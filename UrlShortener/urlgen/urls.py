from django.urls import path, re_path
from . import views

app_name = 'urlgen'

urlpatterns = [
    path('', views.home, name = "home"),
    path('error', views.error, name = "error"),   
    path('<slug:detail>', views.bigredirect, name = "bigredirect"),  
    path('redirect/<slug:detail>', views.redirect, name = "redirect"),   
]

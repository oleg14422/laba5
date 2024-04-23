from django.urls import path
from . import views

urlpatterns = [path('', views.mainPage, name='home'),
               path('diff', views.diffPage, name='diff'),
               path('diffapi', views.getdiffAPI, name='getdiffapi'),
               path('message', views.sendMessagePage, name='sendmessage'),
               path('cisco', views.ciscoPage, name='cisco'),
               path('site', views.sitePage, name='Site')
]
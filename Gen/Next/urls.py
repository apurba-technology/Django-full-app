from django.conf.urls import url

from Next import views

urlpatterns = [
    url('', views.index,name='index'),
   
]
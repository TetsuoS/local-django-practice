from django.urls import path
from . import views

app_name = 'formdemo'

urlpatterns = [
    path('', views.formdemo_list, name='formdemo_list'),
]
from django.urls import path
from . import views

app_name = 'formdemo'

urlpatterns = [
    path('', views.formdemo_top, name ='formdemo_top'),
    path('create/', views.formdemo_create, name='formdemo_create'),
    path('detail/<int:pk>/', views.formdemo_detail, name='formdemo_detail'),
#    path('update/<int:pk>/', views.formdemo_update, name='formdemo_update'),
    path('update/', views.formdemo_update, name='formdemo_update'),
    path('delete/', views.formdemo_delete, name='formdemo_delete'),
]
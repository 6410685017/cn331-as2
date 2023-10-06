from django.urls import path
from . import views

app_name = 'regist'

urlpatterns = [
    path('sublist/', views.sublist, name='sublist'),
    path('enroll/<str:sub_id>', views.enroll, name='enroll'),
    
]
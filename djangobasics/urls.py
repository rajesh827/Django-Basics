from django.contrib import admin  
from django.urls import path
from djangolab import views

urlpatterns = [
    path('admin/', admin.site.urls), #Q1
    path('login/', views.login_view, name='login'), #Q1
    path('dashboard/', views.dashboard_view, name='dashboard'), #Q1
    path('add-patient/', views.add_patient, name='add_patient'), #Q2
    path('register/', views.register_view, name='register'), #Q3
    path('upload/', views.upload_view, name='upload'), #Q4
    path('submit-project/', views.submit_project, name='submit_project'), #Q5
]
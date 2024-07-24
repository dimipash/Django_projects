from django.contrib import admin
from django.urls import path
from my_app import views

urlpatterns = [
    path("admin/", admin.site.urls),    
    path('', views.index, name='index'),
    path('delete/<int:task_id>/', views.delete, name='delete'),
]

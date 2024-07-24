from django.contrib import admin
from django.urls import path
from my_app import views

urlpatterns = [
    path("admin/", admin.site.urls),    
    path('', views.index, name='index'),
    path('delete/<int:task_id>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path("cbv-index/", views.TaskListView.as_view(), name='cbv-index'),
    path("cbv-detail/<int:pk>/", views.TaskDetailView.as_view(), name='cbv-detail'),
    path("cbv-update/<int:pk>/", views.TaskUpdateView.as_view(), name='cbv-update'),
    path("cbv-delete/<int:pk>/", views.TaskDeleteView.as_view(), name='cbv-delete'),
]

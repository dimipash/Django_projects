from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.hello_world, name="hello_world"),
    path("health/", views.health_check, name="health_check"),
]

from django.contrib import admin
from django.urls import path
from new_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', views.movie_list, name='movie_list'),
]

from django.contrib import admin
from django.urls import path
from shop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('<int:id>', views.detail, name='detail'),
    path('checkout/', views.checkout, name='checkout'),
]

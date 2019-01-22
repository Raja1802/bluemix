from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="home"),
    path('all_images/', views.all_images, name="all_images"),
]
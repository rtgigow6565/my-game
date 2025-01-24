from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('game/', views.game, name='game'),
    path('blog/', views.blog, name='blog'),
    path('news/', views.news, name='news'),
    path('roadmap/', views.roadmap, name='roadmap'),
]

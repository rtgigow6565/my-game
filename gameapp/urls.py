from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt
import os

urlpatterns = [
    path('', views.home, name='home'),
    path('game/', views.game, name='game'),
    path('blog/', views.blog, name='blog'),
    path('news/', views.news, name='news'),
    path('roadmap/', views.roadmap, name='roadmap'),
    path('rating/', views.radingame, name='rating'),
]

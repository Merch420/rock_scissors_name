from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('register', views.register, name='register'),
    path('avtoris', views.avtoris, name='avtoris'),
    path('game2', views.game2, name='game2')
]

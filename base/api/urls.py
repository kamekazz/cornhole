from django.urls import path
from . import controllers

urlpatterns = [
    path('', controllers.getRoute),
    path('rooms/', controllers.getRooms),
    path('room/<str:pk>', controllers.getRoom),
]

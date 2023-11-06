from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexed, name='index'),
    path("informacion", views.get_agent, name="info_dispositivo"),
    path("infoUser", views.info_agent, name="info_user_agent"),
]
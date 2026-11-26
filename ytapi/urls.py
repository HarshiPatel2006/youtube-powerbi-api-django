from django.urls import path

from . import views

urlpatterns = [
    path("", views.home),
    path("api/channel_id", views.get_channel_id),
    path("api/data", views.get_data),
]

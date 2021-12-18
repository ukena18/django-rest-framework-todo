from django.urls import path

from . import views


urlpatterns = [
    # this is for home page
    path("", views.list, name='list')
]





from django import views
from django.urls import path

from . import views


app_name = "shortener"

urlpatterns = [
    path("", views.index),
    path("<slug:slug>/", views.shorted_url_redirect)
]
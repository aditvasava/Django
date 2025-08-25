from django.urls import path

from . import views

# This is the normal syntax, nothing to be memorized
urlpatterns = [
    # whenever the url is challenges/january, execute the index function in views.py file
    path("january", views.index),
    path("february", views.feb)
]

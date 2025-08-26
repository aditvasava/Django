from django.urls import path

from . import views

# This is the normal syntax, nothing to be memorized
urlpatterns = [
    # whenever the url is challenges/january, execute the january function in views.py file
    # path("january", views.january),
    # path("february", views.february),

    path("", views.index, name="index"), # localhost:8000/challenges will be handled by views.index function

    # <> is used for dynamic urls
    path("<int:month>", views.monthly_challenge_by_number), # for routes - challenges/1 , challenges/2 ...

    # the name parameter is used to give a name to this url. So basically, the parent url is localhost:8000/challenge. If there
    # is a change at the root level, say localhost:8000/challenges, then all the nested routes will be broken, so to avoid this issue
    # we give a name to the url like below, and then in the views.py, we can get the url
    path("<str:month>", views.monthly_challenge, name="month-challenge") # for routes - challenges/january , challenges/february
]

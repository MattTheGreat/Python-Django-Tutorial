from django.conf.urls import url
from . import views

"""
If a user request Main he will brought here where the server
will again look for the specific url after Main

If nothing else is requested the user will then be directed to
index page.

If a url is requested that does not exist the user will then be
directed to an error page.

"""
urlpatterns = [
    url(r'^$', views.index, name='index'),
]

from django.conf.urls import include, url
from django.contrib import admin


"""These are request and response urls
When a user connects to the server and requests a url
the server will look here to see what to do when a particular
url is requested.

"""
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^Main/', include('Main.urls')),

]

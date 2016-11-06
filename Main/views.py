from django.http import HttpResponse
"""
This page is like a controller in the MVC
its shows a particular view and basically controls the flow
of information on this page.
"""
def index(request):
    return HttpResponse("<h1>This Is The Home Page")

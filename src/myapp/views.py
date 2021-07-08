from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>My Home Page App<h1>")

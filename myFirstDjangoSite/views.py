from django.http import HttpResponse


def hello(request):
    return HttpResponse("Hello world")


def homePage(request):
    return HttpResponse("This is the home page!")

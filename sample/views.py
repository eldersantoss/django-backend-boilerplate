from django.http.request import HttpRequest
from django.http.response import HttpResponse


def hello_world(request: HttpRequest):

    if request.method == "GET":
        return HttpResponse("Hello, world!!!")
    elif request.method == "POST":
        return HttpResponse("Hello, world!!!")

    return HttpResponse("Hello, world!!!")

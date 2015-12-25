from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext


def index(request):
    return render(request, "ask_app/index.html")


def registration(request):
    return render(request, "ask_app/registration.html")


def handle_wsgi_get_post(request):
    response = 'Hello world <br>'
    for key, value in request.GET.items():
        response = response + str(key) + " : " + str(value) + "<br>"
    for key, value in request.POST.items():
        response = response + str(key) + " : " + str(value) + "<br>"
    return HttpResponse(response)

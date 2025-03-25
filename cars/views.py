from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("List of cars")

def car(request, car_id):
    return HttpResponse("Description of single car")

def category(request, category_id):
    return HttpResponse("List of cars from single category")
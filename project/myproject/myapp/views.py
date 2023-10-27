from django.shortcuts import render
from django.http import HttpResponse
     

# Create your views here.
def drinks(request, drink_name):
    drink = {'mocha': 'type of coffee', 'tea': 'type of beverage', 'lemonade': 'type of refreshment'}
    choice_of_drink = drink.get(drink_name, 'unknown')
    response = f"<h2> {drink_name} </h2> {choice_of_drink}"
    return HttpResponse(response)

def home(request):
    return HttpResponse('welcome to little lemon!')

def about(request):
    return HttpResponse('about us')

def menu(request):
    return HttpResponse('menu')

def book(request):
    return HttpResponse('make a booking')


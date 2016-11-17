from django.shortcuts import render, redirect, HttpResponse



def index(request):
    return render(request, 'turtles/index.html')

def all(request):
    ninjas = 'all_turtles'
    context = {
    'turtle':ninjas
    }
    return render(request, 'turtles/show.html', context)

def show(request, color):
    if color == 'purple':
        donatello = 'donatello'
        context = {
        'ninja': color,
        'turtle': donatello
        }
    if color == 'orange':
        mike = 'michaelangelo'
        context = {
        'ninja': color,
        'turtle': mike
        }
    if color == 'blue':
        leonardo = 'leonardo'
        context = {
        'ninja': color,
        'turtle': leonardo
        }
    if color == 'red':
        raphael = 'raphael'
        context = {
        'ninja': color,
        'turtle': raphael
        }
    else:
        megan = 'megan_fox'
        context = {
        'turtle': megan
        }
    return render(request, 'turtles/show.html', context)

# Create your views here.

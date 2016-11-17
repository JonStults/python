from django.shortcuts import render, redirect, HttpResponse
from . import models

def index(request):
    classes = models.Courses.objects.all()
    context = {
        'classes':classes,
    }
    return render(request, 'addcourse/index.html', context)

def show(request):
    models.Courses.objects.create(name = request.POST['name'], description = request.POST['description'])
    return redirect('/')

def remove(request, id):
    classy = models.Courses.objects.get(id = id)
    context = {
        'classy' : classy
    }
    return render(request, 'addcourse/remove.html', context)

def no(request):
    return redirect('/')

def yes(request, id):
    models.Courses.objects.filter(id=id).delete()
    return redirect('/')

# Create your views here.

import random
from django.shortcuts import render, HttpResponse, redirect
a = ['coding', 'sometimes', 'hard']
def index(request):
    attempt = request.session['count']
    word = (random.choice(a))
    context = {
    'word' : word,
    'count': attempt
    }
    return render(request, 'rando/index.html', context)

def show(request):
    if 'count' in request.session:
        request.session['count'] += 1
    else:
        request.session['count'] = 1
        context = {}
    return redirect('/')





# Create your views here.

from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, 'survey/index.html')

def process(request):
    print 'hello'
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    context = {}
    return redirect('/result')

def result(request):
    context = {
    'name' : request.session['name'],
    'location' : request.session['location'],
    'language' : request.session['language'],
    'comment' : request.session['comment']
    }
    return render(request, 'survey/info.html', context)


# Create your views here.

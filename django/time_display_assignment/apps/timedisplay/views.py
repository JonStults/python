from django.shortcuts import render, HttpResponse
from datetime import datetime
date = datetime.now().date()
time = datetime.now().time()
def index(request):
    context = {
    "Date": date,
    "Time": time
    }
    return render(request, 'timedisplay/index.html', context)
# Create your views here.

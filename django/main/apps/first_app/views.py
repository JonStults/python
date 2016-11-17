from django.shortcuts import render, HttpResponse
# CONTROLLER!!
def index(request):
    print ('*'*100)
    # response = "Hello, I am your first request!"
    return render(request, 'first_app/index.html')

# Create your views here.

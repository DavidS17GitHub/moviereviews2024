from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    searchTerm = request.GET.get('searchMovie')
    return render(request, 'home.html', {'searchTerm':searchTerm})


def about(request):
    return HttpResponse('<h1>About Page</h1>')

def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email': email})
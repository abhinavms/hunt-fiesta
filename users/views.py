from django.shortcuts import render, redirect

# Create your views here.

def index_page(request):
    return render(request, "index.html")
            
def about_page(request):
    return render(request, "about.html")

def login_page(request):
    return render(request, "login.html")
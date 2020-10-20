from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from users.models import CustomUser

def index_page(request):
    return render(request, "index.html")
            
def about_page(request):
    return render(request, "about.html")

def login_page(request):
    if request.user.is_authenticated:
        request.session.flush()
        return render(request, "login.html")

    else:
        if request.method == 'POST':
            email  = request.POST.get('email')
            password  = request.POST.get('password')
            print(email, password)
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("hunt")
            else:
                request.session.flush()
                return render(request, "login.html", {'error' : 'Incorrect email or password.'})
        else:
            return render(request, "login.html")
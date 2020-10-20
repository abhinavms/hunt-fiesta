from django.shortcuts import render, redirect
from users.models import CustomUser

def hunt_page(request):
    if request.user.is_authenticated:
        email = request.user
        try:
            user = CustomUser.objects.get(email=email)
            return render(request, "hunt.html")
        except:
            request.session.flush()
            return redirect("/")
    else:
        request.session.flush()
        return redirect("/")            

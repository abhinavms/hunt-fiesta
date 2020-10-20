from django.shortcuts import render, redirect

def hunt_page(request):
    return render(request, "clue.html")
            
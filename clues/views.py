from django.shortcuts import render, redirect
from users.models import CustomUser
from .models import Level

def hunt_page(request):
    if request.user.is_authenticated:
        email = request.user
        try:
            user = CustomUser.objects.get(email=email)
        except:
            request.session.flush()
            return redirect("/")

        if request.method == 'POST':
            if (request.POST.get('answer') == Level.objects.get(no=user.level).answer):
                user.level += 1
                user.save()
            return redirect("hunt")

        totalLevel = len(Level.objects.filter())
        if (user.level > totalLevel):
            return render(request, "congrats.html")
        else:
            context = {}
            level = Level.objects.get(no = user.level)
            context['no'] = level.no
            if hasattr(level, 'text'):
                context['text'] = level.text
            if level.picture and hasattr(level.picture, 'url'):
                context['picture'] = level.picture.url
            if hasattr(level, 'hiddenHTML') and level.hiddenHTML != "":
                context['hiddenHTML'] = level.hiddenHTML
            # print(context)
            return render(request, "hunt.html", context)
    else:
        request.session.flush()
        return redirect("/")            

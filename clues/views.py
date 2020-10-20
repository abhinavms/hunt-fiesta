from django.shortcuts import render, redirect
from users.models import CustomUser, Logs
from .models import Level
from django.utils import timezone

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        print ("returning FORWARDED_FOR")
        ip = x_forwarded_for.split(',')[-1].strip()
    elif request.META.get('HTTP_X_REAL_IP'):
        print ("returning REAL_IP")
        ip = request.META.get('HTTP_X_REAL_IP')
    else:
        print ("returning REMOTE_ADDR")
        ip = request.META.get('REMOTE_ADDR')
    return ip


def hunt_page(request):
    if request.user.is_authenticated:
        email = request.user
        try:
            user = CustomUser.objects.get(email=email)
        except:
            request.session.flush()
            return redirect("/")

        if request.method == 'POST':
            log = Logs.objects.create(user=user)
            # log.user = CustomUser.objects.get(email=email)
            log.level = user.level
            log.text = request.POST.get('answer')
            log.ip_address = get_client_ip(request)
            log.datetime = timezone.localtime()
            log.save()
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

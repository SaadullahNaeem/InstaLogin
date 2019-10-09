from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
def login(request):
    return render(request, 'login.html')


@login_required
def home(request):
    context = dict()
    try:
        context['user_data'] = request.user.social_auth.first().extra_data
    except:
        pass
    return render(request, 'home.html', context=context)

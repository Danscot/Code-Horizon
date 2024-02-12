from .models import Profile

from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.

from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def user_page(request):

    user = request.user

    user_profile = Profile.objects.get(user=user)

    if request.method == 'POST':

        bio = request.POST['bio']

        user_profile.bio = bio

        user_profile.save()

        if request.FILES.get('image') is None:

            image = user_profile.profileimg

            user_profile.profileimg = image

            bio = request.POST['bio']

            user_profile.bio = bio

        if request.FILES.get('image') is not None:

            image = request.FILES.get('image')

            user_profile.profileimg = image

            bio = request.POST['bio']

            user_profile.bio = bio

            user_profile.save()

        return redirect('user_page')

    context1 = {'user': user}

    context2 = {'user_profile': user_profile}

    context = {

        'context1': context1,

        'context2': context2
    }

    return render(request, 'profile.html', context)


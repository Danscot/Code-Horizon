from django.contrib.auth import authenticate, login

from django.contrib.auth.models import User

from django.shortcuts import render, redirect

from django.contrib import messages, auth

from django.contrib.auth.decorators import login_required

from django.http import HttpResponse

from profile_page.models import Profile


def signin(request):

    if request.method == "POST":

        username = request.POST['username']

        password = request.POST['password']

        email = request.POST['email']

        password1 = request.POST['password1']

        if password == password1:

            if User.objects.filter(username=username).exists():

                messages.info(request, 'Username Already Exist')

                return redirect('sign')

            else:

                user = User.objects.create_user(username, email, password)

                user.save()

                user_model = User.objects.get(username=username)

                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)

                new_profile.save()

                return redirect('login')

        else:

            messages.info(request, 'Password Not Matching')

            return redirect('sign')

    return render(request, "sign.html")


def log_in(request):

    if request.method == "POST":

        username = request.POST['username']

        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        new_profile = Profile.objects.get(user=user)

        error = """

                           You Have Enter Wrong Credidential\n

                               Login To View Your Profile

                           """
        if user is not None:

            login(request, user)

            return redirect("home")

        else:

            messages.error(request, error)

            return redirect("login")

    return render(request, "login.html")


def logout(request):

    auth.logout(request)

    return redirect('sign')


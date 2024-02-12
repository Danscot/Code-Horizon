from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

from profile_page.models import Profile


from .models import Post, LikePost, FollowersCount


# Create your views here.


@login_required(login_url='login')
def home(request):

    user = request.user

    user_profile = Profile.objects.get(user=user)

    posts = Post.objects.all()

    context1 = {'user': user}

    context2 = {'user_profile': user_profile}

    context3 = {'posts': posts}

    context = {

        'context1': context1,

        'context2': context2,

        'context3': context3,
    }

    if request.method == 'POST':

        image = request.FILES.get('image_upload')

        caption = request.POST['caption']

        new_post = Post.objects.create(user=user.username, image=image, caption=caption)

        new_post.save()

    return render(request, 'home.html', context)


def like_post(request):

   username = request.user.username

   post_id = request.GET.get('post_id')

   post = Post.objects.get(id=post_id)

   like_filter = LikePost.objects.filter(post_id=post_id, username=username).first()

   if like_filter is None:

       new_like = LikePost.objects.create(post_id=post_id, username=username)

       new_like.save()

       post.no_of_likes = int(post.no_of_likes) + 1

       post.save()

       return redirect('home')

   else:

       like_filter.delete()

       post.no_of_likes = int(post.no_of_likes) - 1

       post.save()

       return redirect('home')


@login_required(login_url='login')
def follow(request):

    if request.method == 'POST':

        follower = request.POST['follower']

        user = request.POST['user']

        if FollowersCount.objects.filter(follower=follower, user=user).first():

            delete_follower = FollowersCount.objects.get(follower=follower, user=user)

            delete_follower.delete()

            return redirect('/profile/' + user)

        else:

            new_follower = FollowersCount.objects.create(follower=follower, user=user)

            new_follower.save()

            return redirect('/profile/' + user)

    else:

        return redirect('home')


@login_required(login_url='login')
def profile(request, pk):

    user_obj = User.objects.get(username=pk)

    user_profile = Profile.objects.get(user=user_obj)

    user_posts = Post.objects.filter(user=pk)

    user_post_length = len(user_posts)

    folllower = request.user.username

    user = pk
    if FollowersCount.objects.filter(follower=folllower, user=user):

        button_text = 'Unfollow'

    else:

        button_text = 'Follow'

    user_followers = len(FollowersCount.objects.filter(user=pk))

    user_following = len(FollowersCount.objects.filter(follower=pk))

    context = {

        'user_obj': user_obj,
        'user_profile': user_profile,
        'user_posts': user_posts,
        'user_post_length': user_post_length,
        'button_text': button_text,
        'user_following': user_following,
        'user_followers': user_followers,

    }

    return render(request, 'user_view.html', context)


def search(request):








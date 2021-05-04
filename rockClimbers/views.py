from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Post
from .models import Comment
from django.http import HttpResponseRedirect
from django.urls import reverse
import re


def home(request):
    """
    Takes users to the create_post.html page
    This function is called often
    """
    return render(request, 'create_post.html', {"posts": Post.objects.all()})


def create_post(request):
    print(request.POST)
    """
    View to create_post with input validation
    """
    if not request.POST.get("username") or \
            not re.match(r"^[a-zA-Z0-9_-]{3,15}$", request.POST["username"]):
        return render(request, 'create_post.html', {"posts": Post.objects.all(),
                                                    "error": "WARNING: "
                                                             "Username cannot "
                                                             "be empty and "
                                                             "must "
                                                             "be "
                                                             "between 3-15 "
                                                             "characters and "
                                                             "cannot contain "
                                                             "special "
                                                             "characters"})
    elif not request.POST.get("title"):
        return render(request, 'post-detail.html', {"post": Post.objects.all(),
                                                    "error": "Title cannot be "
                                                             "empty"})
    elif not request.POST.get("body"):
        return render(request, 'post-detail.html', {"post": Post.objects.all(),
                                                    "error": "Body cannot be "
                                                             "empty"})
    elif not request.POST.get("date"):
        return render(request, 'post-detail.html', {"post": Post.objects.all(),
                                                    "error": "Date cannot be "
                                                             "empty"})

    Post.objects.create(title=request.POST["title"], date=request.POST[
        "date"], body=request.POST["body"], username=request.POST["username"])
    return HttpResponseRedirect(reverse('home'))


def create_comment(request, post_id):
    # checking that the username is atleast more than 3 characters
    # and less than 15
    # input validation on comments
    if not request.POST.get("username") or \
            not re.match(r"^[a-zA-Z0-9_-]{3,15}$", request.POST["username"]):
        return render(request, 'post-detail.html', {"post": Post.objects.get(
            id=post_id), "error": "WARNING: Username cannot be empty and must "
                                  "be "
                                  "between 3-15 characters and cannot contain "
                                  "special characters"})
    elif not request.POST.get("title"):
        return render(request, 'post-detail.html', {"post": Post.objects.get(
            id=post_id), "error": "Title cannot be empty"})
    elif not request.POST.get("body"):
        return render(request, 'post-detail.html', {"post": Post.objects.get(
            id=post_id), "error": "Body cannot be empty"})
    elif not request.POST.get("date"):
        return render(request, 'post-detail.html', {"post": Post.objects.get(
            id=post_id), "error": "Date cannot be empty"})
    Comment.objects.create(title=request.POST["title"], date=request.POST[
        "date"], body=request.POST["body"], username=request.POST["username"],
                           post_id=post_id)
    return HttpResponseRedirect(reverse('post-detail', args=[post_id]))


def post_detail(request, post_id):
    """
    This function is called when a user clicks on the link to a certain post
    :param request:
    :param post_id: This param is used to get the post that the user
    specified/clicked

    :return: The return is an html template of the post
    """
    return render(request, 'post-detail.html', {"post": Post.objects.get(
        id=post_id)})

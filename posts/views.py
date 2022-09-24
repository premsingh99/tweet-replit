from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm
# Create your views here.


def index(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

        else:
            return HttpResponseRedirect(form.errors.as_json())

     # get all the posts, limit to 20
    posts = Post.objects.all()[:20]
    return render(request, 'posts.html', {'posts': posts})


def delete(render, post_id):

    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')


def edit(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.errors.as_json())
    form = PostForm
    return render(request, 'edit.html', {'post': post, 'form': form})


def like(request, post_id):
    post = Post.objects.get(id=post_id)
    if post.like_count == 0:
        post.like_count = 1
        post.save()
    else:
        post.like_count = 0
        post.save()
    return HttpResponseRedirect('/')


def cancel(request):
    return HttpResponseRedirect('/')

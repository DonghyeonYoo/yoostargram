from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from posts.models import Post, Comment


def post_comments(request, pk):
    post = Post.objects.get(pk=pk)
    Post.comment_set.create(
        content=request.POST.get('contnet'),
    )

    return redirect(
        posts,
    )

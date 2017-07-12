from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404

import re
from django.db.models import Q

# Create your views here.
def post_list(request):

	posts = Post.objects.all() # the name of our querySet
	
	return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_index(request):
    post_list = Post.objects.order_by('published_date')
    context = {'post_list': post_list}

    return render(request, 'blog/index.html', context)
		
def post_search(request, search_key):
    print("get to views")
    search_post_list = Post.objects.filter(title__contains=search_key)
    context = {'search_post_list': search_post_list}
    return render(request, 'blog/post_search.html', context)
    
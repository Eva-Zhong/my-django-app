from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):

	posts = Post.objects.filter(title__contains='t') # the name of our querySet
	
	return render(request, 'blog/post_list.html', {'posts': posts})
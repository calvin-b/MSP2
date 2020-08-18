from django.shortcuts import render

# Create your views here.
from .models import Post

def index(request):
	posts = Post.objects.all();
	context={
		'judul':'Blog',
		'content':'Lorem Ipsum',
		'Posts':posts,
	}
	return render(request,'blog/index.html',context)

def detailPost(request,sinput):
	posts = Post.objects.get(slug=sinput)
	context={
		'judul':'Blog',
		'content':'Lorem Ipsum',
		'Posts':posts,
	}
	return render(request,'blog/detail.html',context)
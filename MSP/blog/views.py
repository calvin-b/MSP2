from django.shortcuts import render

# Create your views here.
from .models import Post

def index(request):
	posts = Post.objects.all();
	categories = Post.objects.values('category').distinct();
	context={
		'judul':'Blog',
		'content':'Lorem Ipsum',
		'Posts':posts,
		'Categories':categories,
	}
	return render(request,'blog/index.html',context)

def detailPost(request,sinput):
	posts = Post.objects.get(slug=sinput)
	categories = Post.objects.values('category').distinct();
	context={
		'judul':'Blog',
		'content':'Lorem Ipsum',
		'Posts':posts,
		'Categories':categories,
	}
	return render(request,'blog/detail.html',context)

def categoryPost(request,cinput):
	posts = Post.objects.filter(category=cinput)

	categories = Post.objects.values('category').distinct();

	context={
		'judul':'Blog',
		'content':'Category Filtered',
		'Posts':posts,
		'Categories':categories,
		'cf':cinput,
	}
	return render(request,'blog/category.html',context)
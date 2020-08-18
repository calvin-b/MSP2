from django.shortcuts import render

def index(request):
	context={
		'judul':'Home',
		'content':'Hallo Selamat Datang',
	}
	return render(request,'index.html',context)
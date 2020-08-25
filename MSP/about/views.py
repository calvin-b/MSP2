from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import ContactForm
from .models import ContactModel


def update(request, update_id):
	update_acc = ContactModel.objects.get(id=update_id)

	data = {
		'nama'				: update_acc.nama,
		'gender'			: update_acc.gender,
		'tanggal_lahir'		: update_acc.tanggal_lahir,
		'email'				: update_acc.email,
		'alamat'			: update_acc.alamat,
	}
	update_form = ContactForm(request.POST or None, initial=data, instance=update_acc)

	error = None
	if request.method == 'POST':
		if update_form.is_valid():
			update_form.save()

			return HttpResponseRedirect("/about/")
		else:
			error = update_form.errors

	context={
		'judul':'About - Update Contact',
		'subjudul':'Update Contact',
		'content':'Update Contact',
		'contact_form':update_form,
		'error':error,
	}
	return render(request,'about/create.html',context)


def delete(request, delete_id):
	ContactModel.objects.filter(id=delete_id).delete()
	return HttpResponseRedirect("/about/")


def index(request):
	contact_model=ContactModel.objects.all()

	context={
		'judul':'About',
		'subjudul':'Form Tutorial',
		'content':'Contact List',
		'contact_model':contact_model,
	}

	if request.method == 'POST':
		print("ini post")
		print(request.POST['nama'])
		print(request.POST['alamat'])
	else:
		print("ini get")
	return render(request,'about/index.html',context)

def create(request):
	contact_form=ContactForm(request.POST or None)
	error = None
	if request.method == 'POST':
		if contact_form.is_valid():
			contact_form.save()

			return HttpResponseRedirect("/about/")
		else:
			error = contact_form.errors

	context={
		'judul':'About - Create Contact',
		'subjudul':'Create Contact',
		'content':'Add Contact',
		'contact_form':contact_form,
		'error':error,
	}
	return render(request,'about/create.html',context)
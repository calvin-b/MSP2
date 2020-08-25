from django import forms

from .models import ContactModel

class ContactForm(forms.ModelForm):

	class Meta:
		tahun = range(1945,2020,1)
		model = ContactModel
		fields = [
			'nama',
			'gender',
			'tanggal_lahir',
			'alamat',
			'email',

		]

		labels = {
			'gender':'Jenis Kelamin',
			'alamat':'Alamat Rumah',
			'email':'Alamat Email',
		}

		widgets = {
			'nama': forms.TextInput(
				attrs={
					'class':'form-control',
					'placeholder':'Masukan nama lengkap anda',
				}
			),
			'gender':forms.RadioSelect(
				attrs={
					'class':'form-check-input',
				}
			),
			'tanggal_lahir': forms.SelectDateWidget(
				years=tahun,
				attrs = {
					'class':'form-control col-sm-2',
				}
			),
			'alamat': forms.Textarea,
			'email': forms.TextInput(
				attrs = {
					'class':'form-control',
					'placeholder':'Isi dengan Email anda',
				}
			),
		}

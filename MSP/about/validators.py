from django.core.exceptions import ValidationError

def validateNama(value):
	nama_input = value

	if nama_input == "Reza":
		message = "Maaf, " + nama_input + " tidak bisa diposting"
		raise ValidationError(message)
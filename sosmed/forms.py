from django import forms

from .models import instagram

class instagramform(forms.ModelForm):
	class Meta:
		model = instagram
		fields=[
			'nama_depan',
			'nama_belakang',
			'username',
			'context',
		]
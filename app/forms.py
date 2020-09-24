from django import forms
from .models import CadastroEgresso

class CadastroEgressoForm(forms.ModelForm):
	class Meta:
		model = CadastroEgresso
		#exclude = 
		fields =  '__all__'
			
	WIDGETS = [

	]
from django import forms
#Bibliotecas Country
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
#Bilioteca LocalFlavor
from django.contrib.localflavor
#My imports here
from .models import CadastroEgresso

YES_NO_CHOICES = [
	('nao', 'Não'),
	('sim', 'Sim'),
]

MERCADO_CHOICES = [
	('AF', 'Atuo na minha área de formação'),
	('AC', 'Atuo em área correlata à minha da formação'),
	('AD', 'Atuo em área diferente da minha formação'),
	('AP', 'Estou aposentado'),
	('NO', 'Não estou trabalhando'),
]

AREA_CHOICES = [
	('EngApp', 'Engenheiro de Aplicativos em Computação'),
	('EngEquip', 'Engenheiro de Equipamentos em Computação'),
	('EngSO', 'Engenheiros de Sistemas Operacionais em Computação'),
	('AdmDB', 'Administrador de Banco de Dados'),
	('AdmR', 'Administrador de Redes'),
	('AdmSO', 'Administrador de Sistemas Operacionais'),
	('AdmInfo', 'Administrador em Segurança da Informação'),
	('AnalDS', 'Analista de Desenvolvimento de Sistemas'),
	('AnalRCD', 'Analista de Redes e de Comunicação de Dados'),
	('AnalAuto', 'Analista de Sistemas de Automação'),
	('AnalSC', 'Analista de Suporte Computacional'),
	('AnalTI', 'Analista de Testes de Tecnologia da Informação'),
	('ArqTI', 'Arquiteto de Soluções de Tecnologia da Informação'),
	('Não atuo na área', 'Não trabalho na área de Ciência da Computação'),
]

TRABALHO_CHOICES = [
	('autonomo', 'Autônomo'),
	('empregado', 'Empregado'),
	('servidor', 'Servidor Público'),
	('empresario', 'Empresário'),
	]

INGRESSO_CHOICES = [
	('Sim, na área de Ciência da Computação', 'Sim, na área de Ciência da Computação'),
	('Sim, em uma área diferente', 'Sim, em uma área diferente'),
	('Não, estou com outras ideias para minha vida', 'Não, estou com outras ideias para minha vida')
]

class CadastroEgressoForm(forms.ModelForm):
	#Dados Pessoais
	pais = CountryField().formfield(widget=CountrySelectWidget())
	dataNascimento = generic.forms.DateField()
	#Dados Acadêmicos
	outraFormacao = forms.ChoiceField(choices=YES_NO_CHOICES, widget=forms.RadioSelect())
	#Dados Profissionais
	opcaoMercado = forms.ChoiceField(choices=MERCADO_CHOICES, widget=forms.RadioSelect())
	areaAtuacao = forms.ChoiceField(choices=AREA_CHOICES, widget=forms.RadioSelect())
	formaTrabalho = forms.ChoiceField(choices=TRABALHO_CHOICES, widget=forms.RadioSelect())
	ingressoPos = forms.ChoiceField(choices=INGRESSO_CHOICES, widget=forms.RadioSelect())

	class Meta:
		model = CadastroEgresso
		fields =  '__all__'

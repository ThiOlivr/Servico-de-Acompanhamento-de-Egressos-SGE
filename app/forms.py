from django import forms
from .models import CadastroEgresso


MERCADO_CHOICES = [
	('AF', 'Atuo na minha área de formação'),
	('AC', 'Atuo em área correlata à minha da formação'),
	('AD', 'Atuo em área diferente da minha formação'),
	('AP', 'Estou aposentado'),
	('NO', 'Não estou trabalhando'),
]

AREA_CHOICES = [
	('', '-------'), #Depois analisar se não há um jeito melhor de implementar
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
]

TRABALHO_CHOICES = [
		('autonomo', 'Autônomo'),
		('empregado', 'Empregado'),
		('servidor', 'Servidor Público'),
		('empresario', 'Empresário'),
		('outro', 'Outro')
	]

class CadastroEgressoForm(forms.ModelForm):

	opcaoMercado = forms.ChoiceField(choices=MERCADO_CHOICES, widget=forms.RadioSelect())
	areaAtuacao = forms.ChoiceField(choices=AREA_CHOICES, widget=forms.Select())
	formaTrabalho = forms.ChoiceField(choices=TRABALHO_CHOICES, widget=forms.RadioSelect())
	class Meta:
		model = CadastroEgresso
		fields =  '__all__'

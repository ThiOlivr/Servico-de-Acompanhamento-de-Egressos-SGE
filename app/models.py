from django.db import models
from django_countries.fields import CountryField
#Parâmetro de tradução para utilizãção do CountryField
def foo_bar(language):
   	translation.activate(language)
   	return [(translation.gettext(country.name), country.code) for country in countries]

# Create your models here.

class CadastroEgresso (models.Model):
	SEXO_CHOICES = [
		('M', 'Masculino'),
		('F', 'Feminino' ),
	]

	ESTADO_CHOICES = [
		('CE', 'Ceará'),
		('RN', 'Rio Grando do Norte'),
		('PE', 'Pernambuco'),
		('RS', 'Rio Grande do Sul'),
	]

	CURSO_CHOICES = [
		('BCC', 'Bach. Ciência da Computação'),
		('PPGCC', 'Pós-Graduação em Ciência da Computação'),
	]

	PERIODO_CHOICES = [
		('20201', '2020.1'),
		('20202', '2020.2'),
	]

	#Dados Pessoais
	cpf = models.CharField(max_length=14, null=False, blank=False, primary_key=True)
	nome = models.CharField(max_length=45, null=False, blank=False)
	sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, null=False, blank=False)
	#dataNascimento = models.DateField(null=True, blank=False)
	#pais = CountryField()
	estado = models.CharField(max_length=2, choices=ESTADO_CHOICES, null=False, blank=False)
	cidade = models.CharField(max_length=30, null=False, blank=False)
	#Contatos
	email = models.EmailField(null=False, blank=False)
	telefone = models.CharField(max_length=13, null= False, blank= False)
	site = models.CharField(max_length=45, null = True)
	#Dados Acadêmicos
	curso = models.CharField(max_length=5, choices=CURSO_CHOICES, blank=False)
	anoPeriodo = models.CharField(max_length=5, choices=PERIODO_CHOICES, null=False, blank=False)
	outraFormacao = models.CharField(max_length=3, null=False, blank= False)
	outraFormacaoInfo = models.CharField(max_length=50, null=True, blank=True)
	ingressoPos = models.CharField(max_length=50, null=False, blank=False)
	#Dados Profissionais
	opcaoMercado = models.CharField(max_length=2, blank=False)
	areaAtuacao = models.CharField(max_length=20, null=False, blank=False)
	formaTrabalho = models.CharField(max_length=10, null=False, blank=False)
	#Relatos
	sugestao = models.TextField(null=False, blank=False)
	depoimento = models.TextField(null=False, blank=False) 

	def __str__(self):
		return self.nome

	
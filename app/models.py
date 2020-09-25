from django.db import models
#from datetime import date

# Create your models here.

class CadastroEgresso (models.Model):
	SEXO_CHOICES = [
		('M', 'Masculino'),
		('F', 'Feminino' ),
	]

	PAIS_CHOICES = [
		('BR', 'Brasil'),
		('FR', 'França'),
		('CA', 'Canadá'),
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

	NATUREZA_CHOICES = [
		('SP', 'Setor Público'),
		('SP', 'Setor Privado'),
		('TS', 'Terceiro Setor - organizações sem fins lucrativos'),
		('PL', 'Profissional Liberal'),
		('FL', 'Freelancer'),
		('BT', 'Bolsista'),
		('MT', 'Militar'),
		('OI', 'Organismo Internacional'),
	]

	#Dados Pessoais
	cpf = models.CharField(max_length=14, null=False, blank=False, primary_key=True)
	nome = models.CharField(max_length=45, null=False, blank=False)
	sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, null=False, blank=False)
	dataNascimento = models.DateField(null=True, blank=False)
	pais = models.CharField(max_length=2, choices=PAIS_CHOICES, null=False, blank=False)
	estado = models.CharField(max_length=2, choices=ESTADO_CHOICES, null=False, blank=False)
	cidade = models.CharField(max_length=30, null=False, blank=False)
	#Contatos
	email = models.EmailField(null=False, blank=False)
	telefone = models.CharField(max_length=13, null= False, blank= False)
	site = models.CharField(max_length=45, null = True)
	#Dados Acadêmicos
	curso = models.CharField(max_length=5, choices=CURSO_CHOICES, blank=False)
	anoPeriodo = models.CharField(max_length=5, choices=PERIODO_CHOICES, null=False, blank=False)
	tituloTrabalho =  models.CharField(max_length= 100)
	#Dados Profissionais
	areaAtuacao = models.CharField(max_length=50, null=True, blank=True)
	naturezaOcupacao = models.CharField(max_length=2, choices=NATUREZA_CHOICES, null=True, blank=True)
	#Relatos
	sugestao = models.TextField(null=False, blank=False)
	depoimento = models.TextField(null=False, blank=False) 

	def __str__(self):
		return self.nome

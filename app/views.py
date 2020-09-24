from django.shortcuts import render,  redirect
#from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
from .forms import CadastroEgressoForm
from .models import *



def home(request):
	egresso = CadastroEgresso.objects.all()
	context = {'egresso':egresso}
	return render(request, 'main.html', context)

def cadastroEgresso(request):
	formEgresso = CadastroEgressoForm()
	if request.method == "POST":
		formEgresso = CadastroEgressoForm(request.POST)
		if formEgresso.is_valid():
			formEgresso.save()
			messages.success(request, 'Formulário enviado com sucesso!')
			return redirect('/')
		else:
			messages.info(request, 'Preenchimento incorreto')
			return redirect('cadastro')
	else:
		context = {'formEgresso': formEgresso}
		return render (request, 'app/form_egresso.html', context)


def dashboard(request):

	context =  {}
	return render(request, 'app/dashboard.html', context)
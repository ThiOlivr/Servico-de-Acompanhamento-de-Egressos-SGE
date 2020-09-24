from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro_egresso/', views.cadastroEgresso, name='cadastro'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
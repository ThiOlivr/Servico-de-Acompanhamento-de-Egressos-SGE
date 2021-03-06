# Generated by Django 3.0.7 on 2020-06-30 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Academico',
            fields=[
                ('curso', models.CharField(choices=[('BCC', 'Bach. Ciência da Computação'), ('PPGCC', 'Pós-Graduação em Ciência da Computação')], max_length=5, primary_key=True, serialize=False)),
                ('anoConclusao', models.DateField()),
                ('tituloTrabalho', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoal',
            fields=[
                ('cpf', models.CharField(max_length=14, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(max_length=13)),
                ('pais', models.CharField(choices=[('BR', 'Brasil'), ('FR', 'França'), ('CA', 'Canadá')], max_length=2)),
                ('estado', models.CharField(choices=[('CE', 'Ceará'), ('RN', 'Rio Grando do Norte'), ('PE', 'Pernambuco'), ('RS', 'Rio Grande do Sul')], max_length=2)),
                ('cidade', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Profissional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('areaAtuacao', models.CharField(blank=True, max_length=50, null=True)),
                ('naturezaOcupacao', models.CharField(blank=True, choices=[('SP', 'Setor Público'), ('SP', 'Setor Privado'), ('TS', 'Terceiro Setor - organizações sem fins lucrativos'), ('PL', 'Profissional Liberal'), ('FL', 'Freelancer'), ('BT', 'Bolsista'), ('MT', 'Militar'), ('OI', 'Organismo Internacional')], max_length=2, null=True)),
                ('anoOcupacaoInicio', models.DateField()),
            ],
        ),
    ]

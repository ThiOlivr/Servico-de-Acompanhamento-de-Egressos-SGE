# Generated by Django 3.0.7 on 2020-09-30 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_remove_cadastroegresso_titulotrabalho'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastroegresso',
            name='areaAtuacao',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='cadastroegresso',
            name='formaTrabalho',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='cadastroegresso',
            name='outraFormacaoInfo',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
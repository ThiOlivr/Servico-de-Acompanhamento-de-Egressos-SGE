# Generated by Django 3.0.7 on 2020-09-25 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_cadastroegresso_opcaomercado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastroegresso',
            name='areaAtuacao',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
# Generated by Django 3.0.7 on 2020-09-30 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20200930_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastroegresso',
            name='outraFormacaoInfo',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]

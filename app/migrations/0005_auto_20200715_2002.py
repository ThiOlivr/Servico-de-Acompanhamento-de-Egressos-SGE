# Generated by Django 3.0.7 on 2020-07-15 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200715_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastroegresso',
            name='depoimento',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cadastroegresso',
            name='sugestao',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
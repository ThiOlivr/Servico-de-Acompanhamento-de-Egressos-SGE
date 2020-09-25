# Generated by Django 3.0.7 on 2020-09-25 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20200925_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastroegresso',
            name='anoPeriodo',
            field=models.CharField(choices=[('20201', '2020.1'), ('20202', '2020.2')], default=2020.1, max_length=5),
            preserve_default=False,
        ),
    ]
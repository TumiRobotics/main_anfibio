# Generated by Django 4.1.2 on 2022-11-28 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infoAnfibio', '0003_usuariosanfibio_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='botesAnfibio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigoBote', models.CharField(default='', max_length=512)),
                ('urlBote', models.CharField(default='', max_length=512)),
            ],
        ),
    ]
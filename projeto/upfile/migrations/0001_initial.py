# Generated by Django 4.1.2 on 2022-10-14 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arquivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('extensao', models.CharField(max_length=5)),
                ('arquivo', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('sobrenome', models.CharField(blank=True, max_length=50)),
                ('sexo', models.CharField(blank=True, max_length=1)),
                ('email', models.EmailField(max_length=254)),
                ('cidade', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=2)),
                ('descricao', models.TextField(max_length=400)),
            ],
        ),
    ]

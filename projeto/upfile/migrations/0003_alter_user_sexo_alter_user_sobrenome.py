# Generated by Django 4.1.2 on 2022-10-15 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upfile', '0002_alter_arquivo_arquivo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='sexo',
            field=models.CharField(max_length=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='sobrenome',
            field=models.CharField(max_length=50),
        ),
    ]

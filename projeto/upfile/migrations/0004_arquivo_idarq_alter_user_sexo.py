# Generated by Django 4.1.2 on 2022-10-15 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upfile', '0003_alter_user_sexo_alter_user_sobrenome'),
    ]

    operations = [
        migrations.AddField(
            model_name='arquivo',
            name='idarq',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='sexo',
            field=models.CharField(blank=True, max_length=1),
        ),
    ]

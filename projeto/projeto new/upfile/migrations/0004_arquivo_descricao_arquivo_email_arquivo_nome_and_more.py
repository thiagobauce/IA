# Generated by Django 4.1 on 2022-10-05 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("upfile", "0003_alter_arquivo_arquivo"),
    ]

    operations = [
        migrations.AddField(
            model_name="arquivo",
            name="descricao",
            field=models.TextField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name="arquivo",
            name="email",
            field=models.CharField(default="meuprojeto7225@gmail.com", max_length=50),
        ),
        migrations.AddField(
            model_name="arquivo",
            name="nome",
            field=models.CharField(default="NULL", max_length=50),
        ),
        migrations.DeleteModel(name="Pessoa",),
    ]

# Generated by Django 5.1.3 on 2024-11-26 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("FitGym", "0005_alter_ejercicio_imagen_alter_entrenamiento_imagen"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ejercicio",
            name="descripcion",
            field=models.TextField(default="", verbose_name="Descripción"),
        ),
        migrations.AlterField(
            model_name="ejercicio",
            name="nombre",
            field=models.CharField(default="", max_length=100, verbose_name="Nombre"),
        ),
        migrations.AlterField(
            model_name="entrenamiento",
            name="descripcion",
            field=models.TextField(default="", verbose_name="Descripción"),
        ),
        migrations.AlterField(
            model_name="entrenamiento",
            name="titulo",
            field=models.CharField(default="", max_length=100, verbose_name="Titulo"),
        ),
    ]

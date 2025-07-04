# Generated by Django 5.2.3 on 2025-06-24 13:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parroquia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('ubicacion', models.CharField(max_length=300)),
                ('tipo', models.CharField(choices=[('Urbana', 'Urbana'), ('Rural', 'Rural')], max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Barrio_Ciudadela',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('numero_viviendas', models.IntegerField()),
                ('numero_parques', models.IntegerField(choices=[(1, '1 parque'), (2, '2 parques'), (3, '3 parques'), (4, '4 parques'), (5, '5 parques'), (6, '6 parques')])),
                ('numero_edificios', models.IntegerField()),
                ('parroquia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ordenamiento.parroquia', verbose_name='barrios')),
            ],
        ),
    ]

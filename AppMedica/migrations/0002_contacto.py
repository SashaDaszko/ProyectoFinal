# Generated by Django 3.2.9 on 2021-12-16 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppMedica', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('tel', models.IntegerField()),
                ('mensaje', models.CharField(max_length=250)),
            ],
        ),
    ]

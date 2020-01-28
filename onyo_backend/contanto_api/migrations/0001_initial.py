# Generated by Django 3.0.2 on 2020-01-27 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nome')),
                ('email', models.EmailField(max_length=150, verbose_name='E-mail')),
                ('assunto', models.CharField(blank=True, max_length=250, null=True, verbose_name='Assunto')),
                ('message', models.TextField(blank=True, max_length=600, null=True, verbose_name='Messagem')),
                ('date_register', models.DateTimeField(auto_now_add=True, verbose_name='Registrado em')),
            ],
            options={
                'verbose_name': 'Contato',
                'verbose_name_plural': 'Contatos',
            },
        ),
    ]

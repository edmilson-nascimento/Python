# Generated by Django 4.1.4 on 2022-12-14 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=150)),
                ('marca', models.CharField(max_length=1000)),
                ('ano', models.IntegerField()),
            ],
        ),
    ]

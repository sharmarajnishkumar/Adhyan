# Generated by Django 4.0.2 on 2022-02-27 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('mobile', models.CharField(max_length=13)),
                ('gender', models.CharField(max_length=6)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('address', models.TextField(max_length=60)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]

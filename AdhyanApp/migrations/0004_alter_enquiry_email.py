# Generated by Django 4.0.2 on 2022-03-21 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdhyanApp', '0003_enquiry_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
# Generated by Django 4.0.2 on 2022-03-06 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0004_alter_register_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='pic',
            field=models.ImageField(default='logo11.png', upload_to='Profile Pic'),
        ),
    ]
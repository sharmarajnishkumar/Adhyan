# Generated by Django 4.0.2 on 2022-03-06 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0002_register_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='All_Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coname', models.CharField(max_length=50)),
                ('coduration', models.CharField(max_length=30)),
                ('coprice', models.IntegerField()),
                ('codepartment', models.CharField(max_length=30)),
                ('codiscription', models.TextField(max_length=100)),
                ('coyear', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='register',
            name='pic',
            field=models.ImageField(default='logo2.png', upload_to='Profile Pic'),
        ),
    ]

# Generated by Django 4.1.5 on 2023-01-25 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='profile_pic',
        ),
        migrations.AlterField(
            model_name='customer',
            name='Gender',
            field=models.CharField(choices=[('MALE', 'FEMALE')], max_length=50),
        ),
        migrations.AlterField(
            model_name='customer',
            name='images',
            field=models.ImageField(upload_to='media/image/'),
        ),
    ]
# Generated by Django 2.1.2 on 2018-10-31 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to='images/categories/'),
        ),
    ]

# Generated by Django 3.0.2 on 2020-01-19 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='email',
            field=models.CharField(max_length=50),
        ),
    ]

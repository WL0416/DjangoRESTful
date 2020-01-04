# Generated by Django 2.2.6 on 2020-01-04 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('birthday', models.DateField()),
                ('passport', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('address', models.CharField(max_length=150)),
                ('issue_date', models.DateField(auto_now=True)),
                ('start_date', models.DateField()),
                ('courses', models.CharField(max_length=20)),
            ],
        ),
    ]
# Generated by Django 3.0.2 on 2020-01-14 08:21

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
                ('birthday', models.CharField(max_length=10)),
                ('passport', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('address', models.CharField(max_length=150)),
                ('start_date', models.CharField(max_length=10)),
                ('courses', models.CharField(max_length=20)),
                ('campus', models.CharField(default='Melbourne', max_length=15)),
            ],
            options={
                'ordering': ['start_date'],
            },
        ),
    ]

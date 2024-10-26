# Generated by Django 5.1.2 on 2024-10-26 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('Name', models.CharField(max_length=10)),
                ('Accno', models.IntegerField(primary_key='Accno', serialize=False)),
                ('Address', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=254)),
                ('DoB', models.DateField()),
            ],
        ),
    ]

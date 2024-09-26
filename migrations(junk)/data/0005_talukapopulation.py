# Generated by Django 3.2.13 on 2024-09-09 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_add_cities_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='TalukaPopulation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taluka_name', models.CharField(max_length=100, unique=True)),
                ('total_population', models.IntegerField()),
            ],
        ),
    ]

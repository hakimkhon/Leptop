# Generated by Django 4.0.5 on 2022-06-13 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kompyuter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('system', models.CharField(max_length=100)),
                ('cost', models.CharField(max_length=50)),
            ],
        ),
    ]

# Generated by Django 4.0.1 on 2022-01-30 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cout_id', models.IntegerField(unique=True)),
                ('cout_name_ru', models.CharField(max_length=100)),
                ('cout_name_tj', models.CharField(max_length=100)),
                ('cout_name_en', models.CharField(max_length=100)),
                ('cout_avail', models.BooleanField(default=True)),
            ],
        ),
    ]

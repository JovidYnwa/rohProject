# Generated by Django 4.0.1 on 2022-01-30 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_id', models.IntegerField()),
                ('city_name_ru', models.CharField(max_length=100)),
                ('city_name_en', models.CharField(max_length=100)),
                ('city_name_tj', models.CharField(max_length=100)),
                ('city_avail', models.BooleanField(default=True)),
                ('cout_cout_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trips.countries')),
            ],
        ),
    ]

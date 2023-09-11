# Generated by Django 4.2.2 on 2023-09-11 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=50)),
                ('participants', models.PositiveIntegerField()),
                ('price', models.FloatField()),
                ('key', models.CharField(max_length=255)),
            ],
        ),
    ]

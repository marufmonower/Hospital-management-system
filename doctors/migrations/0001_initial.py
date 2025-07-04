# Generated by Django 5.2 on 2025-04-13 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialization', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('available_days', models.CharField(max_length=100)),
                ('is_available', models.BooleanField(default=True)),
            ],
        ),
    ]

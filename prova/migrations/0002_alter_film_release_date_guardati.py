# Generated by Django 5.0.6 on 2024-07-01 07:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prova', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='release_date',
            field=models.DateField(null=True),
        ),
        migrations.CreateModel(
            name='Guardati',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prova.film')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# Generated by Django 5.0.3 on 2024-03-26 23:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArthurApp', '0005_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ArthurApp.categoria'),
        ),
    ]

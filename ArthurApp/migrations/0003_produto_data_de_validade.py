# Generated by Django 5.0.3 on 2024-03-26 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArthurApp', '0002_produto_peso'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='data_de_validade',
            field=models.DateField(blank=True, null=True),
        ),
    ]
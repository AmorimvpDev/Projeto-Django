# Generated by Django 5.0.3 on 2024-03-26 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArthurApp', '0004_produto_cor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
            ],
        ),
    ]
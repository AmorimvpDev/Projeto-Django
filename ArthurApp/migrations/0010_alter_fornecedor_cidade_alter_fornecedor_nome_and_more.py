# Generated by Django 5.0.3 on 2024-03-27 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArthurApp', '0009_rename_fornecedores_fornecedor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fornecedor',
            name='cidade',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='nome',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='telefone',
            field=models.CharField(blank=True, max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='descricao',
            field=models.TextField(max_length=8000, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Preço'),
        ),
    ]

# Generated by Django 5.0.3 on 2024-03-26 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArthurApp', '0003_produto_data_de_validade'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='cor',
            field=models.CharField(blank=True, choices=[('BRC', 'Branco'), ('PRT', 'Preto'), ('AMA', 'Amarelo'), ('VRD', 'Verde'), ('VML', 'Vermelho'), ('AZL', 'Azul'), ('LGB', 'LGBT')], max_length=3, null=True),
        ),
    ]

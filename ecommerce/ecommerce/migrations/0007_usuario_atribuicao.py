# Generated by Django 4.1.3 on 2022-11-01 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0006_compra_itemcompra'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='atribuicao',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.1.3 on 2022-11-02 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0014_alter_itemcompra_subtotal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='precoTotal',
            field=models.FloatField(null=True),
        ),
    ]
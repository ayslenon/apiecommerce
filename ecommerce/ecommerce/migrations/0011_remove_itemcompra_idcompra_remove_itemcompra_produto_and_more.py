# Generated by Django 4.1.3 on 2022-11-02 02:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0010_remove_itemcompra_precounitario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemcompra',
            name='idCompra',
        ),
        migrations.RemoveField(
            model_name='itemcompra',
            name='produto',
        ),
        migrations.DeleteModel(
            name='Compra',
        ),
        migrations.DeleteModel(
            name='ItemCompra',
        ),
    ]

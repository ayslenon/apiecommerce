# Generated by Django 4.1.3 on 2022-11-01 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0003_delete_anotherdrink'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeCategoria', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=150)),
                ('precoTotal', models.FloatField()),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('descricaoCompra', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='ItemCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('precoUnitario', models.FloatField()),
                ('idCompra', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ecommerce.compra')),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeProduto', models.CharField(max_length=50)),
                ('descricaoProduto', models.CharField(max_length=250)),
                ('precoProduto', models.FloatField()),
                ('imagemProduto', models.CharField(max_length=150)),
                ('categoriaProduto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ecommerce.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeUsuario', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=150)),
                ('jwt', models.CharField(max_length=150)),
            ],
        ),
        migrations.DeleteModel(
            name='Drink',
        ),
        migrations.AddField(
            model_name='itemcompra',
            name='produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ecommerce.produto'),
        ),
    ]

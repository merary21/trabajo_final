# Generated by Django 4.1.3 on 2022-11-06 22:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tblCiente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=200)),
                ('direccion', models.CharField(max_length=200)),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='tblpedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.CharField(max_length=200)),
                ('precio', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='tblproducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('codigo', models.CharField(max_length=200)),
                ('precio', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='tblTipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='tblTarjeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Num_tarjeta', models.CharField(max_length=200)),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_tienda.tbltipo')),
            ],
        ),
        migrations.CreateModel(
            name='tblpago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Num_tarjeta', models.CharField(max_length=200)),
                ('Fecha', models.DateTimeField()),
                ('Nombre_Cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_tienda.tblciente')),
            ],
        ),
    ]
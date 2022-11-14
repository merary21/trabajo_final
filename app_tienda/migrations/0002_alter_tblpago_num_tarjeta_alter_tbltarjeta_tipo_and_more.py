# Generated by Django 4.1.3 on 2022-11-06 23:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_tienda', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tblpago',
            name='Num_tarjeta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_tienda.tbltarjeta'),
        ),
        migrations.AlterField(
            model_name='tbltarjeta',
            name='tipo',
            field=models.CharField(max_length=200),
        ),
        migrations.DeleteModel(
            name='tblTipo',
        ),
    ]
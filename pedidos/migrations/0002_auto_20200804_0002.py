# Generated by Django 3.0.8 on 2020-08-04 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza_ingrediente',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

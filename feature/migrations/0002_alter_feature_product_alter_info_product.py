# Generated by Django 5.0.6 on 2024-07-06 07:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feature', '0001_initial'),
        ('product', '0002_remove_property_product_delete_feature_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feature', to='product.product'),
        ),
        migrations.AlterField(
            model_name='info',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='info', to='product.product'),
        ),
    ]
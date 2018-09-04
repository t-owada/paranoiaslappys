# Generated by Django 2.1.1 on 2018-09-04 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdata',
            name='Price',
            field=models.CharField(default=(3, 0), max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productdata',
            name='Size',
            field=models.CharField(default='S/M/L', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productimage',
            name='ProductData',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ProductImage', to='products.ProductData'),
        ),
    ]

# Generated by Django 4.2.6 on 2023-11-06 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_image1_alter_product_image2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='specs',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
# Generated by Django 3.1.3 on 2020-12-17 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='prod_category',
            field=models.CharField(default='Product Category', max_length=30),
        ),
        migrations.AlterField(
            model_name='product',
            name='prod_desc',
            field=models.CharField(default='Product Description', max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='prod_name',
            field=models.CharField(default='Product Name', max_length=30),
        ),
        migrations.AlterField(
            model_name='product',
            name='prod_subcategory',
            field=models.CharField(default='Product Subcategory', max_length=30),
        ),
    ]

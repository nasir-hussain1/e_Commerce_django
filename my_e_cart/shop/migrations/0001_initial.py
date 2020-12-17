# Generated by Django 3.1.3 on 2020-12-17 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_name', models.CharField(default='No Name', max_length=30)),
                ('prod_desc', models.CharField(default='No Description', max_length=200)),
                ('prod_category', models.CharField(default='Category', max_length=30)),
                ('prod_subcategory', models.CharField(default='Subcategory', max_length=30)),
                ('prod_price', models.IntegerField(default=0)),
                ('prod_pub_date', models.DateField()),
                ('prod_image', models.ImageField(default='', upload_to='shop/images')),
            ],
        ),
    ]

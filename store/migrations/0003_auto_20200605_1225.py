# Generated by Django 2.2.4 on 2020-06-05 04:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='quantitiy',
            new_name='quantity',
        ),
    ]

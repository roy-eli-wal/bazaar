# Generated by Django 5.1.1 on 2024-11-14 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_item_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='category',
            new_name='listing_category',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='created_at',
            new_name='listing_created_at',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='created_by',
            new_name='listing_created_by',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='descrition',
            new_name='listing_description',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='image',
            new_name='listing_image',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='is_sold',
            new_name='listing_is_sold',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='name',
            new_name='listing_name',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='price',
            new_name='listing_price',
        ),
    ]

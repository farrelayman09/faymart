# Generated by Django 4.2.5 on 2023-09-26 19:50

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_product_user_alter_product_price'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='Item',
        ),
    ]
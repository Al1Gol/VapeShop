# Generated by Django 4.1.6 on 2023-03-17 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_remove_menu_parents_remove_menu_sub_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='img',
            field=models.ImageField(blank=True, upload_to='products', verbose_name='Изображение'),
        ),
    ]
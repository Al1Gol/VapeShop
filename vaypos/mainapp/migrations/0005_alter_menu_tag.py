# Generated by Django 4.1.6 on 2023-02-16 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_alter_menu_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='tag',
            field=models.CharField(default='123', max_length=20, verbose_name='Тэг'),
        ),
    ]
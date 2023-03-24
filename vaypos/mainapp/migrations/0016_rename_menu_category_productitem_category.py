# Generated by Django 4.1.6 on 2023-03-24 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0015_alter_menu_url_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Menu',
            new_name='Category',
        ),
        migrations.AddField(
            model_name='productitem',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mainapp.category'),
            preserve_default=False,
        ),
    ]
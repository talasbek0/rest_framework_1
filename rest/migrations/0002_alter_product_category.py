# Generated by Django 4.2.7 on 2023-11-21 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='rest.category'),
        ),
    ]

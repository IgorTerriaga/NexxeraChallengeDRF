# Generated by Django 4.0.3 on 2022-03-12 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0013_alter_conta_data_abertura'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conta',
            name='data_abertura',
            field=models.DateField(verbose_name='%d-%m-%Y'),
        ),
    ]
# Generated by Django 4.0.3 on 2022-03-11 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0010_alter_transacao_saldo_final_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transacao',
            name='saldo_final',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transacao',
            name='saldo_inicial',
            field=models.FloatField(blank=True, null=True),
        ),
    ]

# Generated by Django 4.0.3 on 2022-03-11 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0006_remove_transacao_saldo_final_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='transacao',
            name='saldo_final',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transacao',
            name='saldo_inicial',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]

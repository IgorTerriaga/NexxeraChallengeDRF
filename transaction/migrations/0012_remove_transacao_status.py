# Generated by Django 4.0.3 on 2022-03-12 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0011_alter_transacao_saldo_final_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transacao',
            name='status',
        ),
    ]

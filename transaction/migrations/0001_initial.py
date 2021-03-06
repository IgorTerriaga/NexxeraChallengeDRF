# Generated by Django 4.0.3 on 2022-03-11 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titular', models.CharField(max_length=43)),
                ('saldo', models.FloatField(default=0)),
                ('data_abertura', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Transacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discriminacao', models.CharField(max_length=100)),
                ('valor', models.FloatField()),
                ('data', models.DateField()),
                ('status', models.CharField(max_length=12)),
                ('saldo_inicial', models.FloatField()),
                ('saldo_final', models.FloatField()),
                ('tipo', models.CharField(choices=[('C', 'Credito'), ('D', 'Debitar')], max_length=1)),
            ],
        ),
    ]

# Generated by Django 4.0.6 on 2023-07-28 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0002_alter_cadastro_ano_pago_alter_cadastro_celular_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastro',
            name='club',
            field=models.IntegerField(choices=[(1, '1-PATRIM'), (2, '2-CONTRIB')], default='1-PATRIM', verbose_name='Tipo socio'),
        ),
    ]

# Generated by Django 4.0.6 on 2023-07-31 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0005_alter_cadastro_data_nascimento'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastro',
            name='club',
            field=models.IntegerField(choices=[(1, '1-PATRIM'), (2, '2-CONTRIB')], default='1-PATRIM', verbose_name='Tipo socio'),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='data_nascimento',
            field=models.DateField(blank=True, null=True, verbose_name='Data Nascimento'),
        ),
    ]

# Generated by Django 4.0.6 on 2023-07-31 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0003_cadastro_club'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cadastro',
            name='club',
        ),
    ]

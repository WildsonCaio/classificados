# Generated by Django 2.2 on 2021-12-15 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
    ]

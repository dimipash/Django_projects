# Generated by Django 4.2.4 on 2023-09-16 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.2.4 on 2023-08-17 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://img.freepik.com/free-vector/green-restaurant-menu-background_23-2147490040.jpg?w=740&t=st=1692250749~exp=1692251349~hmac=2b7f6638a23793d5969690a5ed403d8b47ab0d45371df6c00cc2a43b50e28b6d', max_length=500),
        ),
    ]

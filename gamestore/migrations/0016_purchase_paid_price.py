# Generated by Django 3.0.2 on 2020-02-02 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamestore', '0015_purchase_purchase_complete'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='paid_price',
            field=models.PositiveSmallIntegerField(default=0, editable=False),
            preserve_default=False,
        ),
    ]
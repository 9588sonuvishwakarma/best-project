# Generated by Django 4.0.4 on 2022-07-29 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_tag_order_product_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='contact',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app1.booking'),
        ),
    ]

# Generated by Django 4.1.7 on 2023-05-06 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0008_alter_popular_options_alter_recommended_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='order_count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]

# Generated by Django 5.0.1 on 2024-01-23 07:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("barshop", "0003_remove_reserve_status_table_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, default="2000-01-01 00:00"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="order",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
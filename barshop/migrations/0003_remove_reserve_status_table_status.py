# Generated by Django 5.0.1 on 2024-01-16 08:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("barshop", "0002_remove_reserve_phone_alter_reserve_status"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="reserve",
            name="status",
        ),
        migrations.AddField(
            model_name="table",
            name="status",
            field=models.CharField(
                choices=[("Wait", "Wait"), ("Process", "Process")],
                default="Wait",
                max_length=32,
            ),
            preserve_default=False,
        ),
    ]

# Generated by Django 5.1.1 on 2024-10-01 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='content',
            field=models.TextField(blank=True, max_length=350, null=True),
        ),
    ]

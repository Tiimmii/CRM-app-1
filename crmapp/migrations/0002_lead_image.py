# Generated by Django 4.0.4 on 2022-07-07 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]

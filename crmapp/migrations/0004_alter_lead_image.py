# Generated by Django 4.0.4 on 2022-07-10 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmapp', '0003_alter_lead_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='image',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
# Generated by Django 4.0.1 on 2022-01-25 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudd', '0002_alter_employee_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='profile',
            field=models.ImageField(default=0, upload_to='pics'),
            preserve_default=False,
        ),
    ]
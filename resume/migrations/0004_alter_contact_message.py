# Generated by Django 3.2.6 on 2021-08-18 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_alter_contact_email_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(max_length=2000, null=True),
        ),
    ]

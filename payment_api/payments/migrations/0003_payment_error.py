# Generated by Django 4.2.1 on 2023-05-25 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_payment_user_delete_customuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='error',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
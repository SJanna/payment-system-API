# Generated by Django 4.2.1 on 2023-05-25 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0003_payment_error'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='bank',
            field=models.CharField(default='EastBank', max_length=30),
            preserve_default=False,
        ),
    ]

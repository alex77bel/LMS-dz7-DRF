# Generated by Django 4.2.3 on 2023-08-01 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0013_alter_payment_payment_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_id',
            field=models.CharField(max_length=100, verbose_name='идентификатор платежа у Stripe'),
        ),
    ]
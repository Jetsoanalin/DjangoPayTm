# Generated by Django 2.1.7 on 2019-03-29 15:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('paytm', '0004_auto_20190329_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='paytm_history',
            name='user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rel_payment_paytm', to=settings.AUTH_USER_MODEL),
        ),
    ]
# Generated by Django 4.2.7 on 2023-11-10 17:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_dispositif'),
    ]

    operations = [
        migrations.AddField(
            model_name='dispositif',
            name='users',
            field=models.ManyToManyField(related_name='dispositifs', to=settings.AUTH_USER_MODEL),
        ),
    ]
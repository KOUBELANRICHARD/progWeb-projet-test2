# Generated by Django 4.2.7 on 2023-11-10 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dispositif',
            fields=[
                ('id_dispositif', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=200)),
                ('type', models.CharField(choices=[('CAPTEUR', 'Capteur'), ('ACTUATEUR', 'Actuateur')], default='CAPTEUR', max_length=200)),
                ('image', models.ImageField(upload_to='images/')),
                ('description', models.TextField()),
                ('localisation', models.CharField(blank=True, max_length=200)),
                ('code', models.CharField(blank=True, max_length=4)),
            ],
        ),
    ]

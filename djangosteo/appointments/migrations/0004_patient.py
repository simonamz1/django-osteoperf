# Generated by Django 2.0.2 on 2018-02-07 21:07

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        ('appointments', '0003_auto_20180207_2039'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')], verbose_name='Phone Number')),
                ('birth_date', models.DateField(verbose_name='Date of Birth')),
                ('address', models.CharField(max_length=255, verbose_name='Postal Address')),
            ],
        ),
    ]

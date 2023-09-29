# Generated by Django 3.1.7 on 2021-03-24 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_plan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('couponname', models.CharField(max_length=100)),
                ('coupondiscount', models.CharField(max_length=1000)),
                ('couponlimits', models.CharField(max_length=500)),
                ('code', models.CharField(max_length=100)),
                ('coupondescription', models.CharField(max_length=1000)),
            ],
        ),
    ]
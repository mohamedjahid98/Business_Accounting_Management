# Generated by Django 3.1.7 on 2021-03-25 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_invoice1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Managecreditnotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creditcustomer', models.CharField(max_length=100)),
                ('creditamount', models.CharField(max_length=100)),
                ('creditdate', models.CharField(max_length=100)),
                ('creditdescription', models.CharField(max_length=100)),
            ],
        ),
    ]
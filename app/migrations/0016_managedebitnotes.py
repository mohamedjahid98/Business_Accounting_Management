# Generated by Django 3.1.7 on 2021-03-25 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_bill'),
    ]

    operations = [
        migrations.CreateModel(
            name='Managedebitnotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('debitbill', models.CharField(max_length=100)),
                ('debitamount', models.CharField(max_length=100)),
                ('debitdate', models.CharField(max_length=100)),
                ('debitdescription', models.CharField(max_length=100)),
            ],
        ),
    ]

# Generated by Django 3.1.7 on 2021-03-23 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_managepayment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registername', models.CharField(max_length=100)),
                ('registeremail', models.EmailField(max_length=254)),
                ('registerpass', models.CharField(max_length=8)),
            ],
        ),
    ]

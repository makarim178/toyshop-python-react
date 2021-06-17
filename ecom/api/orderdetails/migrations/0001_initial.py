# Generated by Django 3.1.2 on 2020-11-06 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orderdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderid', models.CharField(max_length=5)),
                ('productid', models.CharField(max_length=5)),
                ('productname', models.CharField(max_length=255)),
                ('productqty', models.CharField(max_length=10)),
                ('productprice', models.CharField(max_length=10)),
            ],
        ),
    ]

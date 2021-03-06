# Generated by Django 3.0.7 on 2020-07-06 08:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer_name', models.CharField(max_length=250)),
                ('mail', models.CharField(max_length=250, unique=True)),
                ('phone_number', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=250, unique=True)),
                ('Price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Order_date', models.DateTimeField(blank=True, null=True)),
                ('number_of_items', models.IntegerField(unique=True)),
                ('Bill', models.IntegerField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coffee_site.Customer')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coffee_site.Menu')),
            ],
        ),
        migrations.CreateModel(
            name='Records',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coffee_site.Customer')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coffee_site.Order')),
            ],
        ),
    ]

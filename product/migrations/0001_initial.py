# Generated by Django 4.1 on 2022-08-21 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'collection',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'product',
                'managed': True,
            },
        ),
    ]

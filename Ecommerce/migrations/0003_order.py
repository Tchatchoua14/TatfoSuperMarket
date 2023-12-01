# Generated by Django 4.2.6 on 2023-11-12 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce', '0002_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=250)),
                ('company', models.CharField(blank=True, max_length=250, null=True)),
                ('apartment', models.CharField(blank=True, max_length=250, null=True)),
                ('post_code', models.CharField(blank=True, max_length=20, null=True)),
                ('city', models.CharField(max_length=100)),
                ('paid', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]

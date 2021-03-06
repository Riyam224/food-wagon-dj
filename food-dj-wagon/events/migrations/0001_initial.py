# Generated by Django 3.2.7 on 2021-09-30 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Featured_Restaurants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('discount', models.IntegerField(verbose_name='discount')),
                ('delivered_status', models.CharField(choices=[('Fast', 'fast'), ('Medium', 'medium'), ('Slow', 'slow')], max_length=10, verbose_name='delivered status')),
                ('image', models.ImageField(upload_to='featured_restaurants', verbose_name='image')),
                ('logo_img', models.ImageField(upload_to='featured_logo', verbose_name='logo image')),
                ('opening_status', models.CharField(choices=[('Tomorrow', 'Opens_Tomorrow'), ('Now', 'Opens_Now')], max_length=10, verbose_name='opening status')),
            ],
            options={
                'verbose_name': 'Featured_Restaurants',
                'verbose_name_plural': 'Featured_Restaurantss',
            },
        ),
        migrations.CreateModel(
            name='OnSale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('image', models.ImageField(upload_to='onsale', verbose_name='image')),
                ('discount', models.IntegerField(verbose_name='discount')),
                ('remaining_days', models.IntegerField(verbose_name='remaining days')),
            ],
            options={
                'verbose_name': 'OnSale',
                'verbose_name_plural': 'OnSales',
            },
        ),
        migrations.CreateModel(
            name='Popular_items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('image', models.ImageField(upload_to='popular_items', verbose_name='image')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='price')),
                ('restaurants', models.CharField(choices=[('BA', 'Burger Arena'), ('TS', 'Top Sticks'), ('CW', 'Cake World'), ('FD', 'Fastfood Dine'), ('FM', 'Foody Man')], max_length=2, verbose_name='restaurants')),
            ],
            options={
                'verbose_name': 'Popular_items',
                'verbose_name_plural': 'Popular_itemss',
            },
        ),
    ]

# Generated by Django 5.0.3 on 2024-12-11 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('serving_size', models.CharField(max_length=50)),
                ('calories', models.DecimalField(decimal_places=2, max_digits=5)),
                ('carbohydrate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('cholesterol', models.DecimalField(decimal_places=2, max_digits=5)),
                ('total_fat', models.DecimalField(decimal_places=2, max_digits=5)),
                ('saturated_fat', models.DecimalField(decimal_places=2, max_digits=5)),
                ('fiber', models.DecimalField(decimal_places=2, max_digits=5)),
                ('protein', models.DecimalField(decimal_places=2, max_digits=5)),
                ('sodium', models.DecimalField(decimal_places=2, max_digits=5)),
                ('sugars', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]

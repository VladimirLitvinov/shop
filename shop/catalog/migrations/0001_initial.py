# Generated by Django 5.0.4 on 2024-09-03 11:33

import catalog.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=128)),
                ('active', models.BooleanField(default=False)),
                ('favourite', models.BooleanField(default=False)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='subcategories', to='catalog.category')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='CategoryIcon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('src', models.ImageField(max_length=500, upload_to=catalog.models.category_image_directory_path)),
                ('category', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='image', to='catalog.category')),
            ],
            options={
                'verbose_name': 'Category icon',
                'verbose_name_plural': 'Category icons',
                'ordering': ['pk'],
            },
        ),
    ]

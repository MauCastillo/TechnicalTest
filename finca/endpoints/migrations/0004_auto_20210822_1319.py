# Generated by Django 3.2.6 on 2021-08-22 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endpoints', '0003_auto_20210822_1311'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.SlugField(max_length=128)),
                ('avatar', models.URLField()),
                ('rating', models.PositiveIntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Reviews',
        ),
        migrations.AlterField(
            model_name='city',
            name='zip',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='property',
            name='sqft',
            field=models.PositiveIntegerField(),
        ),
    ]

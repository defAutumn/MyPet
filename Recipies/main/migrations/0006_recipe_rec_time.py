# Generated by Django 4.1.7 on 2023-05-03 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_recipe_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='rec_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

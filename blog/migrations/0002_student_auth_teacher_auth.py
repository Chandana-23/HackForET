# Generated by Django 4.0 on 2022-04-14 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='auth',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teacher',
            name='auth',
            field=models.BooleanField(default=False),
        ),
    ]

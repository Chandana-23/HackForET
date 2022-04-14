# Generated by Django 4.0 on 2022-04-14 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20220414_1715'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('role', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('img', models.ImageField(upload_to='media/')),
            ],
        ),
    ]
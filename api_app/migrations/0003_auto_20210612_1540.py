# Generated by Django 3.2.3 on 2021-06-12 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0002_book_category_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

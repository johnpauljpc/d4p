# Generated by Django 4.2.1 on 2023-07-04 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_reviews_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(null=True, upload_to='covers/'),
        ),
        migrations.AddField(
            model_name='book',
            name='ebook',
            field=models.FileField(null=True, upload_to='ebooks/'),
        ),
    ]

# Generated by Django 2.0 on 2017-12-24 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0006_auto_20171224_0517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='profile_image',
            field=models.ImageField(null=True, upload_to='profiles/'),
        ),
    ]

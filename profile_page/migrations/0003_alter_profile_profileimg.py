# Generated by Django 5.0.1 on 2024-02-11 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_page', '0002_rename_profile_pict_profile_profileimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profileimg',
            field=models.ImageField(default='bg.png', upload_to='profile_img'),
        ),
    ]

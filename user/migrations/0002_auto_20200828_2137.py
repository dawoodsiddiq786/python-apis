# Generated by Django 2.2.4 on 2020-08-28 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorie',
            name='image',
            field=models.URLField(blank=True, default='http://192.168.1.5:8001/media/image_picker_E34557B2-4E0D-4E94-89D3-8F7D529EB41F-8866-000059F15CE19779.png'),
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.URLField(blank=True, default='http://192.168.1.5:8001/media/image_picker_E34557B2-4E0D-4E94-89D3-8F7D529EB41F-8866-000059F15CE19779.png'),
        ),
    ]
# Generated by Django 3.1.7 on 2021-03-18 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=10),
        ),
    ]

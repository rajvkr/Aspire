# Generated by Django 2.0.1 on 2018-03-21 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_auto_20180321_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.Album'),
        ),
    ]
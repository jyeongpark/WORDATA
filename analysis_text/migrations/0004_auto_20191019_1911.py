# Generated by Django 2.2.6 on 2019-10-19 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis_text', '0003_auto_20191018_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataframe',
            name='numbering',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userinput',
            name='word_except',
            field=models.IntegerField(default=False),
        ),
    ]

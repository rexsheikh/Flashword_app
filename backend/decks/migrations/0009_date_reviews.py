# Generated by Django 4.0.4 on 2022-05-11 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decks', '0008_alter_date_date_alter_word_date_started'),
    ]

    operations = [
        migrations.AddField(
            model_name='date',
            name='reviews',
            field=models.IntegerField(default=0),
        ),
    ]
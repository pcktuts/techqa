# Generated by Django 3.2.4 on 2021-06-26 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('techqa', '0002_auto_20210626_1446'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='question_author',
            new_name='answer_author',
        ),
    ]

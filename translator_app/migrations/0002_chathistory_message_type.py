# Generated by Django 4.2.3 on 2023-07-12 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translator_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chathistory',
            name='message_type',
            field=models.CharField(choices=[('QUESTION', 'Question'), ('ANSWER', 'Answer'), ('ERROR', 'Error')], default='ANSWER', max_length=10),
        ),
    ]
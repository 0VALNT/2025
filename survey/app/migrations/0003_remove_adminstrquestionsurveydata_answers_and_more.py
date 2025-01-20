# Generated by Django 5.1.4 on 2025-01-20 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_adminintquestionsurveydata_answers_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adminstrquestionsurveydata',
            name='answers',
        ),
        migrations.AddField(
            model_name='adminstrquestionsurveydata',
            name='amount',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='adminstrquestionsurveydata',
            name='count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
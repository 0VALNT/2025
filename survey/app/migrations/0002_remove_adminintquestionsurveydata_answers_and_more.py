# Generated by Django 5.1.4 on 2025-01-20 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adminintquestionsurveydata',
            name='answers',
        ),
        migrations.AlterField(
            model_name='adminintquestionsurveydata',
            name='amount',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='adminintquestionsurveydata',
            name='count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
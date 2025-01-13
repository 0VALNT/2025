# Generated by Django 5.1.4 on 2025-01-13 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
        migrations.AddField(
            model_name='question',
            name='answer',
            field=models.CharField(choices=[], default=1, max_length=256),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='type',
            field=models.CharField(choices=[('int', 'int'), ('string', 'string'), ('choices', 'choices'), ('multiple_choice', 'multiple_choice')], max_length=32),
        ),
    ]
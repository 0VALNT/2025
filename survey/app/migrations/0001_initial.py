# Generated by Django 5.1.4 on 2025-01-20 07:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminSurveyData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_of_pass', models.PositiveIntegerField(default=0)),
                ('count_of_question', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='SomeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='CountOfAnswers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count_of_answer', models.PositiveIntegerField(default=0)),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.answer')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('type', models.CharField(choices=[('int', 'int'), ('string', 'string'), ('choices', 'choices'), ('multiple_choice', 'multiple_choice')], max_length=32)),
                ('necessarily', models.BooleanField(default=True)),
                ('answers', models.ManyToManyField(default='-', to='app.answer')),
            ],
        ),
        migrations.CreateModel(
            name='AdminChoseQuestionSurveyData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(default=0)),
                ('admin_survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.adminsurveydata')),
                ('help_model', models.ManyToManyField(to='app.countofanswers')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.question')),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('one_attempt', models.BooleanField(default=True)),
                ('category', models.ManyToManyField(to='app.category')),
                ('past_users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('questions', models.ManyToManyField(to='app.question')),
            ],
        ),
        migrations.AddField(
            model_name='adminsurveydata',
            name='survey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.survey'),
        ),
        migrations.CreateModel(
            name='UserAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=256)),
                ('type', models.CharField(max_length=32)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.question')),
            ],
        ),
        migrations.CreateModel(
            name='AdminStrQuestionSurveyData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.adminsurveydata')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.question')),
                ('answers', models.ManyToManyField(to='app.useranswer')),
            ],
        ),
        migrations.CreateModel(
            name='AdminIntQuestionSurveyData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('count', models.PositiveIntegerField()),
                ('admin_survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.adminsurveydata')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.question')),
                ('answers', models.ManyToManyField(to='app.useranswer')),
            ],
        ),
        migrations.CreateModel(
            name='UserAnswers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.survey')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='useranswer',
            name='user_answers',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.useranswers'),
        ),
    ]

# Generated by Django 4.1.3 on 2022-12-07 13:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('elearn', '0004_remove_marks_course_marks_exam'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materials',
            name='material',
            field=models.FileField(upload_to='media/'),
        ),
        migrations.CreateModel(
            name='Teachprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=51)),
                ('dob', models.DateField()),
                ('address', models.TextField()),
                ('place', models.CharField(max_length=51)),
                ('city', models.CharField(max_length=51)),
                ('state', models.CharField(max_length=51)),
                ('course', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='elearn.courses')),
                ('owner', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Stuprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=51)),
                ('dOB', models.DateField()),
                ('address', models.TextField()),
                ('place', models.CharField(max_length=51)),
                ('city', models.CharField(max_length=51)),
                ('state', models.CharField(max_length=51)),
                ('owner', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Mycourses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='elearn.courses')),
                ('owner', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

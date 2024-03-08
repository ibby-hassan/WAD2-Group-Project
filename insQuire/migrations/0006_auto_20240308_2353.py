# Generated by Django 2.2.28 on 2024-03-08 23:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insQuire', '0005_auto_20240308_1609'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='questionsInCategory',
        ),
        migrations.AddField(
            model_name='category',
            name='questionCount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='answer',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='insQuire.UserProfile'),
        ),
    ]

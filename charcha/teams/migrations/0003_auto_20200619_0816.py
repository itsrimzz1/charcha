# Generated by Django 3.0.7 on 2020-06-19 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_auto_20200618_0024'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='teammember',
            name='team_member_gchat_u_c65725_idx',
        ),
        migrations.AddIndex(
            model_name='teammember',
            index=models.Index(fields=['gchat_user', 'team'], name='team_member_gchat_u_f93a26_idx'),
        ),
    ]

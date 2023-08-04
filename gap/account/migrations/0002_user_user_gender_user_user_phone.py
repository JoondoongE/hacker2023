# Generated by Django 4.2.3 on 2023-08-03 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_gender',
            field=models.CharField(blank=True, choices=[('M', '남성'), ('F', '여성'), ('O', '기타')], max_length=1, null=True, verbose_name='유저 성별'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_phone',
            field=models.CharField(default='', max_length=128, verbose_name='유저 전화번호'),
        ),
    ]

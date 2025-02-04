# Generated by Django 5.1.5 on 2025-02-04 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WorkSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Tiêu đề')),
                ('start_time', models.DateTimeField(verbose_name='Thời gian bắt đầu')),
                ('end_time', models.DateTimeField(verbose_name='Thời gian kết thúc')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Ngày tạo')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Ngày cập nhật')),
            ],
        ),
    ]

# Generated by Django 4.0.3 on 2022-03-08 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stud_name', models.CharField(max_length=200)),
                ('deptt', models.CharField(max_length=100)),
                ('course', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Time_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(verbose_name='date published')),
                ('stud_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stud_detail.student_detail')),
            ],
        ),
    ]

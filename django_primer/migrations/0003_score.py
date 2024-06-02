# Generated by Django 4.1.1 on 2022-09-07 04:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_primer', '0002_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_primer.student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_primer.subject')),
            ],
        ),
    ]

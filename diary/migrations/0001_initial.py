# Generated by Django 2.2.1 on 2019-05-29 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='제목없음', max_length=20)),
                ('image', models.FileField(upload_to='images/')),
                ('text', models.CharField(max_length=500)),
                ('writer', models.CharField(blank=True, max_length=10)),
                ('date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]

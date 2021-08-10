# Generated by Django 2.0.13 on 2021-06-13 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100, null=True)),
                ('description', models.CharField(max_length=200, null=True)),
                ('added_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

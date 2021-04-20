# Generated by Django 3.1.7 on 2021-03-22 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=15, null=True)),
                ('ModelNo', models.CharField(max_length=15, null=True)),
                ('IMEINo', models.IntegerField()),
                ('DOM', models.DateField()),
            ],
        ),
    ]

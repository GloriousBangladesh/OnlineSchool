# Generated by Django 3.2.7 on 2021-09-28 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InstituteType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institute_type', models.CharField(max_length=50, verbose_name='Institute Type')),
            ],
        ),
    ]
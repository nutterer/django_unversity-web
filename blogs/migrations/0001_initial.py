# Generated by Django 3.2 on 2021-05-10 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('Line_of_work', models.CharField(max_length=255)),
                ('Position', models.CharField(max_length=255)),
                ('Academic_position', models.CharField(max_length=255)),
                ('Director_position', models.CharField(max_length=255)),
                ('Date_of_working_in', models.CharField(max_length=255)),
                ('Packing_date', models.CharField(max_length=255)),
                ('Do_the_job', models.CharField(max_length=255)),
                ('Date_of_birth', models.CharField(max_length=255)),
            ],
        ),
    ]

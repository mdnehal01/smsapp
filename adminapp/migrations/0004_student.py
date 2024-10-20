# Generated by Django 3.2.4 on 2024-09-16 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0003_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rollno', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('fname', models.CharField(max_length=50)),
                ('mname', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('dob', models.CharField(max_length=15)),
                ('contactno', models.CharField(max_length=15)),
                ('emailaddress', models.EmailField(max_length=50)),
                ('address', models.TextField()),
                ('sclass', models.CharField(max_length=30)),
                ('feespaid', models.CharField(max_length=10)),
                ('duefees', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=50)),
                ('pic', models.ImageField(upload_to='')),
                ('created_date', models.DateTimeField()),
            ],
        ),
    ]

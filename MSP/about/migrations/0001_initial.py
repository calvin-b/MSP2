# Generated by Django 3.1 on 2020-08-24 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=40)),
                ('gender', models.CharField(choices=[('P', 'Pria'), ('W', 'Wanita')], max_length=6)),
                ('tanggal_lahir', models.DateTimeField()),
                ('alamat', models.TextField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]

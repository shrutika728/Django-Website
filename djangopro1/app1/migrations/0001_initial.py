# Generated by Django 4.0.4 on 2022-08-08 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Phone', models.IntegerField()),
                ('Email', models.EmailField(max_length=100)),
                ('Message', models.CharField(max_length=500)),
            ],
        ),
    ]
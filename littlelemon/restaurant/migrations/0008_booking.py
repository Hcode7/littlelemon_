# Generated by Django 4.2 on 2023-04-17 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0007_rename_imgage_menu_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=3)),
                ('last_name', models.CharField(max_length=2)),
                ('guest_number', models.IntegerField()),
                ('commit', models.CharField(max_length=50)),
            ],
        ),
    ]

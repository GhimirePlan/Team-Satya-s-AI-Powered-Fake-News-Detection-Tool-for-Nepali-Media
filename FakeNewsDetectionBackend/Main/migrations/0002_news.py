# Generated by Django 3.2.25 on 2024-11-28 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('source', models.CharField(max_length=255)),
                ('isfake', models.BooleanField(default=False)),
            ],
        ),
    ]

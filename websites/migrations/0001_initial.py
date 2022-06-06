# Generated by Django 4.0.5 on 2022-06-06 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WebsiteCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('date_added', models.DateTimeField()),
                ('date_updated', models.DateTimeField()),
                ('count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('meta_description', models.CharField(max_length=50)),
                ('alexa_rank', models.IntegerField()),
                ('date_added', models.DateTimeField()),
                ('date_updated', models.DateTimeField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='websites.websitecategory')),
            ],
        ),
        migrations.CreateModel(
            name='WebPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('URL', models.CharField(max_length=50, unique=True)),
                ('date_added', models.DateTimeField()),
                ('date_updated', models.DateTimeField()),
                ('title', models.CharField(max_length=50)),
                ('meta_description', models.CharField(max_length=50)),
                ('website', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='websites.website')),
            ],
        ),
    ]

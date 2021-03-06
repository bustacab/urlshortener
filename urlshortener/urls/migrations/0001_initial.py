# Generated by Django 4.0 on 2021-12-24 22:33

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('url', models.URLField(blank=True, null=True, verbose_name='URL')),
            ],
            options={
                'verbose_name_plural': 'URL',
                'ordering': ('-created',),
            },
        ),
    ]

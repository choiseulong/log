# Generated by Django 2.1.8 on 2019-07-30 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogA', '0003_auto_20190729_1622'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitor_name', models.CharField(max_length=20)),
                ('visitor_contents', models.TextField(default='')),
            ],
        ),
    ]

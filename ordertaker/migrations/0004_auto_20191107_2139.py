# Generated by Django 2.2.7 on 2019-11-07 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordertaker', '0003_auto_20191107_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='sugar_level',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
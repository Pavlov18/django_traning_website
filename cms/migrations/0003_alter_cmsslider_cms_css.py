# Generated by Django 4.2.3 on 2023-08-03 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_cmsslider_cms_css'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cmsslider',
            name='cms_css',
            field=models.CharField(default='-', max_length=200, null=True, verbose_name='CSS class'),
        ),
    ]

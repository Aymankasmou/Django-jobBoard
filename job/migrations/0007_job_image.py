# Generated by Django 4.2.3 on 2023-09-04 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_category_job_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='image',
            field=models.ImageField(default='', upload_to='jobs/'),
            preserve_default=False,
        ),
    ]
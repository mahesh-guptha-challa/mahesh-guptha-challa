# Generated by Django 5.0.4 on 2024-08-04 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_comments_alter_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='comments',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='image_name',
            field=models.ImageField(upload_to=''),
        ),
    ]
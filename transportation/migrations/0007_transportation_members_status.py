# Generated by Django 5.0.1 on 2024-03-09 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transportation', '0006_alter_transportation_maritime_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='transportation_members',
            name='status',
            field=models.BooleanField(default=1, verbose_name='وضعیت'),
            preserve_default=False,
        ),
    ]
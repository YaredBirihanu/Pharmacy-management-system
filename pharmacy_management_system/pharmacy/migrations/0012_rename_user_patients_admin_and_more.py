# Generated by Django 5.0.2 on 2024-04-29 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0011_remove_patients_admin_patients_user_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patients',
            old_name='user',
            new_name='admin',
        ),
        migrations.AlterField(
            model_name='patients',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]

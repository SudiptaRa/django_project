# Generated by Django 4.1.7 on 2023-03-10 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allocation_engine', '0002_alter_employee_table_empemail_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_table',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

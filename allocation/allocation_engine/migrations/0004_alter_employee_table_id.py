# Generated by Django 4.1.7 on 2023-03-10 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allocation_engine', '0003_alter_employee_table_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_table',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
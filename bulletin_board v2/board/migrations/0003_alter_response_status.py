# Generated by Django 4.2.1 on 2023-10-27 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_response_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='status',
            field=models.CharField(choices=[('A', 'Принят'), ('D', 'Отклонён')], max_length=1, null=True),
        ),
    ]

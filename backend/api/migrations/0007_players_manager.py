# Generated by Django 4.1.5 on 2023-02-25 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_managers_options_alter_players_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='players',
            name='manager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.managers'),
        ),
    ]

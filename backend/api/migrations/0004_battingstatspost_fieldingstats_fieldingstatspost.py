# Generated by Django 4.1.5 on 2023-01-05 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_battingstats'),
    ]

    operations = [
        migrations.CreateModel(
            name='Battingstatspost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yearid', models.TextField(db_column='yearID')),
                ('round', models.TextField(blank=True)),
                ('playerid', models.TextField(blank=True, db_column='playerID')),
                ('teamid', models.TextField(blank=True, db_column='teamID')),
                ('lgid', models.TextField(blank=True, db_column='lgID')),
                ('g', models.TextField(blank=True, db_column='G')),
                ('ab', models.TextField(blank=True, db_column='AB')),
                ('r', models.TextField(blank=True, db_column='R')),
                ('h', models.TextField(blank=True, db_column='H')),
                ('number_2b', models.TextField(blank=True, db_column='2B')),
                ('number_3b', models.TextField(blank=True, db_column='3B')),
                ('hr', models.TextField(blank=True, db_column='HR')),
                ('rbi', models.TextField(blank=True, db_column='RBI')),
                ('sb', models.TextField(blank=True, db_column='SB')),
                ('cs', models.TextField(blank=True, db_column='CS')),
                ('bb', models.TextField(blank=True, db_column='BB')),
                ('so', models.TextField(blank=True, db_column='SO')),
                ('ibb', models.TextField(blank=True, db_column='IBB')),
                ('hbp', models.TextField(blank=True, db_column='HBP')),
                ('sh', models.TextField(blank=True, db_column='SH')),
                ('sf', models.TextField(blank=True, db_column='SF')),
                ('gidp', models.TextField(blank=True, db_column='GIDP')),
            ],
            options={
                'db_table': 'BattingStatsPost',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Fieldingstats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playerid', models.TextField(db_column='playerID')),
                ('yearid', models.TextField(blank=True, db_column='yearID')),
                ('stint', models.TextField(blank=True)),
                ('teamid', models.TextField(blank=True, db_column='teamID')),
                ('lgid', models.TextField(blank=True, db_column='lgID')),
                ('pos', models.TextField(blank=True, db_column='POS')),
                ('g', models.TextField(blank=True, db_column='G')),
                ('gs', models.TextField(blank=True, db_column='GS')),
                ('innouts', models.TextField(blank=True, db_column='InnOuts')),
                ('po', models.TextField(blank=True, db_column='PO')),
                ('a', models.TextField(blank=True, db_column='A')),
                ('e', models.TextField(blank=True, db_column='E')),
                ('dp', models.TextField(blank=True, db_column='DP')),
                ('pb', models.TextField(blank=True, db_column='PB')),
                ('wp', models.TextField(blank=True, db_column='WP')),
                ('sb', models.TextField(blank=True, db_column='SB')),
                ('cs', models.TextField(blank=True, db_column='CS')),
                ('zr', models.TextField(blank=True, db_column='ZR')),
            ],
            options={
                'db_table': 'FieldingStats',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Fieldingstatspost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playerid', models.TextField(db_column='playerID')),
                ('yearid', models.TextField(blank=True, db_column='yearID')),
                ('teamid', models.TextField(blank=True, db_column='teamID')),
                ('lgid', models.TextField(blank=True, db_column='lgID')),
                ('round', models.TextField(blank=True)),
                ('pos', models.TextField(blank=True, db_column='POS')),
                ('g', models.TextField(blank=True, db_column='G')),
                ('gs', models.TextField(blank=True, db_column='GS')),
                ('innouts', models.TextField(blank=True, db_column='InnOuts')),
                ('po', models.TextField(blank=True, db_column='PO')),
                ('a', models.TextField(blank=True, db_column='A')),
                ('e', models.TextField(blank=True, db_column='E')),
                ('dp', models.TextField(blank=True, db_column='DP')),
                ('tp', models.TextField(blank=True, db_column='TP')),
                ('pb', models.TextField(blank=True, db_column='PB')),
                ('sb', models.TextField(blank=True, db_column='SB')),
                ('cs', models.TextField(blank=True, db_column='CS')),
            ],
            options={
                'db_table': 'FieldingStatsPost',
                'managed': False,
            },
        ),
    ]
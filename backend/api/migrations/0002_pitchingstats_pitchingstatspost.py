# Generated by Django 4.1.5 on 2023-01-04 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pitchingstats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playerid', models.TextField(db_column='playerID')),
                ('yearid', models.TextField(blank=True, db_column='yearID')),
                ('stint', models.TextField(blank=True)),
                ('teamid', models.TextField(blank=True, db_column='teamID')),
                ('lgid', models.TextField(blank=True, db_column='lgID')),
                ('w', models.TextField(blank=True, db_column='W')),
                ('l', models.TextField(blank=True, db_column='L')),
                ('g', models.TextField(blank=True, db_column='G')),
                ('gs', models.TextField(blank=True, db_column='GS')),
                ('cg', models.TextField(blank=True, db_column='CG')),
                ('sho', models.TextField(blank=True, db_column='SHO')),
                ('sv', models.TextField(blank=True, db_column='SV')),
                ('ipouts', models.TextField(blank=True, db_column='IPouts')),
                ('h', models.TextField(blank=True, db_column='H')),
                ('er', models.TextField(blank=True, db_column='ER')),
                ('hr', models.TextField(blank=True, db_column='HR')),
                ('bb', models.TextField(blank=True, db_column='BB')),
                ('so', models.TextField(blank=True, db_column='SO')),
                ('baopp', models.TextField(blank=True, db_column='BAOpp')),
                ('era', models.TextField(blank=True, db_column='ERA')),
                ('ibb', models.TextField(blank=True, db_column='IBB')),
                ('wp', models.TextField(blank=True, db_column='WP')),
                ('hbp', models.TextField(blank=True, db_column='HBP')),
                ('bk', models.TextField(blank=True, db_column='BK')),
                ('bfp', models.TextField(blank=True, db_column='BFP')),
                ('gf', models.TextField(blank=True, db_column='GF')),
                ('r', models.TextField(blank=True, db_column='R')),
                ('sh', models.TextField(blank=True, db_column='SH')),
                ('sf', models.TextField(blank=True, db_column='SF')),
                ('gidp', models.TextField(blank=True, db_column='GIDP')),
            ],
            options={
                'db_table': 'PitchingStats',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pitchingstatspost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playerid', models.TextField(db_column='playerID')),
                ('yearid', models.TextField(blank=True, db_column='yearID')),
                ('round', models.TextField(blank=True)),
                ('teamid', models.TextField(blank=True, db_column='teamID')),
                ('lgid', models.TextField(blank=True, db_column='lgID')),
                ('w', models.TextField(blank=True, db_column='W')),
                ('l', models.TextField(blank=True, db_column='L')),
                ('g', models.TextField(blank=True, db_column='G')),
                ('gs', models.TextField(blank=True, db_column='GS')),
                ('cg', models.TextField(blank=True, db_column='CG')),
                ('sho', models.TextField(blank=True, db_column='SHO')),
                ('sv', models.TextField(blank=True, db_column='SV')),
                ('ipouts', models.TextField(blank=True, db_column='IPouts')),
                ('h', models.TextField(blank=True, db_column='H')),
                ('er', models.TextField(blank=True, db_column='ER')),
                ('hr', models.TextField(blank=True, db_column='HR')),
                ('bb', models.TextField(blank=True, db_column='BB')),
                ('so', models.TextField(blank=True, db_column='SO')),
                ('baopp', models.TextField(blank=True, db_column='BAOpp')),
                ('era', models.TextField(blank=True, db_column='ERA')),
                ('ibb', models.TextField(blank=True, db_column='IBB')),
                ('wp', models.TextField(blank=True, db_column='WP')),
                ('hbp', models.TextField(blank=True, db_column='HBP')),
                ('bk', models.TextField(blank=True, db_column='BK')),
                ('bfp', models.TextField(blank=True, db_column='BFP')),
                ('gf', models.TextField(blank=True, db_column='GF')),
                ('r', models.TextField(blank=True, db_column='R')),
                ('sh', models.TextField(blank=True, db_column='SH')),
                ('sf', models.TextField(blank=True, db_column='SF')),
                ('gidp', models.TextField(blank=True, db_column='GIDP')),
            ],
            options={
                'db_table': 'PitchingStatsPost',
                'managed': False,
            },
        ),
    ]

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Managers(models.Model):
    playerid = models.TextField(db_column='playerID')  # Field name made lowercase.
    yearid = models.TextField(db_column='yearID', blank=True)  # Field name made lowercase.
    teamid = models.TextField(db_column='teamID', blank=True)  # Field name made lowercase.
    lgid = models.TextField(db_column='lgID', blank=True)  # Field name made lowercase.
    inseason = models.TextField(blank=True)
    g = models.TextField(db_column='G', blank=True)  # Field name made lowercase.
    w = models.TextField(db_column='W', blank=True)  # Field name made lowercase.
    l = models.TextField(db_column='L', blank=True)  # Field name made lowercase.
    rank = models.TextField(blank=True)
    plyrmgr = models.TextField(db_column='plyrMgr', blank=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'Managers'

class Teams(models.Model):
    yearid = models.TextField(db_column='yearID', blank=True)  # Field name made lowercase.
    lgid = models.TextField(db_column='lgID', blank=True)  # Field name made lowercase.
    teamid = models.TextField(db_column='teamID', blank=True)  # Field name made lowercase.
    franchid = models.TextField(db_column='franchID', blank=True)  # Field name made lowercase.
    divid = models.TextField(db_column='divID', blank=True)  # Field name made lowercase.
    rank = models.TextField(db_column='Rank', blank=True)  # Field name made lowercase.
    g = models.TextField(db_column='G', blank=True)  # Field name made lowercase.
    ghome = models.TextField(db_column='Ghome', blank=True)  # Field name made lowercase.
    w = models.TextField(db_column='W', blank=True)  # Field name made lowercase.
    l = models.TextField(db_column='L', blank=True)  # Fieldame made lowercase.
    divwin = models.TextField(db_column='DivWin', blank=True)  # Field name made lowercase.
    wcwin = models.TextField(db_column='WCWin', blank=True)  # Field name made lowercase.
    lgwin = models.TextField(db_column='LgWin', blank=True)  # Field name made lowercase.
    wswin = models.TextField(db_column='WSWin', blank=True)  # Field name made lowercase.
    r = models.TextField(db_column='R', blank=True)  # Field name made lowercase.
    ab = models.TextField(db_column='AB', blank=True)  # Field name made lowercase.
    h = models.TextField(db_column='H', blank=True)  # Field name made lowercase.
    number_2b = models.TextField(db_column='2B', blank=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3b = models.TextField(db_column='3B', blank=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    hr = models.TextField(db_column='HR', blank=True)  # Field name made lowercase.
    bb = models.TextField(db_column='BB', blank=True)  # Field name made lowercase.
    so = models.TextField(db_column='SO', blank=True)  # Field name made lowercase.
    sb = models.TextField(db_column='SB', blank=True)  # Field name made lowercase.
    cs = models.TextField(db_column='CS', blank=True)  # Field name made lowercase.
    hbp = models.TextField(db_column='HBP', blank=True)  # Field name made lowercase.
    sf = models.TextField(db_column='SF', blank=True)  # Field name made lowercase.
    ra = models.TextField(db_column='RA', blank=True)  # Field name made lowercase.
    er = models.TextField(db_column='ER', blank=True)  # Field name made lowercase.
    era = models.TextField(db_column='ERA', blank=True)  # Field name made lowercase.
    cg = models.TextField(db_column='CG', blank=True)  # Field name made lowercase.
    sho = models.TextField(db_column='SHO', blank=True)  # Field name made lowercase.
    sv = models.TextField(db_column='SV', blank=True)  # Field name made lowercase.
    ipouts = models.TextField(db_column='IPouts', blank=True)  # Field name made lowercase.
    ha = models.TextField(db_column='HA', blank=True)  # Field name made lowercase.
    hra = models.TextField(db_column='HRA', blank=True)  # Field name made lowercase.
    bba = models.TextField(db_column='BBA', blank=True)  # Field name made lowercase.
    soa = models.TextField(db_column='SOA', blank=True)  # Field name made lowercase.
    e = models.TextField(db_column='E', blank=True)  # Field name made lowercase.
    dp = models.TextField(db_column='DP', blank=True)  # Field name made lowercase.
    fp = models.TextField(db_column='FP', blank=True)  # Field name made lowercase.
    name = models.TextField(blank=True)
    park = models.TextField(blank=True)
    attendance_field = models.TextField(db_column='attendance', blank=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    bpf = models.TextField(db_column='BPF', blank=True)  # Field name made lowercase.
    ppf = models.TextField(db_column='PPF', blank=True)  # Field name made lowercase.
    teamidbr = models.TextField(db_column='teamIDBR', blank=True)  # Field name made lowercase.
    teamidlahman45 = models.TextField(db_column='teamIDlahman45', blank=True)  # Field name made lowercase.
    teamidretro = models.TextField(db_column='teamIDretro', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Teams'

class Players(models.Model):
    playerid = models.TextField(db_column='playerID')  # Field name made lowercase.
    birthyear = models.TextField(db_column='birthYear', blank=True)  # Field name made lowercase.
    birthmonth = models.TextField(db_column='birthMonth', blank=True)  # Field name made lowercase.
    birthday = models.TextField(db_column='birthDay', blank=True)  # Field name made lowercase.
    birthcountry = models.TextField(db_column='birthCountry', blank=True)  # Field name made lowercase.
    birthstate = models.TextField(db_column='birthState', blank=True)  # Field name made lowercase.
    birthcity = models.TextField(db_column='birthCity', blank=True)  # Field name made lowercase.
    deathyear = models.TextField(db_column='deathYear', blank=True)  # Field name made lowercase.
    deathmonth = models.TextField(db_column='deathMonth', blank=True)  # Field name made lowercase.
    deathday = models.TextField(db_column='deathDay', blank=True)  # Field name made lowercase.
    deathcountry = models.TextField(db_column='deathCountry', blank=True)  # Field name made lowercase.
    deathstate = models.TextField(db_column='deathState', blank=True)  # Field name made lowercase.
    deathcity = models.TextField(db_column='deathCity', blank=True)  # Field name made lowercase.
    namefirst = models.TextField(db_column='nameFirst', blank=True)  # Field name made lowercase.
    namelast = models.TextField(db_column='nameLast', blank=True)  # Field name made lowercase.
    namegiven = models.TextField(db_column='nameGiven', blank=True)  # Field name made lowercase.
    weight = models.TextField(blank=True)
    height = models.TextField(blank=True)
    bats = models.TextField(blank=True)
    throws = models.TextField(blank=True)
    debut = models.TextField(blank=True)
    finalgame = models.TextField(db_column='finalGame', blank=True)  # Field name made lowercase.
    retroid = models.TextField(db_column='retroID', blank=True)  # Field name made lowercase.
    bbrefid = models.TextField(db_column='bbrefID', blank=True)  # Field name made lowercase.
    manager = models.ForeignKey(Managers, on_delete=models.CASCADE, null=True)
    
    class Meta:
        # managed = False
        db_table = 'Players'


class Pitchingstats(models.Model):
    playerid = models.TextField(db_column='playerID')  # Field name made lowercase.
    yearid = models.TextField(db_column='yearID', blank=True)  # Field name made lowercase.
    stint = models.TextField(blank=True)
    teamid = models.TextField(db_column='teamID', blank=True)  # Field name made lowercase.
    lgid = models.TextField(db_column='lgID', blank=True)  # Field name made lowercase.
    w = models.TextField(db_column='W', blank=True)  # Field name made lowercase.
    l = models.TextField(db_column='L', blank=True)  # Field name made lowercase.
    g = models.TextField(db_column='G', blank=True)  # Field name made lowercase.
    gs = models.TextField(db_column='GS', blank=True)  # Field name made lowercase.
    cg = models.TextField(db_column='CG', blank=True)  # Field name made lowercase.
    sho = models.TextField(db_column='SHO', blank=True)  # Field name made lowercase.
    sv = models.TextField(db_column='SV', blank=True)  # Field name made lowercase.
    ipouts = models.TextField(db_column='IPouts', blank=True)  # Field name made lowercase.
    h = models.TextField(db_column='H', blank=True)  # Field name made lowercase.
    er = models.TextField(db_column='ER', blank=True)  # Field name made lowercase.
    hr = models.TextField(db_column='HR', blank=True)  # Field name made lowercase.
    bb = models.TextField(db_column='BB', blank=True)  # Field name made lowercase.
    so = models.TextField(db_column='SO', blank=True)  # Field name made lowercase.
    baopp = models.TextField(db_column='BAOpp', blank=True)  # Field name made lowercase.
    era = models.TextField(db_column='ERA', blank=True)  # Field name made lowercase.
    ibb = models.TextField(db_column='IBB', blank=True)  # Field name made lowercase.
    wp = models.TextField(db_column='WP', blank=True)  # Field name made lowercase.
    hbp = models.TextField(db_column='HBP', blank=True)  # Field name made lowercase.
    bk = models.TextField(db_column='BK', blank=True)  # Field name made lowercase.
    bfp = models.TextField(db_column='BFP', blank=True)  # Field name made lowercase.
    gf = models.TextField(db_column='GF', blank=True)  # Field name made lowercase.
    r = models.TextField(db_column='R', blank=True)  # Field name made lowercase.
    sh = models.TextField(db_column='SH', blank=True)  # Field name made lowercase.
    sf = models.TextField(db_column='SF', blank=True)  # Field name made lowercase.
    gidp = models.TextField(db_column='GIDP', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PitchingStats'



class Pitchingstatspost(models.Model):
    playerid = models.TextField(db_column='playerID')  # Field name made lowercase.
    yearid = models.TextField(db_column='yearID', blank=True)  # Field name made lowercase.
    round = models.TextField(blank=True)
    teamid = models.TextField(db_column='teamID', blank=True)  # Field name made lowercase.
    lgid = models.TextField(db_column='lgID', blank=True)  # Field name made lowercase.
    w = models.TextField(db_column='W', blank=True)  # Field name made lowercase.
    l = models.TextField(db_column='L', blank=True)  # Field name made lowercase.
    g = models.TextField(db_column='G', blank=True)  # Field name made lowercase.
    gs = models.TextField(db_column='GS', blank=True)  # Field name made lowercase.
    cg = models.TextField(db_column='CG', blank=True)  # Field name made lowercase.
    sho = models.TextField(db_column='SHO', blank=True)  # Field name made lowercase.
    sv = models.TextField(db_column='SV', blank=True)  # Field name made lowercase.
    ipouts = models.TextField(db_column='IPouts', blank=True)  # Field name made lowercase.
    h = models.TextField(db_column='H', blank=True)  # Field name made lowercase.
    er = models.TextField(db_column='ER', blank=True)  # Field name made lowercase.
    hr = models.TextField(db_column='HR', blank=True)  # Field name made lowercase.
    bb = models.TextField(db_column='BB', blank=True)  # Field name made lowercase.
    so = models.TextField(db_column='SO', blank=True)  # Field name made lowercase.
    baopp = models.TextField(db_column='BAOpp', blank=True)  # Field name made lowercase.
    era = models.TextField(db_column='ERA', blank=True)  # Field name made lowercase.
    ibb = models.TextField(db_column='IBB', blank=True)  # Field name made lowercase.
    wp = models.TextField(db_column='WP', blank=True)  # Field name made lowercase.
    hbp = models.TextField(db_column='HBP', blank=True)  # Field name made lowercase.
    bk = models.TextField(db_column='BK', blank=True)  # Field name made lowercase.
    bfp = models.TextField(db_column='BFP', blank=True)  # Field name made lowercase.
    gf = models.TextField(db_column='GF', blank=True)  # Field name made lowercase.
    r = models.TextField(db_column='R', blank=True)  # Field name made lowercase.
    sh = models.TextField(db_column='SH', blank=True)  # Field name made lowercase.
    sf = models.TextField(db_column='SF', blank=True)  # Field name made lowercase.
    gidp = models.TextField(db_column='GIDP', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PitchingStatsPost'

class Battingstats(models.Model):
    playerid = models.TextField(db_column='playerID')  # Field name made lowercase.
    yearid = models.TextField(db_column='yearID', blank=True)  # Field name made lowercase.
    stint = models.TextField(blank=True)
    teamid = models.TextField(db_column='teamID', blank=True)  # Field name made lowercase.
    lgid = models.TextField(db_column='lgID', blank=True)  # Field name made lowercase.
    g = models.TextField(db_column='G', blank=True)  # Field name made lowercase.
    ab = models.TextField(db_column='AB', blank=True)  # Field name made lowercase.
    r = models.TextField(db_column='R', blank=True)  # Field name made lowercase.
    h = models.TextField(db_column='H', blank=True)  # Field name made lowercase.
    number_2b = models.TextField(db_column='2B', blank=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3b = models.TextField(db_column='3B', blank=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    hr = models.TextField(db_column='HR', blank=True)  # Field name made lowercase.
    rbi = models.TextField(db_column='RBI', blank=True)  # Field name made lowercase.
    sb = models.TextField(db_column='SB', blank=True)  # Field name made lowercase.
    cs = models.TextField(db_column='CS', blank=True)  # Field name made lowercase.
    bb = models.TextField(db_column='BB', blank=True)  # Field name made lowercase.
    so = models.TextField(db_column='SO', blank=True)  # Field name made lowercase.
    ibb = models.TextField(db_column='IBB', blank=True)  # Field name made lowercase.
    hbp = models.TextField(db_column='HBP', blank=True)  # Field name made lowercase.
    sh = models.TextField(db_column='SH', blank=True)  # Field name made lowercase.
    sf = models.TextField(db_column='SF', blank=True)  # Field name made lowercase.
    gidp = models.TextField(db_column='GIDP', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BattingStats'

class Battingstatspost(models.Model):
    yearid = models.TextField(db_column='yearID')  # Field name made lowercase.
    round = models.TextField(blank=True)
    playerid = models.TextField(db_column='playerID', blank=True)  # Field name made lowercase.
    teamid = models.TextField(db_column='teamID', blank=True)  # Field name made lowercase.
    lgid = models.TextField(db_column='lgID', blank=True)  # Field name made lowercase.
    g = models.TextField(db_column='G', blank=True)  # Field name made lowercase.
    ab = models.TextField(db_column='AB', blank=True)  # Field name made lowercase.
    r = models.TextField(db_column='R', blank=True)  # Field name made lowercase.
    h = models.TextField(db_column='H', blank=True)  # Field name made lowercase.
    number_2b = models.TextField(db_column='2B', blank=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3b = models.TextField(db_column='3B', blank=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    hr = models.TextField(db_column='HR', blank=True)  # Field name made lowercase.
    rbi = models.TextField(db_column='RBI', blank=True)  # Field name made lowercase.
    sb = models.TextField(db_column='SB', blank=True)  # Field name made lowercase.
    cs = models.TextField(db_column='CS', blank=True)  # Field name made lowercase.
    bb = models.TextField(db_column='BB', blank=True)  # Field name made lowercase.
    so = models.TextField(db_column='SO', blank=True)  # Field name made lowercase.
    ibb = models.TextField(db_column='IBB', blank=True)  # Field name made lowercase.
    hbp = models.TextField(db_column='HBP', blank=True)  # Field name made lowercase.
    sh = models.TextField(db_column='SH', blank=True)  # Field name made lowercase.
    sf = models.TextField(db_column='SF', blank=True)  # Field name made lowercase.
    gidp = models.TextField(db_column='GIDP', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BattingStatsPost'


class Fieldingstats(models.Model):
    playerid = models.TextField(db_column='playerID')  # Field name made lowercase.
    yearid = models.TextField(db_column='yearID', blank=True)  # Field name made lowercase.
    stint = models.TextField(blank=True)
    teamid = models.TextField(db_column='teamID', blank=True)  # Field name made lowercase.
    lgid = models.TextField(db_column='lgID', blank=True)  # Field name made lowercase.
    pos = models.TextField(db_column='POS', blank=True)  # Field name made lowercase.
    g = models.TextField(db_column='G', blank=True)  # Field name made lowercase.
    gs = models.TextField(db_column='GS', blank=True)  # Field name made lowercase.
    innouts = models.TextField(db_column='InnOuts', blank=True)  # Field name made lowercase.
    po = models.TextField(db_column='PO', blank=True)  # Field name made lowercase.
    a = models.TextField(db_column='A', blank=True)  # Field name made lowercase.
    e = models.TextField(db_column='E', blank=True)  # Field name made lowercase.
    dp = models.TextField(db_column='DP', blank=True)  # Field name made lowercase.
    pb = models.TextField(db_column='PB', blank=True)  # Field name made lowercase.
    wp = models.TextField(db_column='WP', blank=True)  # Field name made lowercase.
    sb = models.TextField(db_column='SB', blank=True)  # Field name made lowercase.
    cs = models.TextField(db_column='CS', blank=True)  # Field name made lowercase.
    zr = models.TextField(db_column='ZR', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FieldingStats'


class Fieldingstatspost(models.Model):
    playerid = models.TextField(db_column='playerID')  # Field name made lowercase.
    yearid = models.TextField(db_column='yearID', blank=True)  # Field name made lowercase.
    teamid = models.TextField(db_column='teamID', blank=True)  # Field name made lowercase.
    lgid = models.TextField(db_column='lgID', blank=True)  # Field name made lowercase.
    round = models.TextField(blank=True)
    pos = models.TextField(db_column='POS', blank=True)  # Field name made lowercase.
    g = models.TextField(db_column='G', blank=True)  # Field name made lowercase.
    gs = models.TextField(db_column='GS', blank=True)  # Field name made lowercase.
    innouts = models.TextField(db_column='InnOuts', blank=True)  # Field name made lowercase.
    po = models.TextField(db_column='PO', blank=True)  # Field name made lowercase.
    a = models.TextField(db_column='A', blank=True)  # Field name made lowercase.
    e = models.TextField(db_column='E', blank=True)  # Field name made lowercase.
    dp = models.TextField(db_column='DP', blank=True)  # Field name made lowercase.
    tp = models.TextField(db_column='TP', blank=True)  # Field name made lowercase.
    pb = models.TextField(db_column='PB', blank=True)  # Field name made lowercase.
    sb = models.TextField(db_column='SB', blank=True)  # Field name made lowercase.
    cs = models.TextField(db_column='CS', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FieldingStatsPost'

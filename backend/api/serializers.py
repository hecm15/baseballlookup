from rest_framework import serializers
from api.models import Teams, Players, Pitchingstats, Pitchingstatspost, Battingstats, Battingstatspost, Fieldingstats, Fieldingstatspost, Managers


class PlayerInfoSerializer(serializers.Serializer):
    name = serializers.CharField()
    age = serializers.CharField()
    weight = serializers.CharField()
    height = serializers.CharField()
    bats = serializers.CharField()
    throws = serializers.CharField()
    position = serializers.CharField()

class PlayerOptionsSerializer(serializers.Serializer):
    name = serializers.CharField()
    playerid = serializers.CharField()
    debut = serializers.CharField()

class BattingStatsTableSerializer(serializers.Serializer):
    year = serializers.CharField()
    team = serializers.CharField()
    games = serializers.CharField()
    atbats = serializers.CharField()
    runs = serializers.CharField()
    rbis = serializers.CharField() 
    hits = serializers.CharField()
    doubles = serializers.CharField()
    triples = serializers.CharField()
    homeruns = serializers.CharField()
    bbpercent = serializers.CharField()
    sopercent = serializers.CharField()
    sb = serializers.CharField()
    cs = serializers.CharField()
    avg = serializers.CharField()

class BattingStatsPostTableSerializer(serializers.Serializer):
    year = serializers.CharField()
    team = serializers.CharField()
    series = serializers.CharField()
    games = serializers.CharField()
    atbats = serializers.CharField()
    runs = serializers.CharField()
    rbis = serializers.CharField()
    hits = serializers.CharField()
    doubles = serializers.CharField()
    triples = serializers.CharField()
    homeruns = serializers.CharField()
    bbpercent = serializers.CharField()
    sopercent = serializers.CharField()
    sb = serializers.CharField()
    cs = serializers.CharField()
    avg = serializers.CharField()

class FieldingStatsTableSerializer(serializers.Serializer):
    year = serializers.CharField()
    team = serializers.CharField()
    position = serializers.CharField()
    games = serializers.CharField()
    gamesstarted = serializers.CharField()
    innouts = serializers.CharField()
    po = serializers.CharField()
    a = serializers.CharField()
    e = serializers.CharField()
    dp = serializers.CharField()
    pb = serializers.CharField()
    wp = serializers.CharField()
    sb = serializers.CharField()
    cs = serializers.CharField()
    zr = serializers.CharField()

class FieldingStatsPostTableSerializer(serializers.Serializer):
    year = serializers.CharField()
    team = serializers.CharField()
    series = serializers.CharField()
    position = serializers.CharField()
    games = serializers.CharField()
    gamesstarted = serializers.CharField()
    innouts = serializers.CharField()
    po = serializers.CharField()
    a = serializers.CharField()
    e = serializers.CharField()
    dp = serializers.CharField()
    tp = serializers.CharField()
    pb = serializers.CharField()
    sb = serializers.CharField()
    cs = serializers.CharField()

class PitchingStatsTableSerializer(serializers.Serializer):
    year = serializers.CharField()
    team = serializers.CharField()
    wins = serializers.CharField()
    losses = serializers.CharField()
    era = serializers.CharField()
    games = serializers.CharField()
    gamesstarted = serializers.CharField()
    cg = serializers.CharField()
    sho = serializers.CharField()
    sv = serializers.CharField()
    ip = serializers.CharField()
    tbf = serializers.CharField()
    h = serializers.CharField()
    r = serializers.CharField()
    er = serializers.CharField()
    hr = serializers.CharField()
    bb = serializers.CharField()
    so = serializers.CharField()
    whip = serializers.CharField()
    kkper9 = serializers.CharField()
    bbper9 = serializers.CharField()
    hrper9 = serializers.CharField()

class PitchingStatsPostTableSerializer(serializers.Serializer):
    year = serializers.CharField()
    team = serializers.CharField()
    series = serializers.CharField()
    wins = serializers.CharField()
    losses = serializers.CharField()
    era = serializers.CharField()
    games = serializers.CharField()
    gamesstarted = serializers.CharField()
    cg = serializers.CharField()
    sho = serializers.CharField()
    sv = serializers.CharField()
    ip = serializers.CharField()
    tbf = serializers.CharField()
    h = serializers.CharField()
    r = serializers.CharField()
    er = serializers.CharField()
    hr = serializers.CharField()
    bb = serializers.CharField()
    so = serializers.CharField()
    whip = serializers.CharField()
    kkper9 = serializers.CharField()
    bbper9 = serializers.CharField()
    hrper9 = serializers.CharField()

class TeamOptionsSerializer(serializers.Serializer):
    name = serializers.CharField()
    franchid = serializers.CharField()

class TeamInfoSerializer(serializers.Serializer):
    activeteamname = serializers.CharField()
    seasons = serializers.CharField()
    record  = serializers.CharField()
    pennants = serializers.CharField()
    wswins = serializers.CharField()
    team_names = serializers.CharField()
    franchid = serializers.CharField()

class TeamSerializer(serializers.Serializer):
    year = serializers.CharField()
    teamname = serializers.CharField()
    league = serializers.CharField()
    rank = serializers.CharField()
    g = serializers.CharField()
    w = serializers.CharField()
    l = serializers.CharField()
    wlpercent = serializers.CharField()
    wswin = serializers.CharField()
    r = serializers.CharField()
    ra = serializers.CharField()
    attendance = serializers.CharField()
    park = serializers.CharField()

class ManagerOptionsSerializer(serializers.Serializer):
    name = serializers.CharField()
    playerid = serializers.CharField()

class ManagerInfoSerializer(serializers.Serializer):
    name = serializers.CharField()
    position = serializers.CharField()
    age = serializers.CharField()
    height = serializers.CharField()
    weight = serializers.CharField()
    games = serializers.CharField()
    wins = serializers.CharField()
    losses = serializers.CharField()
    winloss = serializers.CharField()

class ManagerStatTableSerializer(serializers.Serializer):
    year = serializers.CharField()
    team = serializers.CharField()
    league = serializers.CharField()
    g = serializers.CharField()
    w = serializers.CharField()
    l = serializers.CharField()
    winloss = serializers.CharField()
    rank = serializers.CharField()
    wswin = serializers.CharField()

#Not using Model Serializers

# class TeamsSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Teams
#         fields = '__all__' #__all__ keyword lets the serializer know all subject fields need to be serialized for transfer

# class PlayerSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Players
#         fields = ['birthyear', 'birthmonth', 'birthday', 'deathyear', 'deathmonth', 'deathday', 'namefirst', 'namelast', 'weight', 'height', 'bats', 'throws', 'debut', 'finalgame']

# #make serializers for pitching
# class PitchingStatsSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = Pitchingstats
#         fields = '__all__'

# class PitchingStatsPostSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = Pitchingstatspost
#         fields = '__all__'

# class BattingStatsSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Battingstats
#         fields = '__all__'

# class BattingStatsPostSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Battingstatspost
#         fields = '__all__'

# class FieldingStatsSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Fieldingstats
#         fields= '__all__'

# class FieldingStatsPostSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Fieldingstatspost
#         fields= '__all__'        

# class ManagerSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Managers
#         fields = '__all__'
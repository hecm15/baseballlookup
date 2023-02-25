from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from api.models import Teams, Players, Pitchingstats, Pitchingstatspost, Battingstats, Battingstatspost, Fieldingstats, Fieldingstatspost, Managers
from api.serializers import PlayerInfoSerializer, PlayerOptionsSerializer, BattingStatsTableSerializer, BattingStatsPostTableSerializer, FieldingStatsTableSerializer, FieldingStatsPostTableSerializer, PitchingStatsTableSerializer, PitchingStatsPostTableSerializer, TeamOptionsSerializer, TeamInfoSerializer, TeamSerializer,  ManagerOptionsSerializer, ManagerInfoSerializer, ManagerStatTableSerializer
from rest_framework.decorators import api_view
from django.db.models.functions import Concat
from django.db.models import Value, TextField


from .util import calculateAge, calculateHeight, walkpercentage, sopercentage, avg, calculateIP, calculateWHIP, calculateXPER, calculateWinLoss
from datetime import date

from .playerinfomethods import PlayerInformation, PlayerOptions, BattingStatsTable, BattingStatsPostTable, FieldingStatsTable, FieldingStatsPostTable, PitchingStatsTable, PitchingStatsPostTable, TeamOptions, TeamInfo, Team, ManagerOptions, ManagerInfo, ManagerStatTable



# Create your views here.



# API endpoint for Player Card Info Gathering
def player_info(request):
    param = request.GET
    playerid = param["playerid"]
    
    playerinfo = Players.objects.filter(playerid=playerid).values('birthyear', 'birthmonth', 'birthday', 'deathyear', 'deathmonth', 'deathday', 'namefirst', 'namelast', 'weight', 'height', 'bats', 'throws', 'debut', 'finalgame')
    playerposition = Fieldingstats.objects.filter(playerid=playerid).values('pos')

    if playerposition:  
        pos = playerposition[0]['pos']
    else:
        pos = ""

    for position in playerposition:
        if position['pos'] != pos:
            pos = pos + "/" + position['pos']
            break

    for field in playerinfo:
        name = field['namefirst'] + " " + field['namelast']
        if field['deathyear']:
            age = "Deceased"
        else:
            age = calculateAge(date(int(field['birthyear']), int(field['birthmonth']), int(field['birthday'])))
        height = (calculateHeight(field['height']) if field['height'] else "")
        weight = (field['weight'] if field['weight'] else "")
        bats = (field['bats'] if field['bats'] else "")
        throws = (field['throws'] if field['throws'] else "")

        playerdata = PlayerInformation(name, age, weight, height, bats, throws, pos)

    serialized = PlayerInfoSerializer(playerdata)

    return JsonResponse(serialized.data, safe=False)

# API endpoint for Player Search Options gathering
players_annotated = Players.objects.annotate(fullname=Concat('namefirst', Value(' ') ,'namelast', output_field=TextField())) # annotate players model once to join both namefirst and namelast and filter with name param 
def player_options(request):

    if request.method == 'GET':
        nameparam = request.GET
        name = nameparam['name']
        player_options = []

        possiblePlayers = players_annotated.filter(fullname__icontains=name)
        for player in possiblePlayers:
            if player.namefirst and player.namelast:
                name = player.fullname
                playerid = player.playerid
            else:
                continue

            if player.debut:
                debutyear = player.debut[:4]
            else:
                debutyear = ""

            player_options.append(PlayerOptions(name, playerid, debutyear))
         
        serialized = PlayerOptionsSerializer(player_options, many=True)
        
        return JsonResponse(serialized.data, safe=False)

# API endpoint, should return barry bonds 2001 regular szn batting stats
def batting_stats_search(request):
    if request.method == 'GET':
        params = request.GET
        playerid = params['playerid']

        battingstats = Battingstats.objects.filter(playerid=playerid)
        battingstatslist = []

        for stat in battingstats:
            team = Teams.objects.filter(teamid=stat.teamid).values('franchid').order_by('yearid')[:1]
            
            battingstatslist.append(BattingStatsTable(stat.yearid, team[0]['franchid'], stat.g, stat.ab, stat.r, stat.rbi, stat.h, stat.number_2b, stat.number_3b, stat.hr, walkpercentage(stat.bb, stat.ab), sopercentage(stat.so, stat.ab), stat.sb, stat.cs, avg(stat.h, stat.ab)))

        serialized = BattingStatsTableSerializer(battingstatslist, many=True)

        return JsonResponse(serialized.data, safe=False)

# API endpoint , should return Post Szn Batting Stats
def batting_stats_post_search(request):
     if request.method == 'GET':
        params = request.GET
        playerid = params['playerid']

        battingstats = Battingstatspost.objects.filter(playerid=playerid)
        battingstatslist = []

        for stat in battingstats:
            team = Teams.objects.filter(teamid=stat.teamid).values('franchid').order_by('yearid')[:1]
        
            battingstatslist.append(BattingStatsPostTable(stat.yearid, team[0]['franchid'], stat.round[:4], stat.g, stat.ab, stat.r, stat.rbi, stat.h, stat.number_2b, stat.number_3b, stat.hr, walkpercentage(stat.bb, stat.ab), sopercentage(stat.so, stat.ab), stat.sb, stat.cs, avg(stat.h, stat.ab)))

        serialized = BattingStatsPostTableSerializer(battingstatslist, many=True)
        
        return JsonResponse(serialized.data, safe=False)

# API endpoint returns fielding stats for regular szn
def fielding_stats_search(request):
    if request.method == 'GET':
        params = request.GET
        playerid = params['playerid']

        fieldingstats = Fieldingstats.objects.filter(playerid=playerid)
        fieldingstatslist = []

        for stat in fieldingstats:
            team = Teams.objects.filter(teamid=stat.teamid).values('franchid').order_by('yearid')[:1]

            fieldingstatslist.append(FieldingStatsTable(stat.yearid, team[0]['franchid'], stat.pos, stat.g, stat.gs, stat.innouts, stat.po, stat.a, stat.e, stat.dp, stat.pb, stat.wp, stat.sb, stat.cs, stat.zr))
        serialized = FieldingStatsTableSerializer(fieldingstatslist, many=True)

        return JsonResponse(serialized.data, safe=False)

# API endpoint fielding stats for post szn
def fielding_stats_post_search(request):
    if request.method == 'GET':
        params = request.GET
        playerid = params['playerid']

        fieldingstats = Fieldingstatspost.objects.filter(playerid=playerid)
        fieldingstatslist = []

        for stat in fieldingstats:
            team = Teams.objects.filter(teamid=stat.teamid).values('franchid').order_by('yearid')[:1]

            fieldingstatslist.append(FieldingStatsPostTable(stat.yearid, team[0]['franchid'], stat.round[:4], stat.pos, stat.g, stat.gs, stat.innouts, stat.po, stat.a, stat.e, stat.dp, stat.tp, stat.pb, stat.sb, stat.cs))
        serialized = FieldingStatsPostTableSerializer(fieldingstatslist, many=True)

        return JsonResponse(serialized.data, safe=False)

# API endpoint, should return pitching regular szn stats
def pitcher_stats_search(request):
    if request.method == 'GET': 
        params = request.GET
        playerid = params['playerid']

        pitchingstats = Pitchingstats.objects.filter(playerid=playerid)
        pitchingstatslist = []

        for stat in pitchingstats:
            team = Teams.objects.filter(teamid=stat.teamid).values('franchid').order_by('yearid')[:1]
            ip = calculateIP(stat.ipouts)
            whip = calculateWHIP(stat.bb, stat.h, ip)
            kkper9 = calculateXPER(stat.so, ip)   
            bbper9 = calculateXPER(stat.bb, ip)
            hrper9 = calculateXPER(stat.hr, ip)

            pitchingstatslist.append(PitchingStatsTable(stat.yearid, team[0]['franchid'], stat.w, stat.l, stat.era, stat.g, stat.gs, stat.cg, stat.sho, stat.sv, ip, stat.bfp, stat.h, stat.r, stat.er, stat.hr, stat.bb, stat.so, whip, kkper9, bbper9, hrper9))

        serialized = PitchingStatsTableSerializer(pitchingstatslist, many=True)

        return JsonResponse(serialized.data, safe=False)

# API endpoint, should return post szn stats
def pitcher_stats_post_search(request):
    if request.method == 'GET': 
        params = request.GET
        playerid = params['playerid']

        pitchingstats = Pitchingstatspost.objects.filter(playerid=playerid)
        pitchingstatslist = []

        for stat in pitchingstats:
            team = Teams.objects.filter(teamid=stat.teamid).values('franchid').order_by('yearid')[:1]
            ip = calculateIP(stat.ipouts)
            whip = calculateWHIP(stat.bb, stat.h, ip)
            kkper9 = calculateXPER(stat.so, ip)   
            bbper9 = calculateXPER(stat.bb, ip)
            hrper9 = calculateXPER(stat.hr, ip)

            pitchingstatslist.append(PitchingStatsPostTable(stat.yearid, team[0]['franchid'], stat.round[:4],stat.w, stat.l, stat.era, stat.g, stat.gs, stat.cg, stat.sho, stat.sv, ip, stat.bfp, stat.h, stat.r, stat.er, stat.hr, stat.bb, stat.so, whip, kkper9, bbper9, hrper9))

        serialized = PitchingStatsPostTableSerializer(pitchingstatslist, many=True)

        return JsonResponse(serialized.data, safe=False)

#API endpoint, should return team options for search
def team_options(request):
    if request.method == 'GET':
        nameparam = request.GET
        name = nameparam['name']
        team_options = []

        possibleTeams = Teams.objects.filter(name__icontains=name).filter(yearid='2021').distinct('franchid')
        for team in possibleTeams:
            if team.name:
                name = team.name
                franchid = team.franchid
            else:
                continue

            team_options.append(TeamOptions(name, franchid))
         
        serialized = TeamOptionsSerializer(team_options, many=True)
        
        return JsonResponse(serialized.data, safe=False)

# API endpoint, should return team info
def teams_info(request):
    if request.method == 'GET':
        franchidparam = request.GET
        franchid = franchidparam['franchid']
        team_table_query = Teams.objects.filter(franchid=franchid)

        all_team_names = team_table_query.values('name').distinct('name')
        
        firstseason = team_table_query.order_by('yearid')[:1]
        lastseason = team_table_query.order_by('-yearid')[:1]
        num_of_seasons = str(team_table_query.distinct().count())
        
        num_of_wins = 0
        num_of_losses = 0
        num_of_pennants = 0
        num_of_ws = 0
        for season in team_table_query:
            num_of_wins += int(season.w)
            num_of_losses += int(season.l)
            if season.lgwin ==  'Y':
                num_of_pennants += 1
            if season.wswin ==  'Y' and int(season.yearid) >= 1903:
                num_of_ws += 1
        win_loss_percentage = calculateWinLoss(num_of_wins, num_of_losses)
        
        active_team_name = team_table_query.filter(yearid="2021").values('name')
        seasons = num_of_seasons + " (" + firstseason[0].yearid + ' - ' + lastseason[0].yearid + ')'
        record = str(num_of_wins) + ' - ' + str(num_of_losses) + ', ' +  win_loss_percentage
        pennants = str(num_of_pennants)
        wswins = str(num_of_ws)
        team_names = [season['name'] for season in all_team_names]
        franchid = team_table_query[:1]

        serialized = TeamInfoSerializer(TeamInfo(active_team_name[0]['name'], seasons, record, pennants, wswins, team_names, franchid[0].franchid))

        return JsonResponse(serialized.data, safe=False)

#API endpoint Table team information
divsions = {
    'E' : 'East',
    'C' : 'Central',
    'W' : 'West'
}
def teams(request):
    if request.method == 'GET':
        franchidparam = request.GET
        franchid = franchidparam['franchid']
        team_table_query = Teams.objects.filter(franchid=franchid)

        listofseason = []

        for season in team_table_query:
            year = season.yearid
            teamname = season.name
            if season.lgid and season.divid:
               division = season.lgid + ' ' + divsions[season.divid]
            else:
                division = 'N/A'
            rank = season.rank
            games = season.g
            wins = season.w
            losses = season.l
            winlosspercent = calculateWinLoss(int(wins), int(losses))
            wswin = season.wswin
            runs = season.r
            runsallowed = season.ra
            attendance = season.attendance_field
            park = season.park

            listofseason.append(Team(year, teamname, division, rank, games, wins, losses, winlosspercent, wswin, runs, runsallowed, attendance, park))
        
        serialized = TeamSerializer(listofseason, many=True)

        return JsonResponse(serialized.data, safe=False)

# API endpoint, should return manager general info
managers_annotated = Players.objects.annotate(fullname=Concat('namefirst', Value(' ') ,'namelast', output_field=TextField()))
def manager_options(request):
    if request.method == 'GET':
        nameparam = request.GET
        managername = nameparam['name']

        possible_managers = managers_annotated.filter(fullname__icontains=managername)

        manager_options = []

        for manager in possible_managers:
            # if Managers.objects.filter(playerid=manager.playerid):
            if manager.namefirst and manager.namelast:
                name = manager.fullname
                playerid = manager.playerid
                manager_options.append(ManagerOptions(name, playerid))
                # else:
                #     continue

                # manager_options.append(ManagerOptions(name, playerid))

        

        stats_serializer = ManagerOptionsSerializer(manager_options, many=True)
        return JsonResponse(stats_serializer.data, safe=False)

def manager_info(request):
    if request.method == 'GET':
        playeridparam = request.GET
        managerplayerid = playeridparam['playerid']
       
        manager_careerstats = Managers.objects.filter(playerid=managerplayerid)

        personal_info = players_annotated.filter(playerid=managerplayerid)

        name = personal_info[0].fullname
        position = "Manager"
        if personal_info[0].deathyear:
            age = "Deceased"
        else:
            age = calculateAge(date(int(personal_info[0].birthyear), int(personal_info[0].birthmonth), int(personal_info[0].birthday)))
        height = (calculateHeight(personal_info[0].height) if personal_info[0].height else "")
        weight = (personal_info[0].weight if personal_info[0].weight else "")
        
        totalgames = 0
        num_of_wins = 0
        num_of_losses = 0

        for season in manager_careerstats:
            totalgames += int(season.g)
            num_of_wins += int(season.w)
            num_of_losses += int(season.l)

        winloss = calculateWinLoss(num_of_wins, num_of_losses)

        manager_info = ManagerInfo(name, position, age, height, weight, totalgames, str(num_of_wins), str(num_of_losses), winloss)
        
        serialized = ManagerInfoSerializer(manager_info)

        return JsonResponse(serialized.data, safe=False)

def manager_stats_search(request):
    if request.method == 'GET':
        playeridparam = request.GET
        managerplayerid = playeridparam['playerid']

        managercareer = Managers.objects.filter(playerid=managerplayerid)
        managerstats_list = []
        
        for season in managercareer:
            if season.inseason == '1':
                year = season.yearid
                team_query = Teams.objects.filter(teamid=season.teamid).filter(yearid=season.yearid).values('name', 'wswin')
                team = team_query[0]['name']
                league = season.lgid
                games = season.g
                wins = season.w
                losses = season.l
                winloss = calculateWinLoss(int(season.w), int(season.l))
                rank = season.rank
                wswin = team_query[0]['wswin']

                managerstats_list.append(ManagerStatTable(year, team, league, games, wins, losses, winloss, rank, wswin))
        
        serialized = ManagerStatTableSerializer(managerstats_list, many=True)

        return JsonResponse(serialized.data, safe=False)



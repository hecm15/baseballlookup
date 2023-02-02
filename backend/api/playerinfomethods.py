
class PlayerInformation:
    def __init__(self, name, age, weight, height, bats, throws, position) -> None:
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.bats = bats
        self.throws = throws
        self.position = position

class PlayerOptions:
    def __init__(self, name, playerid,debut) -> None:
        self.name = name
        self.playerid = playerid
        self.debut = debut

class BattingStatsTable:
    def __init__(self, year, team, games, atbats, runs, rbis, hits, doubles, triples, homeruns, bbpercent, sopercent, sb, cs, avg):
        self.year = year
        self.team = team
        self.games = games
        self.atbats = atbats
        self.runs = runs
        self.rbis = rbis
        self.hits = hits
        self.doubles = doubles
        self.triples = triples
        self.homeruns = homeruns
        self.bbpercent = bbpercent
        self.sopercent = sopercent
        self.sb = sb
        self.cs = cs
        self.avg = avg

class BattingStatsPostTable:
    def __init__(self, year, team, series, games, atbats, runs, rbis, hits, doubles, triples, homeruns, bbpercent, sopercent, sb, cs, avg):
        self.year = year
        self.team = team
        self.series = series
        self.games = games
        self.atbats = atbats
        self.runs = runs
        self.rbis = rbis
        self.hits = hits
        self.doubles = doubles
        self.triples = triples
        self.homeruns = homeruns
        self.bbpercent = bbpercent
        self.sopercent = sopercent
        self.sb = sb
        self.cs = cs
        self.avg = avg

class FieldingStatsTable:
    def __init__(self, year, team, position, games, gamesstarted, innouts, po, a, e, dp, pb, wp, sb, cs, zr):
        self.year = year
        self.team = team
        self.position = position
        self.games = games
        self.gamesstarted = gamesstarted
        self.innouts = innouts
        self.po = po
        self.a = a
        self.e = e
        self.dp = dp
        self.pb = pb
        self.wp = wp
        self.sb = sb
        self.cs = cs
        self.zr = zr

class FieldingStatsPostTable:
    def __init__(self, year, team, series, position, games, gamesstarted, innouts, po, a, e, dp, tp, pb, sb, cs):
        self.year = year
        self.team = team
        self.series = series
        self.position = position
        self.games = games
        self.gamesstarted = gamesstarted
        self.innouts = innouts
        self.po = po
        self.a = a
        self.e = e
        self.dp = dp
        self.tp = tp
        self.pb = pb
        self.sb = sb
        self.cs = cs

class PitchingStatsTable:
    def __init__(self, year, team, wins, losses, era, games, gamesstarted, cg, sho, sv, ip, tbf, h, r, er, hr, bb, so, whip, kkper9, bbper9, hrper9):
        self.year = year
        self.team = team
        self.wins = wins
        self.losses = losses
        self.era = era
        self.games = games
        self.gamesstarted = gamesstarted
        self.cg = cg
        self.sho = sho
        self.sv = sv
        self.ip = ip
        self.tbf = tbf
        self.h = h
        self.r = r
        self.er = er
        self.hr = hr
        self.bb = bb
        self.so = so
        self.whip = whip
        self.kkper9 = kkper9
        self.bbper9 = bbper9
        self.hrper9 = hrper9

class PitchingStatsPostTable:
    def __init__(self, year, team, series,wins, losses, era, games, gamesstarted, cg, sho, sv, ip, tbf, h, r, er, hr, bb, so, whip, kkper9, bbper9, hrper9):
        self.year = year
        self.team = team
        self.series = series
        self.wins = wins
        self.losses = losses
        self.era = era
        self.games = games
        self.gamesstarted = gamesstarted
        self.cg = cg
        self.sho = sho
        self.sv = sv
        self.ip = ip
        self.tbf = tbf
        self.h = h
        self.r = r
        self.er = er
        self.hr = hr
        self.bb = bb
        self.so = so
        self.whip = whip
        self.kkper9 = kkper9
        self.bbper9 = bbper9
        self.hrper9 = hrper9
        
class TeamOptions:
    def __init__(self, name, teamid):
       self.name = name
       self.franchid = teamid

class TeamInfo:
    def __init__(self, activeteamname, seasons ,record, pennants, wswins, team_names, teamid):
        self.activeteamname = activeteamname
        self.seasons = seasons
        self.record = record
        self.pennants = pennants
        self.wswins = wswins
        self.team_names = team_names
        self.franchid = teamid

class Team: 
    def __init__(self, yearid, teamname, league, rank, g, w, l, wlpercent, wswin, r, ra, attendance, park):
        self.year = yearid
        self.teamname = teamname
        self.league = league
        self.rank = rank
        self.g = g
        self.w = w
        self.l = l
        self.wlpercent = wlpercent
        self.wswin = wswin
        self.r = r
        self.ra = ra
        self.attendance = attendance
        self.park = park

class ManagerOptions:
    def __init__(self, name, playerid):
        self.name = name
        self.playerid = playerid

class ManagerInfo:
    def __init__(self, name, position, age, height, weight, games, wins, losses, winloss):
        self.name = name 
        self.position = position 
        self.age = age
        self.height = height
        self.weight = weight
        self.games = games
        self.wins = wins
        self.losses = losses
        self.winloss = winloss

class ManagerStatTable:
    def __init__(self, year, team, league, g, w, l, winloss, rank, wswin):
        self.year = year
        self.team = team
        self.league = league
        self.g = g
        self.w = w
        self.l = l
        self.winloss = winloss
        self.rank = rank
        self.wswin = wswin
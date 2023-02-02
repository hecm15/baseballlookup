from django.urls import re_path
from api import views

urlpatterns = [
    re_path(r'^api/teaminfo$', views.teams_info),
    re_path(r'^api/teamoptions$', views.team_options),
    re_path(r'^api/teams$', views.teams),
    re_path(r'^api/pitchers$', views.pitcher_stats_search),
    re_path(r'^api/pitcherspostszn$', views.pitcher_stats_post_search),
    re_path(r'^api/batters$', views.batting_stats_search),
    re_path(r'^api/batterspostszn$', views.batting_stats_post_search),
    re_path(r'^api/fielders$', views.fielding_stats_search),
    re_path(r'^api/fielderspostszn$', views.fielding_stats_post_search),
    re_path(r'^api/manageroptions$', views.manager_options),
    re_path(r'^api/managerinfo$', views.manager_info),
    re_path(r'^api/managers$', views.manager_stats_search),
    re_path(r'^api/playerinfo$', views.player_info),
    re_path(r'^api/playeroptions$', views.player_options),
]
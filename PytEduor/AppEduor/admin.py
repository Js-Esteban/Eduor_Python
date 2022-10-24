from django.contrib import admin
from . models import Player, Position, Team, Coach

# Register your models here.

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('team_name','image_flag','image_shield')
    
@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('player_name',)

@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ('coach_name',)
    
    
@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('position_name',)
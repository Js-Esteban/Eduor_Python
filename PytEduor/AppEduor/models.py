from tabnanny import verbose
from django.db import models
from django.utils.html import format_html
from django import forms
# Create your models here.

       
class Team(models.Model):
    team_name = models.CharField(max_length=30, verbose_name='Nombre del Equipo')
    image_flag = models.ImageField(upload_to='media', verbose_name='Imagen Bandera')
    image_shield = models.ImageField(upload_to='media', verbose_name='Escudo del Equipo')
    
    
    def __str__(self):
        return self.team_name
    
    class Meta:
        verbose_name = 'Equipo'
        verbose_name_plural = 'equipo'
        db_table = 'Team'

class Coach(models.Model):
    coach_name = models.CharField(max_length=30, verbose_name='Nombre')
    coach_surname = models.CharField(max_length=30, verbose_name='Apellido')
    coach_datebirth = models.DateTimeField(verbose_name='Fecha De Nacimiento')
    coach_nacionality = models.CharField(max_length=30, verbose_name='Nacionalidad')
    coach_rol = models.CharField(max_length=20, verbose_name='Rol')
    team= models.ForeignKey(Team,null=True,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.coach_name
    
    class Meta:
        verbose_name = 'Técnico'
        verbose_name_plural = 'técnico'
        db_table = 'Coach'

        
class Player(models.Model):
    player_name = models.CharField(max_length=30, verbose_name='Nombre')
    player_surname = models.CharField(max_length=30, verbose_name='Apellido')
    image_photoplayer = models.ImageField(upload_to='media', verbose_name='Foto del jugador')
    player_datebirth = models.DateTimeField(verbose_name='Fecha De Nacimiento')
    player_position = models.CharField(max_length=50, verbose_name='Posición en la que juega')
    player_numshirt = models.CharField(max_length=2, verbose_name='Número de camiseta')
    player_headline = models.CharField(max_length=30, verbose_name='¿Es Titular?')
    player_team = models.CharField(max_length=30, verbose_name='Equipo')
    team= models.ForeignKey(Team,null=True,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.player_name
    
    class Meta:
        verbose_name = 'Jugador'
        verbose_name_plural = 'jugador'
        db_table = 'Player'
        
class Position(models.Model):
    position_name = models.CharField(max_length = 5, verbose_name= 'Abreviación')
    position_description = models.CharField(max_length=50, verbose_name='Descripción')
    player=models.ForeignKey(Player,null=True,on_delete=models.CASCADE)

    def _str_(self):
        return self.position_name
    
    class Meta:
        verbose_name = "Posicion"
        verbose_name_plural = "Posiciones"
        db_table = "positions"

    
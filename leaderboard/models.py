from django.db import models
# Create your models here.


class Player(models.Model):
    Player_Name = models.CharField(max_length=32)
    def __str__(self):
        return self.Player_Name
class Team(models.Model):
    Player1 = models.ForeignKey(Player, related_name='Player1', on_delete=models.CASCADE)
    Player2 = models.ForeignKey(Player, related_name='Player2', on_delete=models.CASCADE)
    Team_Name = models.CharField(max_length=32)
    def __str__(self):
        return self.Team_Name
class Game(models.Model):
    team1 = models.ForeignKey(Team, related_name='team1', on_delete=models.CASCADE)
    team2 = models.ForeignKey(Team, related_name='team2', on_delete=models.CASCADE)
    Game_Name = models.CharField(max_length=32)
    def __str__(self):
        return self.Game_Name
class Score(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    score = models.IntegerField()
class Result(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

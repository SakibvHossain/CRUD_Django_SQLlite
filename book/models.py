from django.db import models

class Book(models.Model):
    player_name = models.CharField(max_length=100)
    player_email = models.CharField(max_length=100)
    team_role = models.CharField(max_length=100)
    team_logo = models.ImageField()
    game_name = models.CharField(max_length=100)
    team_code = models.IntegerField()

    def __str__(self):
        return self.player_name

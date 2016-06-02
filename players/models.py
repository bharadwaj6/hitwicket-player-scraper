"""Models for players app."""

from django.db import models


class PlayerDetails(models.Model):
    """Models for storing player details."""

    age = models.CharField(null=True, max_length=12)
    name = models.CharField(null=True, max_length=1024)
    player_id = models.IntegerField()
    region = models.CharField(max_length=255)
    skill_index = models.IntegerField()
    exp = models.CharField(max_length=255)
    form = models.CharField(max_length=23)
    fitness = models.CharField(max_length=255)
    salary = models.IntegerField()
    team_id = models.IntegerField(null=True)

    def get_player_url(self):
        """Get player_url from player_id in details."""
        pass


class DivTeamDetails(models.Model):
    """Store team_id and div relations."""

    team_id = models.IntegerField()
    div_id = models.IntegerField()
    league_id = models.IntegerField()

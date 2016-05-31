from django.db import models

class PlayerDetails(models.Model):
    age = models.CharField(null=True, max_length=12)
    name = models.CharField(null=True, max_length=1024)
    player_id = models.IntegerField()
    region = models.CharField(max_length=255)
    skill_index = models.IntegerField()
    exp = models.CharField(max_length=255)
    form = models.CharField(max_length=23)
    fitness = models.CharField(max_length=255)
    salary = models.IntegerField()

    def get_player_id(self):
        pass

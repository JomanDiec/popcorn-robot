from django.db import models

# Create your models here.
class GameState(models.Model):
    new_game = models.BooleanField(default=True)
    health = models.IntegerField(default=5)
    bedroom_key = models.BooleanField(default=False)
    front_key = models.BooleanField(default=False)
    jack_found = models.BooleanField(default=False)

    def __str__(self):
        return f" is it a new game: {self.new_game}, health is currently: {self.health}, is the bedroom key found: {self.bedroom_key}, is the front door key found {self.front_key}, has jack been found: {self.jack_found}"

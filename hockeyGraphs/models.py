from django.db import models

# A table for keeping track of players searched by the user
class Player(models.Model):
    fullName = models.CharField(max_length = 30)

    def __str__(self):
        return self.fullName
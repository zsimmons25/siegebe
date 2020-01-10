from django.db import models


class Siege(models.Model):
    operator = models.CharField(max_length=20)
    faction = models.TextField()
    gadget = models.TextField()
    equipment = models.TextField()
    armor = models.PositiveSmallIntegerField()
    speed = models.PositiveSmallIntegerField()
    counters = models.TextField()

    def _op_(self):
        return self.operator
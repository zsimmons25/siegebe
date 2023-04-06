from django.db import models


class Siege(models.Model):
    operator = models.CharField(max_length=20)
    faction = models.TextField()
    gadget = models.TextField()
    equip1 = models.TextField()
    equip2 = models.TextField()
    armor = models.PositiveSmallIntegerField()
    speed = models.PositiveSmallIntegerField()
    side = models.TextField()
    prim1 = models.TextField()
    prim2 = models.TextField()
    prim3 = models.TextField()
    secon1 = models.TextField()
    secon2 = models.TextField()
    count1 = models.TextField()
    count1p = models.TextField()
    count2 = models.TextField()
    count2p = models.TextField()
    release = models.TextField()

    def _op_(self):
        return self.operator

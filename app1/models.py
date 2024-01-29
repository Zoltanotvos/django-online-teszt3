from django.db import models

# Create your models here.
class Adatbázismodell(models.Model):
    szöveg = models.CharField(max_length = 20)
    szám = models.IntegerField()
    boool = models.BooleanField(default = False)
    class Meta:
        verbose_name_plural = "adatbázis adatok"
    def __str__(self):
        return f"{self.szöveg}"
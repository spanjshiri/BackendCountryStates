from django.db import models

class Country(models.Model):
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=20)

    def __str__(self):
        return str(self.name)

class State(models.Model):
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=20)
    country = models.ForeignKey(Country, related_name='states', on_delete=models.CASCADE)
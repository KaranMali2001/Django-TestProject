from django.db import models

class User(models.Model):
    age = models.IntegerField()
    name= models.CharField(max_length=10)

    def __str__(self):
        return self.name
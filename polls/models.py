from django.db import models

# Create your models here.

class Categorie (models.Model):
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return self.title


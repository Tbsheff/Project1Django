from django.db import models

class Flavor(models.Model):
    id = models.AutoField(primary_key=True)  
    flavorname = models.CharField(max_length=100)  
    img = models.URLField(max_length=255)  

    def __str__(self):
        return self.flavorname  


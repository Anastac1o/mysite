from django.db import models

class Item(models.Model):
    titulo = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.FloatField(default=0.0)
    estante = models.SmallIntegerField(default=0)
    prateleira = models.SmallIntegerField(default=0)
    is_rare = models.BooleanField(default=False)
    is_first_edition = models.BooleanField(default=False)
    is_used = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/')
    
    

    def __str__(self):
        return self.titulo + ":" + self.author

   

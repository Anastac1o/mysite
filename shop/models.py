from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    is_rare = models.BooleanField(default=False)
    is_first_edition = models.BooleanField(default=False)
    is_used = models.BooleanField(default=False)
    is_new = models.BooleanField(default=False)
    image = models.ImageField()

    def __str__(self):
        return self.name + " : " + self.author


    

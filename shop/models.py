from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.FloatField(default=0.0)
    is_rare = models.BooleanField(default=False)
    is_first_edition = models.BooleanField(default=False)
    is_used = models.BooleanField(default=False)
    image = models.ImageField(upload_to='shop/item_images', verbose_name='My Image')
    

    def __str__(self):
        return self.name + ":" + self.author

   

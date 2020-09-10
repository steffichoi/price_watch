from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    source = models.CharField(max_length=50)

    def __str__(self):
        return self.name
        



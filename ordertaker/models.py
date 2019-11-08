from django.db import models

# Create your models here.
class Order(models.Model):
    name = models.CharField(max_length=100, default='')
    order = models.CharField(max_length=100)
    size = models.CharField(max_length=5, default='')
    sugar_level = models.CharField(max_length=10, blank=True, default='')
    notes = models.TextField(blank=True)
    addons = models.TextField(blank=True)

    def __str__(self):
        return self.name + ': ' + self.order
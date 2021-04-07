from django.db import models

class CustomerRequestModel(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    category = models.CharField(max_length=100, verbose_name='Interested Product')

    def __str__(self):
        return self.name

from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    image = models.TextField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.id} {self.name}'

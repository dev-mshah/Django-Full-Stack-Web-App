from django.db import models
from django.utils import timezone

# Create your models here.
class ChaiVariety(models.Model):
    CHAI_TYPE_CHOICE = [
        ('ML', 'MASALA'),
        ('GR', 'GINGER'),
        ('KL', 'KIWI'),
        ('PL', 'PLAIN'),
        ('EL', 'ELACHI'),


    ]
    name = models.CharField(max_length=100)
    date_added = models.DateTimeField(default=timezone.now)
    type= models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)


    def __str__(self):
        return self.name
    
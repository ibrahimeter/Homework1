from django.core.serializers import serialize
from django.db import models

# Create your models here.

class Customuser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.first_name + self.last_name

    def serialize(self):
        return {
            "id":self.id,
            "first_name": self.first_name,
            "last_name" :self.last_name,
            "email" : self.email
               }
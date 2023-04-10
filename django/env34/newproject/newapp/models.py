from django.db import models

# Create your models here.


class employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    desc = models.TextField(max_length=500)
    phoneNumber = models.IntegerField()

    def __str__(self):
        return self.name

from django.db import models

# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=100, null=False)
    location = models.CharField(max_length=200)

    def __str__(self):  # when using this function this will display name attribute on the tile of each object in admin panel
        return self.name


class Roles(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class Employee(models.Model):
    firstName = models.CharField(max_length=100, null=False)
    lastName = models.CharField(max_length=100)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    role = models.ForeignKey(Roles, on_delete=models.CASCADE)
    phone = models.IntegerField(default=0)
    hire_date = models.DateField()

    def __str__(self):
        # using this we can print out more than one attributes
        return "%s %s" % (self.firstName, self.lastName)

from django.db import models

# Create your models here.
class faculty(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    age=models.IntegerField()
    contact=models.IntegerField()
    course=models.CharField(max_length=100)
    designation=models.CharField(max_length=100)
    phoneNo=models.IntegerField()
    address=models.CharField(max_length=100)
    id_no=models.IntegerField()
    department=models.CharField(max_length=100)
    joining_date=models.DateField()
    qualification=models.CharField(max_length=100)
    vehicle_no=models.IntegerField()
    expertise=models.CharField(max_length=100)
    description=models.TextField(500)

    def __str__(self):
      return self.fname


class student(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    age=models.IntegerField()
    contact=models.IntegerField()
    course=models.CharField(max_length=100)
    father_name=models.CharField(max_length=50)
    id_no=models.IntegerField()
    department=models.CharField(max_length=100)
    joining_date=models.DateField()
    universty_name=models.CharField(max_length=100)
    description=models.TextField(500)

    def __str__(self):
        return self.fname
    

class cs(models.Model):
    dean_name=models.CharField(max_length=100)
    head_name=models.CharField(max_length=100)
    joining_date=models.DateField()
    technologies=models.CharField(max_length=100)
    universty_name=models.CharField(max_length=100)
    description=models.TextField(500)

    def __str__(self):
        return self.dean_name
    

class se(models.Model):
    dean_name=models.CharField(max_length=100)
    head_name=models.CharField(max_length=100)
    joining_date=models.DateField()
    technologies=models.CharField(max_length=100)
    universty_name=models.CharField(max_length=100)
    description=models.TextField(500)

    def __str__(self):
        return self.dean_name    
    

    


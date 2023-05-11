from django.db import models

# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=100, null=False)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100,)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    phone = models.IntegerField(default=0)
    hire_date = models.DateField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Meeting(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=1000)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.name


class Expense_Training(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=1000)
    emp = models.ForeignKey(Employee, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    date = models.DateField()


class Training(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=1000)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()


class Task(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=1000)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()


class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=20, choices=[
        ('present', 'Present'),
        ('absent', 'Absent'),
        ('late', 'Late'),
    ])

    def __str__(self):
        return f"{self.employee} on {self.date}: {self.status}"


class Payroll(models.Model):
    emp = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    basic_pay = models.IntegerField(default=0)
    overtime_pay = models.IntegerField(default=0)
    tax_deducted = models.IntegerField(default=0)
    net_pay = models.IntegerField(default=0)


class Feedback(models.Model):
    description = models.CharField(max_length=100, null=False)
    dept_name = models.CharField(max_length=100)

    def __str__(self):
        return self.dept_name

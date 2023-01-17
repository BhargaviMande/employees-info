from django.db import models

# Create your models here.
class department(models.Model):
    name=models.CharField(max_length=30)
    location=models.CharField(max_length=30)
    def __str__(self):
        return self.name
class role(models.Model):
    name=models.CharField(max_length=30)
    def __str__(self):
        return self.name
class employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    role = models.ForeignKey(role, on_delete=models.CASCADE)
    department = models.ForeignKey(department,on_delete=models.CASCADE)
    hire_date = models.DateField(max_length=30)
    bonus = models.IntegerField()
    salary = models.IntegerField()
    phone = models.IntegerField()
    def __str__(self):
        return '%s %s ' %(self.first_name,self.last_name)



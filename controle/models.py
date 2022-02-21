from django.utils import timezone
from django.db import models

class Validator(models.Model):
    number = models.IntegerField()
    vmodel = models.CharField(max_length=10)
    
class Company(models.Model):
    name = models.CharField(max_length=45)
    responsable = models.CharField(max_length=60)
    
    def __str__(self):
        return self.name
    
class Responsable(models.Model):
    name = models.CharField(max_length=45)
    
    def __str__(self):
        return self.name

class Service(models.Model):
    validator = models.ForeignKey(Validator, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    issue = models.TextField()
    arrived_date = models.DateTimeField(auto_now_add=timezone.now)
    observation = models.TextField()
    responsable = models.ForeignKey(Responsable, on_delete=models.CASCADE)
    Released_date = models.DateField()
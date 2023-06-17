from django.db import models

# Create your models here.
class Questions(models.Model):
    questions = models.CharField(max_length=500)

class Inspection(models.Model):
    images = models.ImageField(upload_to='images/')
    registration_number = models.CharField(max_length=200)
    description = models.CharField(max_length=900)
    values = models.CharField(max_length=200)
    inspection_person = models.CharField(max_length=200)
    car_brand = models.CharField(max_length=200)
    car_model = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
    variant = models.CharField(max_length=200)
    meter_reading = models.CharField(max_length=200)

class Checkbox(models.Model):
    inspection_id = models.ForeignKey(Inspection,on_delete = models.CASCADE)
    questions_id = models.ForeignKey(Questions,on_delete = models.CASCADE)

class signup(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobile_number = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50)

class Purchase(models.Model):
    inspection_id = models.ForeignKey(Inspection,on_delete = models.CASCADE)
    date = models.DateField()
    amount = models.CharField(max_length=100)
from django.db import models

class Service(models.Model):
    img = models.ImageField()
    title = models.CharField(max_length=255)
    description = models.TextField()

class Doctor(models.Model):
    img = models.ImageField(blank=False)
    name = models.CharField(max_length=255)
    service = models.ForeignKey(Service,on_delete=models.CASCADE)
    about = models.TextField()
    facebook_l = models.URLField(blank=True)
    twitter_l = models.URLField(blank=True)
    instagramm_l = models.URLField(blank=True)

class Contact(models.Model):
    img = models.ImageField(blank=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=500,blank=True)
    message = models.TextField()

class Info(models.Model):
    number = models.CharField(max_length=18)
    address = models.TextField()
    email = models.EmailField()
    doctors_count = models.PositiveIntegerField(
        default=Doctor.objects.count(),editable=False)
    total_patient = models.PositiveIntegerField()
    medical_stuff = models.PositiveIntegerField()
    map_link = models.URLField(blank=True)

    facebook_l = models.URLField(blank=True)
    twitter_l = models.URLField(blank=True)
    instagramm_l = models.URLField(blank=True)
    youtube_l = models.URLField(blank=True)


class Order(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=18)
    date = models.DateField()
    time = models.TimeField()
    doctor = models.ForeignKey(Doctor,
                               on_delete=models.CASCADE)
    problem_text = models.TextField()

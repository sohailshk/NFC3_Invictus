from django.db import models

class Volunteer(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='volunteer_photos/')
    description = models.TextField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name

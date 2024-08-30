from django.db import models

class Donation(models.Model):
    image = models.ImageField(upload_to='donation_images/')
    description = models.TextField()
    goal_amount = models.DecimalField(max_digits=10, decimal_places=2)
    current_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f"Donation {self.id}"
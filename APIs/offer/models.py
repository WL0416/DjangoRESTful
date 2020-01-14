from django.db import models

class Offer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthday = models.CharField(max_length=10)
    passport = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=150)
    start_date = models.CharField(max_length=10)
    courses = models.CharField(max_length=20)
    campus = models.CharField(default='Melbourne', max_length=15)

    class Meta:
        ordering = ['start_date']

    def __str__(self):
        return self.first_name

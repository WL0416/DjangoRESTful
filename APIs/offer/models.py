from django.db import models


class Offer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthday = models.DateField()
    passport = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=150)
    issue_date = models.DateField(auto_now=True)
    start_date = models.DateField()
    courses = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name

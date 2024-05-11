from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=120)

INSTITUTIONS = (
    ("fundacja", "fundacja"),
    ("organizacja pozarządowa", "organizacja pozarządowa"),
    ("zbiórka lokalna", "zbiórka lokalna"),
)


class Institution(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    type = models.CharField(max_length=60, choices=INSTITUTIONS, default="fundacja")
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name

class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=20)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, default=None)
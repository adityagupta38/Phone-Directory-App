from django.db import models

# Create your models here.


class Contacts(models.Model):
    name = models.CharField(max_length=155, unique=True)
    countryCode = models.CharField(max_length=10, blank=True)
    contactNo = models.IntegerField()
    email = models.EmailField(blank=True)

    class Meta:
        db_table = 'Phone Directory'

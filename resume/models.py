from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=60, null=True)
    last_name = models.CharField(max_length=60, null=True)
    email_address = models.EmailField(max_length=150, null=True)
    message = models.TextField( max_length=2000, null=True)

    def __str__(self):
        return self.first_name
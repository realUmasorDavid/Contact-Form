from django.db import models

# Create your models here.

class contact(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
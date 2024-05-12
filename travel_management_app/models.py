from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)  # Note: Storing passwords in plain text is not secure. Use hashing in real-world scenarios.

    def __str__(self):
        return self.username
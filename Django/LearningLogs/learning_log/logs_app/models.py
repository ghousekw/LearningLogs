from django.db import models


# Create your models here.

class Topic(models.Model):
    """A topic that user wants to Learn"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Represent a string representation of model."""
        return self.text[:50]

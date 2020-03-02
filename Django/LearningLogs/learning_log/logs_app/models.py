from django.db import models


# Create your models here.

class Topic(models.Model):
    """A topic that user wants to Learn"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Represent a string representation of model."""
        return self.text[:50]


class Entry(models.Model):
    """Each topic can be associated with many entries"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.text[:50] + "..."

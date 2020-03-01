# from django.db import models

# # Create your models here.
# class Headline(models.Model):
#     title = models.CharField(max_length=200)
#     image = models.URLField(null=True, blank=True)
#     url = models.TextField()

#     def __str__(self):
#         return self.title
from django.db import models

# Create your models here.

class Feed(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Article(models.Model):
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    url = models.URLField()
    description = models.TextField()
    publication_date = models.DateTimeField()

    def __str__(self):
        return self.title
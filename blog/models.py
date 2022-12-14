from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=50)
    short_description = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
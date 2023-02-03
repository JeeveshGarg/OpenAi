from django.db import models

# Create your models here.

class Summary(models.Model):
    text = models.TextField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.text
from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=100)
    priority = models.IntegerField()

    def __str__(self):
        return self.name

from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField()
    Date = models.DateField(blank=False)

    def __str__(self):
        return self.title
from django.db import models
class Kompyuter(models.Model):
    name = models.CharField(max_length=100)
    system = models.CharField(max_length=100)
    cost = models.CharField(max_length=50)
    about = models.TextField()

    def __str__(self):
        return self.name

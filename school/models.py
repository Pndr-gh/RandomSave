from django.db import models

class Classroom(models.Model):
    capacity = models.PositiveIntegerField()
    area = models.PositiveIntegerField()
    name = models.CharField(max_length = 50)
    department = models.CharField(max_length = 50)
from django.db import models

# Create your models here.
class AjaxMe(models.Model):
    checkbox = models.BooleanField(default = False)

    def __bool__(self):
        return self.checkbox

class Animal(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField(blank = True, null = True)

    def __str__(self):
        return self.name

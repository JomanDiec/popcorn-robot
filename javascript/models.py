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

class QuoteMe(models.Model):
    quote = models.CharField(max_length=255)
    author = models.CharField(max_length = 100)

    def __str__(self):
        return self.quote

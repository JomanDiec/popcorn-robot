from django.db import models

# Create your models here.
class AjaxMe(models.Model):
    checkbox = models.BooleanField(default = False)

    def __bool__(self):
        return self.checkbox

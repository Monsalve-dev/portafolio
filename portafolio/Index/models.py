from django.db import models

# Create your models here.
class Project(models.Model):
    Nombre = models.CharField(primary_key=True, max_length=250)
    link = models.CharField(max_length=800)
    
    def __str__(self):
        text= "{0} ({1})"
        return text.format(self.Nombre, self.link)
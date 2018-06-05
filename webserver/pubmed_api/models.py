from django.db import models

# Create your models here.

class PubmedApi(models.Model):
    name = models.CharField('NAME', max_length=20, primary_key=True)
    url = models.CharField('URL', max_length=20, null=True)
    description = models.TextField('DESCRIPTION')

    def __str__(self):
        return self.name
    

from django.db import models

# Create your models here.

class Slideshow(models.Model):
    img = models.ImageField(upload_to='Slideshow', default='-')

    def __dir__(self):
        return self.img

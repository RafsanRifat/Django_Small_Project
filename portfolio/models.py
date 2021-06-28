from django.db import models

# Create your models here.

class HeroSection(models.Model):
    image = models.ImageField(upload_to='hero_image/', default=1)
    name = models.CharField(max_length=100, default=1)
    title = models.TextField(max_length=200, default=1)

    def __str__(self):
        return self.name

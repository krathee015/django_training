from django.db import models

class MovieModel(models.Model):
    moviename = models.CharField(max_length=50)
    directedby = models.CharField(max_length=50)
    releasedate = models.DateField()

    def __str__(self):
        return self.moviename
    



# Create your models here.

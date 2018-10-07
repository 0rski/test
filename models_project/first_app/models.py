from django.db import models

# Create your models here.
class Topics(models.Model):
    top_name = models.CharField(max_length=260, unique=True)

    def __str__(self):
        return self.top_name

class Website(models.Model):
    topic = models.ForeignKey(Topics, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name

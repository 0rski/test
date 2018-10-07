from django.db import models

# Create your models here.
# class User(models.Model):
#     user_name = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.user_name

class User(models.Model):
    # un = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, default="")
    last_name = models.CharField(max_length=100, default="")
    email = models.EmailField(blank=True, default="")

    def __str__(self):
        return self.first_name

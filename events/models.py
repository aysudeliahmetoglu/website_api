from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Events(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    def __str__(self):
        return self.name
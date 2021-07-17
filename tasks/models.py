from django.db import models
from django.contrib.auth.models import User

# Create your models here.


USER_ID = 1


class Task(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    is_done = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=USER_ID)

    def __str__(self):
        return self.title

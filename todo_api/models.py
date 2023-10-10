from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)
    task = models.CharField(max_length = 100)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    completed = models.BooleanField(default = False, blank = True)
    updated = models.DateTimeField(auto_now = True, blank = True)
    

    def __str__(self):
        return self.task
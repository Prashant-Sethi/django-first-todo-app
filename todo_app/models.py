from django.db import models

# Create your models here.

class ToDo(models.Model):
    added_date = models.DateTimeField(auto_now=True)
    text = models.TextField(max_length=200)

    def __str__(self):
        return f'{self.text}'
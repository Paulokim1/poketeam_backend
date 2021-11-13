from django.db import models


class Pokemon(models.Model):
    name = models.CharField(max_length=200)
    type = models.TextField(default='DEFAULT VALUE')


    def __str__(self):
        return f"{self.id}. {self.title}"



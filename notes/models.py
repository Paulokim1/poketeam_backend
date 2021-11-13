from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(default='DEFAULT VALUE')
    img = models.TextField(default='DEFAULT VALUE')


    def __str__(self):
        return f"{self.id}. {self.title}"



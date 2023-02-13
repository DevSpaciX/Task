from django.db import models


class Tag(models.Model):
    title = models.CharField(max_length=15)

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=100)
    is_done = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

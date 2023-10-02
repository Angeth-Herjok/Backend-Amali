from django.db import models

class Comment(models.Model):
    full_name = models.CharField(max_length=255)
    comment = models.TextField()
    likes = models.IntegerField()

    def __str__(self):
        return self.comment

    def add_like(self):
        self.likes += 1
        self.save()

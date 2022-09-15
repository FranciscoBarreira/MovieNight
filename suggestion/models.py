from django.db import models


class MakeSuggestion(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.email

from django.db import models

# Create your models here.


class Comment(models.Model):
    name = models.CharField(max_length=100)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Now set it back to auto_now_add

    def __str__(self):
        return self.name


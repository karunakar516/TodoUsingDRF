from django.db import models
class Todo(models.Model):
    title=models.CharField(max_length=20)
    description=models.TextField()
    def __str__(self):
        return str(self.title)
    
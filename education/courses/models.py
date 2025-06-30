from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    instructor = models.CharField(max_length=100)
    duration = models.IntegerField(help_text="Duration in hours")

    def __str__(self):
        return self.title

from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to="events_thumbnail", blank=True)
    date = models.DateTimeField()
    location = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title


    class Meta:
        ordering = ["-date"]
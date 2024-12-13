from django.db import models
from django.contrib.auth import get_user_model

class PortfolioItem(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    screenshot = models.ImageField(upload_to='portfolio/screenshots/')
    link = models.URLField(blank=True, null=True)
    file = models.FileField(upload_to='portfolio/files/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


    class Meta:
        ordering = ["-created_at"]
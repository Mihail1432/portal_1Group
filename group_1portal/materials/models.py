from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
class Material(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to="materials_files/", blank=True)
    video = models.URLField(blank=True)

    def __str__(self):
        return self.name

    def get_file_name(self):
        return self.file.name.split("/")[-1]
    
    class Meta:
        ordering = ["-uploaded_at"]
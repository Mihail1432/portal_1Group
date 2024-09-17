from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth import get_user_model

# Create your models here.
class Grade(models.Model):
    student = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="grades")
    logiks = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    date = models.DateField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.student} - {self.logiks}"
    
    class Meta:
        ordering = ["date"]
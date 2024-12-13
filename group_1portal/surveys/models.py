from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Survey(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

    def get_users_that_completed(self):
        users = set(
            user 

            for question in self.questions.all() 
            for option in question.options.all() 
            for user in option.users.all()
        )

        return list(users)
    
    def save_submition(self, request):
        for question in self.questions.all():
            chosed_options_id = request.POST.getlist(str(question.id))
            options = question.options.all().filter(id__in=chosed_options_id)

            for option in options:
                option.users.add(request.user)

    
    class Meta:
        ordering = ["-created_at"]

class Question(models.Model):
    TYPE_CHOICES = (
        ("single", "Single choice"),
        ("multiple", "Multiple choice")
    )

    text = models.CharField(max_length=150)
    type = models.CharField(choices=TYPE_CHOICES, max_length=25, default="single")
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name="questions")


class Option(models.Model):
    value = models.CharField(max_length=150)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="options")

    users = models.ManyToManyField(get_user_model(), blank=True, related_name="chosed_surveys_options")

    def get_procentage_of_choosing(self):
        total_submition = len(self.question.survey.get_users_that_completed())
        users = len(self.users.all())

        if not total_submition:
            return 0
        
        return round(users / total_submition * 100, 1)
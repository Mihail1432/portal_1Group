from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Vote(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    question = models.CharField(max_length=150)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_users_that_completed(self):
        user_set = set(
            user
            for option in self.options.all()
            for user in option.users.all()
        )
        return list(user_set)

    def save_submission(self, request):
        option = self.options.get(id=request.POST.get(str(self.id)))
        option.users.add(request.user)


    class Meta:
        ordering = ["-created_at"]

class Option(models.Model):
    value = models.CharField(max_length=150)
    vote = models.ForeignKey(Vote, on_delete=models.Case, related_name="options")

    users = models.ManyToManyField(get_user_model(), blank=True, related_name="chosen_vote_options")

    def get_procentage_of_choosing(self):
        total_submition = len(self.vote.get_users_that_completed())
        users = len(self.users.all())

        if not total_submition:
            return 0
        
        return round(users / total_submition * 100, 1)
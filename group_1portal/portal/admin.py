from django.contrib import admin
from .models import Role, UserProfile, Grade, Event, Survey, SurveyQuestion, SurveyAnswer, \
    SurveyResponse, Vote, VoteOption, VoteResult, Announcement, Material, Portfolio, GalleryItem, MyModel
from django.contrib.auth import get_user_model
User = get_user_model()


# Реєстрація моделей
admin.site.register(User)
admin.site.register(Role)
admin.site.register(UserProfile)
admin.site.register(Grade)
admin.site.register(Event)
admin.site.register(Survey)
admin.site.register(SurveyQuestion)
admin.site.register(SurveyAnswer)
admin.site.register(SurveyResponse)
admin.site.register(Vote)
admin.site.register(VoteOption)
admin.site.register(VoteResult)
admin.site.register(Announcement)
admin.site.register(Material)
admin.site.register(Portfolio)
admin.site.register(GalleryItem)
admin.site.register(MyModel)

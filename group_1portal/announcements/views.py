from django.views.generic import ListView
from announcements.models import Announcement

class AnnouncementsHomeView(ListView):
    model = Announcement
    context_object_name = "announcements"
    template_name = "announcements/home.html"
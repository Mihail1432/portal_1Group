from django.views.generic import ArchiveIndexView, DetailView
from events.models import Event

class EventHomeView(ArchiveIndexView):
    model = Event
    allow_empty = True
    allow_future = True
    date_field = "date"
    context_object_name = "events"
    template_name = "events/home.html"

class EventDetailView(DetailView):
    model = Event
    context_object_name = "event"
    template_name = "events/event_detail.html"

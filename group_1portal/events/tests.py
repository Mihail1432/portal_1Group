from django.test import TestCase
from .models import Event

class EventTests(TestCase):
    def test_create_event(self):
        event = Event.objects.create(title='Test Event', description='Test Description', date='2024-01-01')
        self.assertEqual(event.title, 'Test Event')


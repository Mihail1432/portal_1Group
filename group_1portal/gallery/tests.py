from django.test import TestCase
from .models import Image
from django.contrib.auth import get_user_model

User = get_user_model()

class ImageModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.image = Image.objects.create(
            title='Test Image',
            description='Test Description',
            image='test_image.jpg',
            uploaded_by=self.user
        )

    def test_image_creation(self):
        self.assertEqual(self.image.title, 'Test Image')
        self.assertEqual(self.image.description, 'Test Description')
        self.assertEqual(self.image.uploaded_by.username, 'testuser')

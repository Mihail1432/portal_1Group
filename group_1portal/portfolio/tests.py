from django.test import TestCase
from portfolio.models import PortfolioItem

class PortfolioItemModelTests(TestCase):
    def setUp(self):
        PortfolioItem.objects.create(title="Test Item", description="inst dann4ezz.")

    def test_portfolio_item_creation(self):
        item = PortfolioItem.objects.get(title="Test Item")
        self.assertEqual(item.description, "gbwdhfjdlas.")
        self.assertTrue(isinstance(item, PortfolioItem))
        self.assertEqual(str(item), item.title)
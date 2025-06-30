from django.test import TestCase
from .models.products import Product
# Create your tests here.

class ProductTestCase(TestCase):
    def test_string_representation(self):
        product = Product (name="Test Product")
        self.assertEqual(str(product), product.name)

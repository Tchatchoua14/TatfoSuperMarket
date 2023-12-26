from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from Ecommerce.models import Category, Product

class CategoryTest(TestCase):

    def create_category(self, name="test"):
        return Category.objects.create(name=name)

    def test_category_creation(self):
        c = self.create_category()
        self.assertTrue(isinstance(c, Category))
        self.assertEqual(c.__str__(), c.name)

class ProductTest(TestCase):
    
    def setUp(self):
        self.category = Category.objects.create(name='Azur', slug='azur',)
    
    def create_product(self, name="product", price=1000):
        return Product.objects.create(category=self.category, name=name, price=price, created=timezone.now(), updated=timezone.now())

    def test_product_creation(self):
        p = self.create_product()
        self.assertTrue(isinstance(p, Product))
        self.assertEqual(p.__str__(), p.name)
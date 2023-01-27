from django.test import TestCase
from product.models import Product
from product.models import Category


# Create your tests here.
class CategoryTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='test', slug='test')
    def test_category(self):
        category = Category.objects.get(name='test')
        self.assertEqual(category.name, 'test')
        self.assertEqual(category.slug, 'test')

class ProductTestCase(TestCase):
    def setUp(self):
        category1 = Category.objects.create(name='test', slug='test')
        Product.objects.create(category=category1, name='test', slug='test', price=100)
        Product.objects.create(category=category1, name='test2', slug='test2', price=200)
    def test_product_create(self):
        product1 = Product.objects.get(name='test')
        product2 = Product.objects.get(name='test2')
        self.assertEqual(product1.price, 100)
        self.assertEqual(product2.price, 200)

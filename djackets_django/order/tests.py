from django.test import TestCase
from order.models import Order
from order.models import OrderItem
from django.contrib.auth.models import User
from product.models import Product

class OrderTestCase(TestCase):
    def setUp(self):
        user1 = User.objects.create(username='test', password='test')
        Order.objects.create(user=user1, first_name='test', last_name='test')

    def test_order_create(self):
        order = Order.objects.get(first_name='test')
        self.assertEqual(order.first_name, 'test')
        self.assertEqual(order.last_name, 'test')

Í

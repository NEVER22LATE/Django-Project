from django.test import testcases, client, TestCase
from django.urls import resolve, reverse
from orders.views import order_create
from orders.models import Order, OrderItem
from shop.models import Product, Category
import datetime

class TestUrls(TestCase):
    def setUp(self):
        Category.objects.create(id = 1, name = 'jeans', slug = 'aa', created_at = '2012-07-23', updated_at = '2012-07-24')
        Product.objects.create(id = 1, name = 'shoes', slug = 'aa', category_id = 1,  description = 'Red color', price = 1000, available = 1, stock = 10, created_at = '2012-07-23', updated_at = '2012-07-24', image = 'https://image.shutterstock.com/image-illustration/illustration-international-passengers-infrared-thermal-260nw-1640970700.jpg')
        Order.objects.create(id = 1, first_name = "rahul", last_name ='kumar', 
        email = 'rahul@gmail.com', city ='bangalore', street ='20', house_number = '30', 
        apartment_number = '200', postal_code = '565454', created = '2012-01-03', updated = '2013-02-03', paid = 1)
        OrderItem.objects.create(id = 1, price = 1000, quantity = 1, order_id = 1, product_id = 1)

    def test_order_create_urls(self):
        # print(Product.objects.get(id = 1))
        # print(reverse('cart:cart_add', args=[1]))
        # print(Category.objects.all())
        response = self.client.post(reverse('orders:order_create'))  #pass product id
        print(reverse('orders:order_create'))

        self.assertEqual(response.status_code, 302)

    


    
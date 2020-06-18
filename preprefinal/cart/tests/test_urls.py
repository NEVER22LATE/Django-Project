from django.test import testcases, client, TestCase
from django.urls import resolve, reverse
from cart.views import cart_add, cart_remove, cart_detail
from shop.models import Product, Category
import datetime

class TestUrls(TestCase):
    def setUp(self):
        Category.objects.create(id = 1, name = 'jeans', slug = 'aa', created_at = '2012-07-23', updated_at = '2012-07-24')
        Category.objects.create(id = 2, name = 'shirt', slug = 'bb', created_at = '2012-07-20', updated_at = '2012-07-24')
        Product.objects.create(id = 1, name = 'shoes', slug = 'aa', category_id = 1,  description = 'Red color', price = 1000, available = 1, stock = 10, created_at = '2012-07-23', updated_at = '2012-07-24', image = 'https://image.shutterstock.com/image-illustration/illustration-international-passengers-infrared-thermal-260nw-1640970700.jpg')
        Product.objects.create(id = 2, name = 'cloth', slug = 'bb', category_id = 2, description = 'Red color', price = 12000, available = 1, stock = 5, created_at = '2012-07-23', updated_at = '2012-07-24', image = 'https://image.shutterstock.com/image-illustration/illustration-international-passengers-infrared-thermal-260nw-1640970700.jpg')
        Product.objects.create(id = 3, name = 'watch', slug = 'aa', category_id = 2, description = 'Red color', price = 123000, available = 1, stock = 10, created_at = '2012-07-23', updated_at = '2012-07-24', image = 'https://image.shutterstock.com/image-illustration/illustration-international-passengers-infrared-thermal-260nw-1640970700.jpg')


    def test_cart_add_urls(self):
        # print(Product.objects.get(id = 1))
        # print(reverse('cart:cart_add', args=[1]))
        # print(Category.objects.all())
        response = self.client.post(reverse('cart:cart_add', args=[1]))  #pass product id
        #print(resolve(response))

        self.assertEqual(response.status_code, 302)

    def test_cart_detail_urls(self):
        # print(reverse('cart:cart_detail'))
        response = self.client.post(reverse('cart:cart_detail'))  #pass product id
        #print(resolve(response))
        self.assertEqual(response.status_code, 200)

    def test_cart_remove_urls(self):
        response = self.client.post(reverse('cart:cart_remove', args=[2]))  #pass product id
        #print(resolve(response))
        self.assertEqual(response.status_code, 302)



    
from Ecommerce.views import *
from django.test import SimpleTestCase
from django.urls import reverse, resolve

class TestUrls(SimpleTestCase):

    def test_checkout_url(self):
        url = reverse('Ecommerce:checkout')
        self.assertEquals(resolve(url).func, checkout)


    # def test_list_by_category_url(self):
    #     url = reverse('shop:product_list_by_category', args=['any-slug'])
    #     self.assertEquals(resolve(url).func, product_list)


    def test_detail_url(self):
        url = reverse('Ecommerce:product_detail', kwargs={'id': 1, 'slug': 'any-slug'})
        self.assertEquals(resolve(url).func, product_detail)

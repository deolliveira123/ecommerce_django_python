# coding=utf-8

from django.test import TestCase,  Client
from django.app.urlresolvers import reverse

class IndexViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_status_code(self):
        client = Client()
        response = client.get('/')
        self.assertEquals(response.satus_code, 200)
    def test_template_used(self):
        client = Client()
        response = client.get('/')
        self.assertEquals(response, 'Index.html')

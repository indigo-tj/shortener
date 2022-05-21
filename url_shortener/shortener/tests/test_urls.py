from http import HTTPStatus

from django.test import Client, TestCase


class URLTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_index_url_works(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, HTTPStatus.OK)
    
    def test_index_url_has_correct_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "shortener/index.html")

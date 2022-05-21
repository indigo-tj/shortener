from http import HTTPStatus

from django.test import Client, TestCase
from django.urls import reverse

from ..models import Url


class UrlsFormTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.url_to_shorten = "http://yandex.ru"
        
    def test_client_can_short_url(self):
        response = self.client.post(
            reverse("shortener:index"),
            data={
                'http_url': self.url_to_shorten
            },
            follow=True
        )

        self.assertEqual(response.status_code, HTTPStatus.OK)
        url = Url.objects.first()
        self.assertEqual(url.http_url, self.url_to_shorten)

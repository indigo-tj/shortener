from http import HTTPStatus

from django.test import Client, TestCase
from django.urls import reverse

from ..models import Url
from ..utils import get_short_id


class TestUrlsViews(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.url_to_shorten = "http://yandex.ru"
        cls.shorted_url = get_short_id()
        cls.url = Url.objects.create(
            http_url=cls.url_to_shorten,
            short_id=cls.shorted_url
        )

    def setUp(self) -> None:
        self.client = Client()

    def test_correct_template_used_for_index_reverse(self):
        response = self.client.get(reverse("shortener:index"))   #.get(/unknown_page)  DEBUG=False
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "shortener/index.html")

    def test_index_page_has_correct_context(self):
        response = self.client.get(reverse("shortener:index"))
        self.assertIn("form", response.context)
        self.assertNotIn("shorted_url", response.context)

    def test_short_url_do_redirect(self):
        response = self.client.get(reverse("shortener:redirect_to", args=[self.shorted_url]))
        self.assertEqual(self.url_to_shorten, response.headers["Location"])

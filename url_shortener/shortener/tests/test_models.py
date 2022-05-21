from django.test import TestCase

from ..models import Url
from ..utils import get_short_id


class UrlsModelTest(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.url_to_shorten = "http://yandex.ru"
        cls.url = Url.objects.create(
            http_url=cls.url_to_shorten,
            short_id=get_short_id()
        )

    def test_verbose_name(self):
        field_verboses = {
            "http_url": "Сокращаемая ссылка"
        }

        for value, expected in field_verboses.items():
            with self.subTest(value=value):
                self.assertEqual(self.url._meta.get_field(value).verbose_name, expected)
    
    def test_url_model_has_str_overload(self):
        self.assertEqual(str(self.url), self.url_to_shorten)

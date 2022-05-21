from statistics import mode
from django.db import models


class Url(models.Model):
    short_id = models.SlugField(unique=True)  # 'asde34sad'
    http_url = models.URLField(max_length=255, verbose_name="Сокращаемая ссылка")
    pub_date = models.DateTimeField(auto_now_add=True)
    nums_of_visits = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.http_url}"

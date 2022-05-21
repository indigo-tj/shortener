from hashlib import sha1
from random import choice
from string import ascii_lowercase

from django.conf import settings


def get_short_id():
    code = "".join(
        [choice(ascii_lowercase) for _ in range(settings.SHORT_URL_LENGTH)]
    )
    return sha1(code.encode()).hexdigest()[:settings.SHORT_URL_LENGTH]

    


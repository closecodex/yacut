import random
import string

from .models import URLMap

DEFAULT_SHORT_ID_LENGTH = 6


def get_unique_short_id(length=DEFAULT_SHORT_ID_LENGTH):
    while True:
        short_id = ''.join(
            random.choices(
                string.ascii_letters + string.digits, k=length
            )
        )
        if not URLMap.query.filter_by(short=short_id).first():
            return short_id

from datetime import (
    datetime,
    timezone,
    timedelta
)
from django.utils import timezone as tz
import pytz

from .models import (
    mUser,
    Blog,
    Category,
    Tag,
    Post,
    Comment,
)


def utc_to_jst(timestamp_utc):
    datetime_jst = timestamp_utc.astimezone(timezone(timedelta(hours=+9)))
    timestamp_jst = datetime.strftime(datetime_jst, '%Y-%m-%d %H:%M:%S')
    return timestamp_jst

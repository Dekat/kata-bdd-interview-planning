import re
from datetime import time

REGEX_HOUR = re.compile(r'at ([0-2][0-9]):([0-9]{2})')


def string_period_to_periods_list(str_period: str) -> list[tuple[time, time]]:
    if str_period == 'all day':
        return [(time(0, 0), time(23, 59))]

    hour_match = REGEX_HOUR.match(str_period)
    if hour_match:
        hour = int(hour_match.group(1))
        minute = int(hour_match.group(2))
        return [(time(hour, minute), time(hour + 1, minute))]

    periods: list[tuple[time, time]] = []
    return periods

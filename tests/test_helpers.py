from datetime import time

from tests.helpers import string_period_to_periods_list


class TestStringPeriodToPeriodsList:

    def test_with_just_one_hour(self):
        # Given
        str_period = "at 14:00"

        # When
        periods = string_period_to_periods_list(str_period)

        # Then
        assert len(periods) == 1
        assert periods[0] == (time(14, 0), time(15, 0))

    def test_with_all_day(self):
        # Given
        str_period = "all day"

        # When
        periods = string_period_to_periods_list(str_period)

        # Then
        assert len(periods) == 1
        assert periods[0] == (time(0, 0), time(23, 59))

    def test_with_not_available_today(self):
        # Given
        str_period = "not available today"

        # When
        periods = string_period_to_periods_list(str_period)

        # Then
        assert len(periods) == 0

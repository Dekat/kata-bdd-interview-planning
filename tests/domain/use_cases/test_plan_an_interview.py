from datetime import time

from domain.use_cases import PlanAnInterview


class TestArePeriodsCompatible:

    def test_same_hour(self):
        # Given
        recruiter_periods = [(time(14, 0), time(15, 0))]
        candidate_periods = [(time(14, 0), time(15, 0))]

        # When
        result = PlanAnInterview.are_periods_compatible(
            recruiter_periods, candidate_periods
        )

        # Then
        assert result is True

    def test_no_hour_for_candidate(self):
        # Given
        recruiter_periods = [(time(14, 0), time(15, 0))]
        candidate_periods = []

        # When
        result = PlanAnInterview.are_periods_compatible(
            recruiter_periods, candidate_periods
        )

        # Then
        assert result is False

    def test_no_hour_for_recruiter(self):
        # Given
        recruiter_periods = []
        candidate_periods = [(time(14, 0), time(15, 0))]

        # When
        result = PlanAnInterview.are_periods_compatible(
            recruiter_periods, candidate_periods
        )

        # Then
        assert result is False

    def test_included_hour_from_recruiter_to_candidate(self):
        # Given
        recruiter_periods = [(time(14, 0), time(15, 0))]
        candidate_periods = [(time(0, 0), time(23, 59))]

        # When
        result = PlanAnInterview.are_periods_compatible(
            recruiter_periods, candidate_periods
        )

        # Then
        assert result is True


from datetime import time

from domain.entities.candidate import Candidate
from domain.entities.recruiter import Recruiter


class CandidateMapper:

    def __init__(self, candidate_json: dict):
        self.candidate_json = candidate_json

    def map(self) -> Candidate:
        return Candidate(
            self.candidate_json['known_language'],
            self.candidate_json['email_address'],
            self.candidate_json['nb_years_of_xp'],
            [
                PeriodMapper(p).map() for p in self.candidate_json['available_periods']
            ],
        )


class CandidateJsonMapper:

    def __init__(self, candidate: Candidate):
        self.candidate = candidate

    def map(self) -> dict:
        return {
            'known_language': self.candidate.known_language,
            'email_address': self.candidate.email_address,
            'nb_years_of_xp': self.candidate.nb_years_of_xp,
            'available_periods': [
                PeriodJsonMapper(p).map() for p in self.candidate.available_periods
            ],
        }


class RecruiterMapper:

    def __init__(self, recruiter_json: dict):
        self.recruiter_json = recruiter_json

    def map(self) -> Recruiter:
        return Recruiter(
            self.recruiter_json['known_language'],
            self.recruiter_json['email_address'],
            self.recruiter_json['nb_years_of_xp'],
            [
                PeriodMapper(p).map() for p in self.recruiter_json['available_periods']
            ],
        )


class RecruiterJsonMapper:

    def __init__(self, recruiter: Recruiter):
        self.recruiter = recruiter

    def map(self) -> dict:
        return {
            'known_language': self.recruiter.known_language,
            'email_address': self.recruiter.email_address,
            'nb_years_of_xp': self.recruiter.nb_years_of_xp,
            'available_periods': [
                PeriodJsonMapper(p).map() for p in self.recruiter.available_periods
            ],
        }


class PeriodMapper:
    def __init__(self, period_json: str):
        # (14:00, 15:00)
        self.period_json = period_json

    def map(self) -> tuple[time, time]:
        start, end = self.period_json[1:-1].split(',')
        start_hour, start_minutes = start.strip().split(':')
        end_hour, end_minutes = end.strip().split(':')
        return (
            time(int(start_hour), int(start_minutes)),
            time(int(end_hour), int(end_minutes)),
        )


class PeriodJsonMapper:
    def __init__(self, period: tuple[time, time]):
        self.period = period

    def map(self) -> str:
        return (
            f'({self.period[0].hour}:{self.period[0].minute}, '
            f'{self.period[1].hour}:{self.period[1].minute})'
        )

from datetime import time


class Recruiter:
    def __init__(
            self, known_language: str, email_address: str, nb_years_of_xp: int,
            available_periods: list[tuple[time, time]]
    ):
        self.known_language = known_language
        self.email_address = email_address
        self.nb_years_of_xp = nb_years_of_xp
        self.available_periods = available_periods

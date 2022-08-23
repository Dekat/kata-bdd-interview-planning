from datetime import time
from unittest.mock import Mock

from domain import ports
from domain.entities import exceptions
from domain.entities.candidate import Candidate
from domain.entities.interview_planning import InterviewPlanning
from domain.entities.recruiter import Recruiter


class PlanAnInterview:

    def __init__(
        self,
        interview_planning_repository: ports.InterviewPlanningRepository,
        email_service: ports.EmailService
    ):
        self.interview_planning_repository = interview_planning_repository
        self.email_service = email_service

    def execute(self, recruiter: Recruiter, candidate: Candidate):
        if recruiter.known_language != candidate.known_language:
            raise exceptions.NotTheSameLanguageError()

        if recruiter.nb_years_of_xp <= candidate.nb_years_of_xp:
            raise exceptions.LesserYearsOfXpError(
                f"Recruiter {recruiter.nb_years_of_xp} <= "
                f"Candidate {candidate.nb_years_of_xp}"
            )

        if not PlanAnInterview.are_periods_compatible(
            recruiter.available_periods, candidate.available_periods
        ):
            raise exceptions.AvailablePeriodsNotCompatibleError()

        interview_planning = InterviewPlanning(recruiter, candidate)
        self.interview_planning_repository.save_interview_planning(interview_planning)
        self.email_service.send_email(recruiter.email_address)
        self.email_service.send_email(candidate.email_address)

    @staticmethod
    def are_periods_compatible(
        recruiter_periods: list[tuple[time, time]],
        candidate_periods: list[tuple[time, time]],
    ) -> bool:
        for recruiter_period in recruiter_periods:
            for candidate_period in candidate_periods:
                if (
                    (
                        recruiter_period[0] <= candidate_period[0]
                        and recruiter_period[1] >= candidate_period[1]
                    ) or (
                        candidate_period[0] <= recruiter_period[0]
                        and candidate_period[1] >= recruiter_period[1]
                    )
                ):
                    return True
        return False

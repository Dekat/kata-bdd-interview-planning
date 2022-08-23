from domain import ports
from domain.entities.interview_planning import InterviewPlanning


class InterviewPlanningMemoryStorage(ports.InterviewPlanningRepository):

    def __init__(self):
        self._saved_interview_plannings: list[InterviewPlanning] = []

    def save_interview_planning(self, interview_planning: InterviewPlanning) -> None:
        self._saved_interview_plannings.append(interview_planning)

    def count_interviews_plannings(self) -> int:
        return len(self._saved_interview_plannings)

    def purge_all_data(self) -> None:
        self._saved_interview_plannings = []

from abc import ABC, abstractmethod

from domain.entities.interview_planning import InterviewPlanning


class InterviewPlanningRepository(ABC):

    @abstractmethod
    def save_interview_planning(self, interview_planning: InterviewPlanning) -> None:
        pass

    @abstractmethod
    def count_interviews_plannings(self) -> int:
        pass

    @abstractmethod
    def purge_all_data(self) -> None:
        pass

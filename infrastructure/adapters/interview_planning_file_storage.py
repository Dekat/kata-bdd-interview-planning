import pickle

from domain import ports
from domain.entities.interview_planning import InterviewPlanning


class InterviewPlanningFileStorage(ports.InterviewPlanningRepository):

    FILE_NAME = 'data.db'

    def __init__(self):
        self._saved_interview_plannings: list[InterviewPlanning] = []

    def save_interview_planning(self, interview_planning: InterviewPlanning) -> None:
        self._load_data_from_file()
        self._saved_interview_plannings.append(interview_planning)
        self._persist_data_in_file()

    def count_interviews_plannings(self) -> int:
        self._load_data_from_file()
        return len(self._saved_interview_plannings)

    def purge_all_data(self) -> None:
        self._saved_interview_plannings = []
        self._persist_data_in_file()

    def _load_data_from_file(self) -> None:
        try:
            with open(self.FILE_NAME, 'rb') as file:
                self._saved_interview_plannings = pickle.loads(file.read())
        except (FileNotFoundError, EOFError):
            self._saved_interview_plannings = []

    def _persist_data_in_file(self) -> None:
        with open(self.FILE_NAME, 'wb') as file:
            file.write(
                pickle.dumps(
                    self._saved_interview_plannings, protocol=pickle.HIGHEST_PROTOCOL
                )
            )

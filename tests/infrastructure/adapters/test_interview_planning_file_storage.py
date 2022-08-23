from datetime import time

from domain.entities.candidate import Candidate
from domain.entities.interview_planning import InterviewPlanning
from domain.entities.recruiter import Recruiter
from infrastructure import adapters


def test_should_save_and_retrieve_interviews_plannings():
    # Given
    interview_planning_memory_storage = adapters.InterviewPlanningFileStorage()
    interview_planning = InterviewPlanning(
        Recruiter("Python", "toto@recruiter.com", 5, [(time(14, 0), time(15, 0))]),
        Candidate("Python", "toto@candidate.com", 3, [(time(14, 0), time(15, 0))]),
    )

    # When
    interview_planning_memory_storage.save_interview_planning(interview_planning)

    # Then
    assert interview_planning_memory_storage.count_interviews_plannings() == 1

    # Restore
    interview_planning_memory_storage.purge_all_data()

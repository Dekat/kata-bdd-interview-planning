from domain.entities.candidate import Candidate
from domain.entities.recruiter import Recruiter


class InterviewPlanning:
    def __init__(self, recruiter: Recruiter, candidate: Candidate):
        self.recruiter = recruiter
        self.candidate = candidate

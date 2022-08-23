from domain import use_cases
from infrastructure import adapters


# Use cases
use_case_plan_an_interview = use_cases.PlanAnInterview(
    interview_planning_repository=adapters.InterviewPlanningFileStorage(),
    email_service=adapters.LocalhostMailService()
)

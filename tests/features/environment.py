from unittest.mock import Mock

from behave.model import Scenario
from behave.runner import Context

import registry
from domain import ports
from infrastructure.controllers.api import app


def before_all(context: Context):
    context.api_client = app.test_client()


def before_scenario(context: Context, scenario: Scenario):
    registry.use_case_plan_an_interview.email_service = Mock(spec=ports.EmailService)


def after_scenario(context: Context, scenario: Scenario):
    registry.use_case_plan_an_interview.interview_planning_repository.purge_all_data()

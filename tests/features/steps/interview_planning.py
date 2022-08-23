import behave.runner
from behave import *

import registry
from domain.entities.candidate import Candidate
from domain.entities.recruiter import Recruiter
from infrastructure.controllers.mappers.api import RecruiterJsonMapper, \
    CandidateJsonMapper
from tests.helpers import string_period_to_periods_list

use_step_matcher("re")


@given(
    r'a (?P<known_language>.+?) recruiter \((?P<email_address>.+?)\) with '
    r'(?P<nb_years_of_xp>.+?) years? of experience '
    r'(?:and available|but is) (?P<available_period>.+?)')
def step_impl(
    context: behave.runner.Context, known_language: str, email_address: str,
    nb_years_of_xp: int, available_period: str
):
    context.recruiter = Recruiter(
        known_language, email_address, nb_years_of_xp,
        string_period_to_periods_list(available_period)
    )


@given(
    r'a (?P<known_language>.+?) candidate \((?P<email_address>.+?)\) with '
    r'(?P<nb_years_of_xp>.+?) years? of experience '
    r'(?:and available|but is) (?P<available_period>.+?)')
def step_impl(
    context: behave.runner.Context, known_language: str, email_address: str,
    nb_years_of_xp: int, available_period: str
):
    context.candidate = Candidate(
        known_language, email_address, nb_years_of_xp,
        string_period_to_periods_list(available_period)
    )


@when("we want to plan an interview")
def step_impl(context: behave.runner.Context):
    context.api_client.post('/interview-planning', json={
        'recruiter': RecruiterJsonMapper(context.recruiter).map(),
        'candidate': CandidateJsonMapper(context.candidate).map(),
    })


@then("the planning should be saved")
def step_impl(context: behave.runner.Context):
    assert registry.use_case_plan_an_interview.interview_planning_repository.count_interviews_plannings() == 1


@step("the planning should not be saved")
def step_impl(context: behave.runner.Context):
    assert registry.use_case_plan_an_interview.interview_planning_repository.count_interviews_plannings() == 0


@step("an e-mail is sent to the candidate with address (?P<email_address>.+?)")
def step_impl(context: behave.runner.Context, email_address: str):
    registry.use_case_plan_an_interview.email_service.send_email.assert_any_call(
        email_address
    )


@step("no e-mail sent")
def step_impl(context: behave.runner.Context):
    registry.use_case_plan_an_interview.email_service.send_email.assert_not_called()

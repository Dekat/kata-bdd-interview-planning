from flask import request

import registry
from infrastructure.controllers import mappers
from infrastructure.controllers.api_helpers import create_app


app = create_app()


@app.post("/interview-planning")
def plan_interview():
    json_body = request.json

    registry.use_case_plan_an_interview.execute(
        mappers.RecruiterMapper(json_body['recruiter']).map(),
        mappers.CandidateMapper(json_body['candidate']).map(),
    )

    return {}, 200

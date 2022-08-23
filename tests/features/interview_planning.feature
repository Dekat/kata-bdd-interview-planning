Feature: Planning of an interview between a candidate and a recruiter

  Scenario: Everything is compatible
    Given a Python recruiter (jean@recruiter.com) with 5 years of experience and available at 14:00
    And a Python candidate (francois@candidate.com) with 2 years of experience and available at 14:00
    When we want to plan an interview
    Then the planning should be saved
    And an e-mail is sent to the candidate with address jean@recruiter.com
    And an e-mail is sent to the candidate with address francois@candidate.com

  Scenario: Recruiter is available all day
    Given a Python recruiter (jean@recruiter.com) with 5 years of experience and available all day
    And a Python candidate (francois@candidate.com) with 2 years of experience and available at 14:00
    When we want to plan an interview
    Then the planning should be saved
    And an e-mail is sent to the candidate with address jean@recruiter.com
    And an e-mail is sent to the candidate with address francois@candidate.com

  Scenario: Candidate and recruiter have a different known language
    Given a Javascript recruiter (jean@recruiter.com) with 5 years of experience and available at 14:00
    And a Python candidate (francois@candidate.com) with 2 years of experience and available at 14:00
    When we want to plan an interview
    Then the planning should not be saved
    And no e-mail sent

  Scenario: Recruiter as a lower experience than the candidate
    Given a Python recruiter (jean@recruiter.com) with 1 year of experience and available at 14:00
    And a Python candidate (francois@candidate.com) with 2 years of experience and available at 14:00
    When we want to plan an interview
    Then the planning should not be saved
    And no e-mail sent

  Scenario: Recruiter and candidate have the same experience
    Given a Python recruiter (jean@recruiter.com) with 2 years of experience and available at 14:00
    And a Python candidate (francois@candidate.com) with 2 years of experience and available at 14:00
    When we want to plan an interview
    Then the planning should not be saved
    And no e-mail sent

  Scenario: Recruiter and candidate are not available at same hour
    Given a Python recruiter (jean@recruiter.com) with 5 years of experience and available at 15:00
    And a Python candidate (francois@candidate.com) with 2 years of experience and available at 14:00
    When we want to plan an interview
    Then the planning should not be saved
    And no e-mail sent

  Scenario: Recruiter is not available today
    Given a Python recruiter (jean@recruiter.com) with 5 years of experience but is not available today
    And a Python candidate (francois@candidate.com) with 2 years of experience and available at 14:00
    When we want to plan an interview
    Then the planning should not be saved
    And no e-mail sent

  Scenario: Recruiter is not available today but candidate is available all day
    Given a Python recruiter (jean@recruiter.com) with 5 years of experience but is not available today
    And a Python candidate (francois@candidate.com) with 2 years of experience and available all day
    When we want to plan an interview
    Then the planning should not be saved
    And no e-mail sent

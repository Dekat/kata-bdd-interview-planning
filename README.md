# Kata on Behavior-Driven Development
## Subject

As an HR, I want to plan an interview between a candidate and a recruiter.
To do this, it's necessary that:
- the recruiter have more experience than the candidate
- the two people knows the same technology
- they are available at the same time

If these conditions are met, the interview is saved in the application and 2 e-mails
are sent to the recruiter and the candidate.
Else, the interview is not saved and no e-mail is sent.

## Solution

I used an **hexagonal architecture** to separate layers and be able to easily test each 
part.

I used the library **[behave](https://pypi.org/project/behave/)** to read 
**Gherkin** files.

## Usage

Just create a virtual environment with the tool you prefer and install the requirements:
`pip install -r requirements.txt`

Then, you can run the unit tests: `pytest`

And the Gherkin tests: `behave`

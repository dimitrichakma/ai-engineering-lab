from typing import Literal

from pydantic import BaseModel, Field, model_validator


class Salary(BaseModel):
    min_bdt: int | None = Field(default=None, description="The minimum salary of a bangladeshi job in BDT amount, null means the minimum salary is not specified")
    max_bdt: int | None = Field(default=None, description="The maximum salary of a bangladeshi job in BDT amount, null means the maximum salary is not specified")
    period: Literal["month", "year"] | None = Field(default=None, description="The pay period time. null means the pay period is not specified")
    @model_validator(mode="after")
    def check_min_max(self):
        if self.min_bdt is not None and self.max_bdt is not None:
            if self.min_bdt > self.max_bdt:
                raise ValueError("min_bdt cannot be greater than max_bdt")
        return self
   
    

class Requirement(BaseModel):
    skill: str  = Field(description="The skill required to get a job")
    required: bool = Field(default=True, description="Indicates if the skill is required or just nice to have, true means required, false means nice to have")
    



class JobPost(BaseModel):

    title: str = Field(description="The title of the job post from job description")
    company: str = Field(description="The company name of the job post from job description")
    location: str | None = Field(default=None, description="The location it is based in either a city or country name, null means the location is not specified")
    work_mode: list[Literal["onsite", "hybrid", "remote"]] = Field(default_factory=list, description="on site means the job is done in the office, hybrid means the job is done both in the office and remotely, remote means the job is done remotely")
    description: str | None 
    min_experience_years: float | None = Field(default=None, description="The minimum experience required for the job post in years, null means the minimum experience is not specified")
    requirements: list[Requirement] = Field(description="The list of requirements for the job post, each requirement is a skill and whether it is required or nice to have")
    salary: Salary | None = Field(default=None, description="The salary of the job post, including min_bdt, max_bdt, and period, null means the salary is not specified")
    deadline_text: str | None = Field(default=None, description="The deadline of the job post for applying in text format, null means the deadline is not specified")
    

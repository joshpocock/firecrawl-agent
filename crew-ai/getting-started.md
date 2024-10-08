Installing crewAI¶

Welcome to crewAI! This guide will walk you through the installation process for crewAI and its dependencies. crewAI is a flexible and powerful AI framework that enables you to create and manage AI agents, tools, and tasks efficiently. Let's get started!
Installation¶

To install crewAI, you need to have Python >=3.10 and <=3.13 installed on your system:

# Install the main crewAI package
pip install crewai

# Install the main crewAI package and the tools package
# that includes a series of helpful tools for your agents
pip install 'crewai[tools]'

# Alternatively, you can also use:
pip install crewai crewai-tools

Starting Your CrewAI Project¶

Welcome to the ultimate guide for starting a new CrewAI project. This document will walk you through the steps to create, customize, and run your CrewAI project, ensuring you have everything you need to get started.

Before we start, there are a couple of things to note:

    CrewAI is a Python package and requires Python >=3.10 and <=3.13 to run.
    The preferred way of setting up CrewAI is using the crewai create crew command. This will create a new project folder and install a skeleton template for you to work on.

Prerequisites¶

Before getting started with CrewAI, make sure that you have installed it via pip:

$ pip install 'crewai[tools]'

Creating a New Project¶

In this example, we will be using poetry as our virtual environment manager.

To create a new CrewAI project, run the following CLI command:

$ crewai create crew <project_name>

This command will create a new project folder with the following structure:

my_project/
├── .gitignore
├── pyproject.toml
├── README.md
└── src/
    └── my_project/
        ├── __init__.py
        ├── main.py
        ├── crew.py
        ├── tools/
        │   ├── custom_tool.py
        │   └── __init__.py
        └── config/
            ├── agents.yaml
            └── tasks.yaml

You can now start developing your project by editing the files in the src/my_project folder. The main.py file is the entry point of your project, and the crew.py file is where you define your agents and tasks.
Customizing Your Project¶

To customize your project, you can: - Modify src/my_project/config/agents.yaml to define your agents. - Modify src/my_project/config/tasks.yaml to define your tasks. - Modify src/my_project/crew.py to add your own logic, tools, and specific arguments. - Modify src/my_project/main.py to add custom inputs for your agents and tasks. - Add your environment variables into the .env file.
Example: Defining Agents and Tasks¶
agents.yaml¶

researcher:
  role: >
    Job Candidate Researcher
  goal: >
    Find potential candidates for the job
  backstory: >
    You are adept at finding the right candidates by exploring various online
    resources. Your skill in identifying suitable candidates ensures the best
    match for job positions.

tasks.yaml¶

research_candidates_task:
  description: >
    Conduct thorough research to find potential candidates for the specified job.
    Utilize various online resources and databases to gather a comprehensive list of potential candidates.
    Ensure that the candidates meet the job requirements provided.

    Job Requirements:
    {job_requirements}
  expected_output: >
    A list of 10 potential candidates with their contact information and brief profiles highlighting their suitability.
  agent: researcher # THIS NEEDS TO MATCH THE AGENT NAME IN THE AGENTS.YAML FILE AND THE AGENT DEFINED IN THE crew.py FILE
  context: # THESE NEED TO MATCH THE TASK NAMES DEFINED ABOVE AND THE TASKS.YAML FILE AND THE TASK DEFINED IN THE crew.py FILE
    - researcher

Referencing Variables:¶

Your defined functions with the same name will be used. For example, you can reference the agent for specific tasks from tasks.yaml file. Ensure your annotated agent and function name are the same; otherwise, your task won't recognize the reference properly.
Example References¶

agents.yaml

email_summarizer:
    role: >
      Email Summarizer
    goal: >
      Summarize emails into a concise and clear summary
    backstory: >
      You will create a 5 bullet point summary of the report
    llm: mixtal_llm

tasks.yaml

email_summarizer_task:
    description: >
      Summarize the email into a 5 bullet point summary
    expected_output: >
      A 5 bullet point summary of the email
    agent: email_summarizer
    context:
      - reporting_task
      - research_task

Use the annotations to properly reference the agent and task in the crew.py file.
Annotations include:¶

    @agent
    @task
    @crew
    @tool
    @callback
    @output_json
    @output_pydantic
    @cache_handler

crew.py

# ...
@agent
def email_summarizer(self) -> Agent:
    return Agent(
        config=self.agents_config["email_summarizer"],
    )

@task
def email_summarizer_task(self) -> Task:
    return Task(
        config=self.tasks_config["email_summarizer_task"],
    )
# ...

Installing Dependencies¶

To install the dependencies for your project, you can use Poetry. First, navigate to your project directory:

$ cd my_project
$ crewai install

This will install the dependencies specified in the pyproject.toml file.
Interpolating Variables¶

Any variable interpolated in your agents.yaml and tasks.yaml files like {variable} will be replaced by the value of the variable in the main.py file.
tasks.yaml¶

research_task:
  description: >
    Conduct a thorough research about the customer and competitors in the context
    of {customer_domain}.
    Make sure you find any interesting and relevant information given the
    current year is 2024.
  expected_output: >
    A complete report on the customer and their customers and competitors,
    including their demographics, preferences, market positioning and audience engagement.

main.py¶

# main.py
def run():
    inputs = {
        "customer_domain": "crewai.com"
    }
    MyProjectCrew(inputs).crew().kickoff(inputs=inputs)

Running Your Project¶

To run your project, use the following command:

$ crewai run

This will initialize your crew of AI agents and begin task execution as defined in your configuration in the main.py file.
Replay Tasks from Latest Crew Kickoff¶

CrewAI now includes a replay feature that allows you to list the tasks from the last run and replay from a specific one. To use this feature, run:

$ crewai replay <task_id>

Replace <task_id> with the ID of the task you want to replay.
Reset Crew Memory¶

If you need to reset the memory of your crew before running it again, you can do so by calling the reset memory feature:

$ crewai reset-memory

This will clear the crew's memory, allowing for a fresh start.
Deploying Your Project¶

The easiest way to deploy your crew is through CrewAI+, where you can deploy your crew in a few clicks.

Creating a CrewAI Pipeline Project¶

Welcome to the comprehensive guide for creating a new CrewAI pipeline project. This document will walk you through the steps to create, customize, and run your CrewAI pipeline project, ensuring you have everything you need to get started.

To learn more about CrewAI pipelines, visit the CrewAI documentation.
Prerequisites¶

Before getting started with CrewAI pipelines, make sure that you have installed CrewAI via pip:

$ pip install crewai crewai-tools

The same prerequisites for virtual environments and Code IDEs apply as in regular CrewAI projects.
Creating a New Pipeline Project¶

To create a new CrewAI pipeline project, you have two options:

    For a basic pipeline template:

$ crewai create pipeline <project_name>

    For a pipeline example that includes a router:

$ crewai create pipeline --router <project_name>

These commands will create a new project folder with the following structure:

<project_name>/
├── README.md
├── poetry.lock
├── pyproject.toml
├── src/
│   └── <project_name>/
│       ├── __init__.py
│       ├── main.py
│       ├── crews/
│       │   ├── crew1/
│       │   │   ├── crew1.py
│       │   │   └── config/
│       │   │       ├── agents.yaml
│       │   │       └── tasks.yaml
│       │   ├── crew2/
│       │   │   ├── crew2.py
│       │   │   └── config/
│       │   │       ├── agents.yaml
│       │   │       └── tasks.yaml
│       ├── pipelines/
│       │   ├── __init__.py
│       │   ├── pipeline1.py
│       │   └── pipeline2.py
│       └── tools/
│           ├── __init__.py
│           └── custom_tool.py
└── tests/

Customizing Your Pipeline Project¶

To customize your pipeline project, you can:

    Modify the crew files in src/<project_name>/crews/ to define your agents and tasks for each crew.
    Modify the pipeline files in src/<project_name>/pipelines/ to define your pipeline structure.
    Modify src/<project_name>/main.py to set up and run your pipelines.
    Add your environment variables into the .env file.

Example 1: Defining a Two-Stage Sequential Pipeline¶

Here's an example of how to define a pipeline with sequential stages in src/<project_name>/pipelines/pipeline.py:

from crewai import Pipeline
from crewai.project import PipelineBase
from ..crews.research_crew.research_crew import ResearchCrew
from ..crews.write_x_crew.write_x_crew import WriteXCrew

@PipelineBase
class SequentialPipeline:
    def __init__(self):
        # Initialize crews
        self.research_crew = ResearchCrew().crew()
        self.write_x_crew = WriteXCrew().crew()

    def create_pipeline(self):
        return Pipeline(
            stages=[
                self.research_crew,
                self.write_x_crew
            ]
        )

    async def kickoff(self, inputs):
        pipeline = self.create_pipeline()
        results = await pipeline.kickoff(inputs)
        return results

Example 2: Defining a Two-Stage Pipeline with Parallel Execution¶

from crewai import Pipeline
from crewai.project import PipelineBase
from ..crews.research_crew.research_crew import ResearchCrew
from ..crews.write_x_crew.write_x_crew import WriteXCrew
from ..crews.write_linkedin_crew.write_linkedin_crew import WriteLinkedInCrew

@PipelineBase
class ParallelExecutionPipeline:
    def __init__(self):
        # Initialize crews
        self.research_crew = ResearchCrew().crew()
        self.write_x_crew = WriteXCrew().crew()
        self.write_linkedin_crew = WriteLinkedInCrew().crew()

    def create_pipeline(self):
        return Pipeline(
            stages=[
                self.research_crew,
                [self.write_x_crew, self.write_linkedin_crew]  # Parallel execution
            ]
        )

    async def kickoff(self, inputs):
        pipeline = self.create_pipeline()
        results = await pipeline.kickoff(inputs)
        return results

Annotations¶

The main annotation you'll use for pipelines is @PipelineBase. This annotation is used to decorate your pipeline classes, similar to how @CrewBase is used for crews.
Installing Dependencies¶

To install the dependencies for your project, use Poetry:

$ cd <project_name>
$ crewai install

Running Your Pipeline Project¶

To run your pipeline project, use the following command:

$ crewai run

This will initialize your pipeline and begin task execution as defined in your main.py file.
Deploying Your Pipeline Project¶

Pipelines can be deployed in the same way as regular CrewAI projects. The easiest way is through CrewAI+, where you can deploy your pipeline in a few clicks.

Remember, when working with pipelines, you're orchestrating multiple crews to work together in a sequence or parallel fashion. This allows for more complex workflows and information processing tasks.
# src/first_crew/crew.py

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

from crewai_tools import SerperDevTool

# Tool for web search
searching_tool = SerperDevTool()

@CrewBase
class FirstCrew():
    """Analytical Coding Agent Crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # --- Agents ---
    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],  # defined in agents.yaml
            verbose=True,
            tools=[searching_tool]
        )

    @agent
    def summarizer(self) -> Agent:
        return Agent(
            config=self.agents_config['summarizer'],  # defined in agents.yaml
            verbose=True
        )

    @agent
    def validator(self) -> Agent:
        return Agent(
            config=self.agents_config['validator'],  # defined in agents.yaml
            verbose=True
        )

    # --- Tasks ---
    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],  # defined in tasks.yaml
            agent=self.researcher(),  # 🔑 bind researcher agent
        )

    @task
    def summarization_task(self) -> Task:
        return Task(
            config=self.tasks_config['summarization_task'],  # defined in tasks.yaml
            agent=self.summarizer(),  # 🔑 bind summarizer agent
        )

    @task
    def validation_task(self) -> Task:
        return Task(
            config=self.tasks_config['validation_task'],  # defined in tasks.yaml
            agent=self.validator(),  # 🔑 bind validator agent
            output_file="final_report.md"
        )

    # --- Crew ---
    @crew
    def crew(self) -> Crew:
        """Creates the Analytical Coding Crew"""
        return Crew(
            agents=self.agents,   # auto-created by @agent
            tasks=self.tasks,     # auto-created by @task
            process=Process.sequential,  # step-by-step execution
            verbose=True,
        )

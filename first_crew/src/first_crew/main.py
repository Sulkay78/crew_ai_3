#!/usr/bin/env python
import sys
import warnings
from datetime import datetime
from first_crew.crew import FirstCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This file lets you run, train, replay, or test your crew.
# Keep it simple; logic should live in crew.py, tasks.yaml, agents.yaml

def run():
    """
    Run the Analytical Coding Agent Crew.
    """
    inputs = {
        "topic": "ترتيب الدوري المصري",  # Example: Egyptian League table
        "current_year": str(datetime.now().year)
    }
    try:
        FirstCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }
    try:
        FirstCrew().crew().train(
            n_iterations=int(sys.argv[1]),
            filename=sys.argv[2],
            inputs=inputs
        )
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        FirstCrew().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and return results.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }
    try:
        FirstCrew().crew().test(
            n_iterations=int(sys.argv[1]),
            eval_llm=sys.argv[2],
            inputs=inputs
        )
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

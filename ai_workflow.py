import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables
load_dotenv()
gemini_api_key = os.getenv("GOOGLE_API_KEY")
if not gemini_api_key:
    raise ValueError("Please add your Gemini API key to the .env file as GOOGLE_API_KEY")

# Initialize Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0.7,
    google_api_key=gemini_api_key,
    stream=True
)

# Define Agents

def researcher_agent():
    return Agent(
        role="Researcher",
        goal="Gather accurate and current data for the topic",
        backstory="Expert in online research and extracting meaningful insights.",
        verbose=True,
        llm=llm
    )

def writer_agent():
    return Agent(
        role="Content Writer",
        goal="Write compelling and structured content based on research",
        backstory="Skilled writer who crafts engaging and informative pieces.",
        verbose=True,
        llm=llm
    )

def evaluator_agent():
    return Agent(
        role="Content Evaluator",
        goal="Evaluate and improve clarity, tone, and factual accuracy",
        backstory="Content quality assurance specialist.",
        verbose=True,
        llm=llm
    )

# Define Tasks

def get_tasks(topic):
    researcher = researcher_agent()
    writer = writer_agent()
    evaluator = evaluator_agent()

    task1 = Task(
        description=f"Research the topic: {topic}. Provide key points, facts, and recent insights.",
        expected_output="A bullet-point list of factual and up-to-date research findings.",
        agent=researcher
    )

    task2 = Task(
        description="Write a well-structured article based on the research findings.",
        expected_output="A 400-600 word article with introduction, body, and conclusion.",
        agent=writer,
        context=[task1]
    )

    task3 = Task(
        description="Evaluate and improve the article for clarity, tone, and factual accuracy.",
        expected_output="The final, polished version of the article ready for publishing.",
        agent=evaluator,
        context=[task2]
    )

    return [task1, task2, task3]

# Run the Crew

def run_workflow(topic):
    tasks = get_tasks(topic)
    agents = [t.agent for t in tasks]

    crew = Crew(
        agents=agents,
        tasks=tasks,
        verbose=True,
        llm=llm
    )

    result = crew.kickoff()
    return result

# Entry point

if __name__ == "__main__":
    topic = input("Enter a topic for content generation: ")
    output = run_workflow(topic)
    print("\n=== FINAL OUTPUT ===\n")
    print(output)
from browser_use import Agent, ChatOpenAI
from dotenv import load_dotenv
import asyncio
import yaml

load_dotenv()

async def main():
    llm = ChatOpenAI(model="gpt-4.1-mini")

    # Carrega o prompt do YAML
    with open("task.yaml", "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    
    task = config["task"]

    agent = Agent(task=task, llm=llm)
    await agent.run()

if __name__ == "__main__":
    asyncio.run(main())

from browser_use import Agent, ChatOpenAI
from dotenv import load_dotenv
import asyncio

load_dotenv()

async def main():
    llm = ChatOpenAI(model="gpt-4.1-mini")
    task = """
    1. Acesse o site do YouTube (https://www.youtube.com).
    2. Aguarde de 1 a 2 segundos.
    3. Vá até o campo de pesquisa e clique nele.
    4. Aguarde de 1 a 2 segundos.
    5. Digite o texto: "Agno vs LangGraph" e pressione Enter.
    6. Aguarde o carregamento dos resultados por 1 a 2 segundos.
    7. Procure o vídeo do canal "Gustavo Sacchi" com o título:
    "LangGraph vs Agno: Criei Agentes de IA que Escrevem Notícias SOZINHOS (Tutorial Completo)".
    8. Quando encontrar esse vídeo, clique nele.
    9. Aguarde o vídeo carregar completamente (1 a 2 segundos).
    10. Clique no botão de gostei (👍).
    11. Finalize a execução.
    """
    agent = Agent(task=task, llm=llm)
    await agent.run()

if __name__ == "__main__":
    asyncio.run(main())
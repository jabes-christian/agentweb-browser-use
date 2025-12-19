# Browser Use -- Agente de Automação Inteligente

Este projeto utiliza a biblioteca **browser-use** para criar uma
automação web inteligente, capaz de interpretar instruções em linguagem
natural e executar ações reais no navegador.

## 🚀 Tecnologias Utilizadas

-   **Python 3.10+**
-   **Browser-use** (núcleo da automação)
-   **Playwright** (camada de automação do navegador por trás do
    browser-use)
-   **OpenAI / LangChain-style Agent** (para interpretar instruções e
    planejar ações)

## 🧠 Como funciona

A automação recebe um conjunto de tarefas em YAML e o agente: 1. Lê e
entende o objetivo. 2. Planeja as ações. 3. Navega, clica, preenche
campos, extrai textos, cria arquivos etc. 4. Faz replanejamento em tempo
real caso algo dê errado.

## 📂 Estrutura do Projeto

-   `webagent_teste.py` -- script teste da automação\
-   `agenteweb.py` -- script principal da automação\
-   `task.yaml` -- arquivo que define a tarefa a ser executada\
-   `requirements.txt` -- arquivo com todas as dependencias da apliacação\
-   `README.md` -- documentação\
-   `.gitignore` -- padrões ignorados

## ▶️ Como Executar

``` bash
pip install -r requirements.txt
python agenteweb.py
```

## ✨ Pontos Fortes do Browser Use

-   Automação inteligente de verdade (agente toma decisões)
-   Capta falhas e tenta corrigir sozinho
-   Muito mais amigável que automações rígidas
-   Ótimo para protótipos e POCs rápidas

## ⚠️ Pontos de Atenção

-   Depende de prompts bem escritos\
-   Nem sempre acerta ações complexas de primeira\
-   Ainda é mais instável que Selenium/Playwright puro\
-   Exige ajustes finos conforme o site

## Autor

**Jabes Christian**  
Automation Developer  
[LinkedIn](https://www.linkedin.com/in/jabes-christian/) • [GitHub](https://github.com/jabes-christian)

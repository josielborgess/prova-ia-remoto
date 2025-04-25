# Prova IA – Desenvolvedor Back-End IA

O desafio consiste em criar um mini-backend de IA generativa **e** uma UI simples em Streamlit, conforme **user stories** e **corpus** fornecidos por e-mail.

O repositório inicial contém apenas o essencial para que você comece a codar em segundos (FastAPI + Streamlit *Hello, world!*). Cabe a você estruturar, implementar e documentar as demais funcionalidades.

Boa prova 😊  

---

## Estrutura do repositório

| Pasta                  | Descrição                                                                     |
|------------------------|-------------------------------------------------------------------------------|
| **backend/**           | FastAPI básico (`main.py`, health-check)                                      |
| **frontend/**          | `app.py` Streamlit mínimo                                                     |
| **data/corpus/**       | PDFs e DOCXs utilizados no RAG                                                |
| **requirements.txt**   | Adicione as bibliotecas conforme o necessário                                 |
| **README.md**          | <— VOCÊ está lendo — edite apenas a seção **Relatório do candidato** ao final |

---

## Regras de desenvolvimento

1. É permitido adicionar **novas bibliotecas** — basta incluí-las em `requirements.txt` (ou `pyproject.toml` se preferir Poetry).
2. Mantenha o projeto organizado em camadas (API, domínio, infraestrutura, testes).  
   Ex.: `/backend/chains`, `/backend/services`, `/backend/models`.
3. **Obrigatório**  
   - **Logar** prompts, respostas e uso de tokens em SQLite (`backend/db/usage.db`);
   - Commite as bases de dados utilizadas no projeto (em SQlite) 
   - Criar **≥ 4 commits significativos** com mensagens claras;  
4. *Push* direto na `main`/`master` do seu fork — **não** abra *pull request*.  

---

## Versão Python

Recomendado **Python 3.12** (mínimo 3.11).

---

## Configuração local (sem Docker)

### 1 – Clonar o repositório

```bash
git clone {link a ser enviado por e-mail}
cd prova-ia-generativa-backend
```

### 2 – Criar e ativar ambiente virtual

```bash
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\Activate.ps1
```

### 3 – Instalar dependências

```bash
pip install -r backend/requirements.txt
```

### 4 – Configurar variáveis de ambiente

Crie um arquivo `.env` na raiz (não faça commit!):

```
OPENAI_API_KEY=<fornecida por e-mail>
EMBEDDINGS_MODEL=text-embedding-3-small
CHAT_MODEL=gpt-4o
```

### 5 – Executar serviços

```bash
# Backend
uvicorn backend.main:app --reload --port 8000

# Em outro terminal
cd frontend
streamlit run app.py
```

- **Docs da API**: http://localhost:8000/docs  
- **UI**: http://localhost:8501  

---

## Relatório do candidato

> **Edite APENAS esta seção após concluir a prova.**

### Funcionalidades implementadas

- …

### Funcionalidades não implementadas / pendências

- …

### Novas bibliotecas adicionadas

| Lib | Motivo |
|-----|--------|
| …   | …      |

---

No mais, desenvolva com qualidade e divirta-se 🚀

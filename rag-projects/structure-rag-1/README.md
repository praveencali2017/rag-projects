# structure-rag-1

A text-to-SQL notebook workflow that answers natural-language questions over the [Chinook](https://github.com/lerocha/chinook-database) sample SQLite database using LangChain and OpenAI.

Ask a question like "List all the customers from Brazil" and the notebook will translate it into SQL, run it against the local database, and return a natural-language summary.

## How it works

The pipeline in [sql_agent.ipynb](sql_agent.ipynb) follows a simple LangChain flow:

1. **Schema loading** — the database schema is loaded from the local SQLite file and included in the prompt.
2. **SQL generation** — an LLM prompt generates a single read-only SQLite query from the user's question.
3. **Cleaning and validation** — the generated SQL is cleaned up and checked to block unsafe write operations.
4. **Execution** — the validated query is executed against the Chinook database using SQLite and pandas.
5. **Response generation** — the retrieved rows are turned into a friendly answer.

```text
user question → generate SQL → clean and validate → run against Chinook DB → summarize results → answer
```

> **Safety note:** this is a notebook demo and uses a basic allowlist-style validation check. It is not a hardened production SQL security boundary.

## Tech stack

- [LangChain](https://python.langchain.com/) for prompt-based query generation
- [langchain-openai](https://python.langchain.com/docs/integrations/platforms/openai) for OpenAI model access
- [langchain-community](https://python.langchain.com/docs/integrations/providers/community) for SQL database utilities
- pandas for working with query results
- pydantic-settings and python-dotenv for configuration loading
- SQLite for the local Chinook database

## Project structure

```text
structure-rag-1/
├── config.py          # loads OPENAI_API_KEY and OPENAI_LLM_MODEL from .env
├── data/
│   └── chinook.db     # sample SQLite database
├── sql_agent.ipynb    # the text-to-SQL workflow
├── pyproject.toml
└── uv.lock
```

## Setup

Requires Python 3.12+ and [uv](https://docs.astral.sh/uv/).

1. Install dependencies:
   ```bash
   uv sync
   ```
2. Create a .env file in this directory with:
   ```env
   OPENAI_API_KEY=sk-...
   OPENAI_LLM_MODEL=gpt-4o-mini
   ```
3. Open [sql_agent.ipynb](sql_agent.ipynb) and run the cells top to bottom.

## Usage

The notebook exposes a generate_response(user_query: str) helper:

```python
generate_response("List all the customers from Brazil")
generate_response("What are the top 5 best-selling genres?")
```

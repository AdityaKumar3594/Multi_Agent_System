# Multi-Agent Research System

A Python-based multi-agent research pipeline that uses LangChain, a web search tool, and a web scraper to gather information, generate a structured report, and critique the final output.

## Overview

This repository implements a small multi-agent system with two primary execution modes:

- **CLI pipeline** via `pipeline.py`
- **Streamlit web app** via `app.py`

The system uses:

- a **search agent** to gather recent web content using Tavily
- a **reader agent** to scrape and extract deeper page content from selected URLs
- a **writer chain** to draft a polished research report
- a **critic chain** to review the report and provide feedback

## Repository Structure

- `app.py` — Streamlit interface for running the research pipeline in a browser.
- `pipeline.py` — console-based orchestration of the full pipeline with printed progress.
- `agents.py` — agent and chain builder for search, reader, writer, and critic workflows.
- `tools.py` — custom LangChain tools for web search and scraping.
- `main.py` — simple placeholder entry point.
- `requirements.txt` — Python dependencies.
- `pyproject.toml` — project metadata and Python version requirements.
- `.env` — environment variables (not committed; used for API keys).

## Core Components

### Agents and Chains

`agents.py` defines:

- `build_search_agent()` — LangChain agent with `web_search_tool`
- `build_reader_agent()` — LangChain agent with `web_scraping_tool`
- `writer_chain` — prompt chain for generating a structured research report
- `critic_chain` — prompt chain for evaluating the report and producing feedback

### Tools

`tools.py` implements two LangChain tools:

- `web_search_tool(query: str)` — performs web search via the Tavily API and returns titles, URLs, and snippets
- `web_scraping_tool(url: str)` — fetches page HTML and extracts visible text using BeautifulSoup

### Pipeline

`pipeline.py` coordinates the full flow:

1. search for topic-related results
2. choose and scrape a top resource
3. combine findings and generate a report
4. critique the final report

### Streamlit App

`app.py` provides a polished UI with a four-step progress indicator, result cards, and download support.

## Setup

1. Create and activate a virtual environment:

```bash
python -m venv .venv
.\.venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file with your Tavily API key:

```ini
TAVILY_API_KEY=your_api_key_here
MISTRAL_API_KEY=your_api_key_here
```

## Usage

### Run the CLI pipeline

```bash
python pipeline.py
```

Enter a research topic when prompted.

### Run the Streamlit app

```bash
streamlit run app.py
```

Open the local Streamlit URL shown in the terminal to use the browser UI.

## Notes

- The current implementation uses `mistral-small-2506` via `ChatMistralAI`.
- The web scraper trims content to approximately 3000 characters to avoid overly large outputs.
- `app.py` includes custom styling and a stepper UI for a better user experience.

## Requirements

- Python 3.12+
- `langchain`
- `langchain-core`
- `langchain-community`
- `langchain-mistralai`
- `tavily`
- `bs4`
- `requests`
- `streamlit`


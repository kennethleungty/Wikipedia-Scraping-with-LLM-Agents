# How to Scrape Wikipedia with LLM Agents
## Combining LangChain's agents and tools with OpenAI's LLMs and function calling for the web scraping of Wikipedia

Link to step-by-step guide: https://medium.com/datadriveninvestor/how-to-web-scrape-wikipedia-using-llm-agents-f0dba8400692

### Context
- The task of web scraping Wikipedia is a highly useful technique for extracting valuable information, thanks to its vast collection of structured and unstructured data. 
- Traditional tools like Selenium, while effective, tend to be manual and time-consuming.
- The impressive capabilities of large language models (LLMs) and the ability to connect them to the Internet have ushered in new possibilities in many use cases, including the domain of web scraping.
- In this article, we harness a synergistic combination of LLM agents, tools, and function calling to extract data from Wikipedia readily.

### Data
- Top 200 songs of the 2010s (from Chart2000.com - https://chart2000.com/data/chart2000-song-2010-decade-0-3-0070.csv)

### Toolkit
- LangChain
  - Agents
  - Tools
  - Output Parsers
-  OpenAI
   - LLMs (specifically `gpt-3.5-turbo-1106`)
   - Function calling


### How to
- Run `python main.py` to execute the web scraping loop for the input songs dataset

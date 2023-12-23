import csv
import os

import box
import pandas as pd
import yaml
from dotenv import load_dotenv
from langchain.agents import (
    AgentExecutor,
    AgentType,
    OpenAIFunctionsAgent,
    Tool,
    initialize_agent,
)
from langchain.agents.format_scratchpad import format_to_openai_function_messages
from langchain.agents.output_parsers import OpenAIFunctionsAgentOutputParser
from langchain.callbacks import get_openai_callback
from langchain.chat_models import ChatOpenAI
from langchain.output_parsers.openai_functions import JsonOutputFunctionsParser
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder, PromptTemplate
from langchain.tools.render import format_tool_to_openai_function
from langchain_community.tools.ddg_search.tool import DuckDuckGoSearchRun
from langchain_community.utilities.wikipedia import WikipediaAPIWrapper


with open("config/config.yaml", "r", encoding="utf8") as ymlfile:
    cfg = box.Box(yaml.safe_load(ymlfile))
load_dotenv(dotenv_path=cfg.ENVDIR, verbose=True)

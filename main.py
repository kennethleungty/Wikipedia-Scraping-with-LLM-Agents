import csv
import json
import os

import box
import pandas as pd
import yaml

from langchain.callbacks import get_openai_callback
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.tools.render import format_tool_to_openai_function
from tenacity import retry, stop_after_attempt, wait_fixed

from src.agents import create_agent_executor
from src.llm import llm
from src.tools import wikipedia_tool
from src.prompts import system_prompt, generate_input_prompt
from src.utils import default_values


with open("config/config.yaml", "r", encoding="utf8") as ymlfile:
    cfg = box.Box(yaml.safe_load(ymlfile))

# Define tools
tools = [wikipedia_tool]
llm_with_tools = llm.bind(functions=[format_tool_to_openai_function(t) for t in tools])

# Define prompt
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("user", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)

agent_executor = create_agent_executor(
    prompt=prompt, llm_with_tools=llm_with_tools, tools=tools
)


@retry(
    stop=stop_after_attempt(2), wait=wait_fixed(10), retry_error_callback=default_values
)
def execute_web_scraping(
    input_file_path: str = cfg.INPUT_FILE, output_file_path: str = cfg.OUTPUT_FILE
):
    df = pd.read_csv(input_file_path)
    for _, row in df.iterrows():
        song, artist = row["song"], row["artist"]
        if os.path.exists(output_file_path):
            df_song_info = pd.read_csv(output_file_path, encoding="utf-8")
        else:
            df_song_info = pd.DataFrame(
                columns=[
                    "artist",
                    "song",
                    "genre",
                    "label",
                    "language",
                    "llm_cost",
                    "llm_tokens",
                    "producers",
                    "songwriters",
                ]
            )
            df_song_info.to_csv(output_file_path, index=False)

        if song not in df_song_info["song"].tolist():
            print(f"***** Processing: {song} by {artist} *****")
            input_prompt = generate_input_prompt(song, artist)
            with get_openai_callback() as cb:
                response = agent_executor.invoke({"input": input_prompt})
                cost = cb.total_cost
                tokens = cb.total_tokens
                output = response["output"]
                print(output)
                output_dict = json.loads(output)

                new_row = {
                    "artist": artist,
                    "song": song,
                    "genre": output_dict.get("genre"),
                    "label": output_dict.get("label"),
                    "language": output_dict.get("language"),
                    "llm_cost": cost,
                    "llm_tokens": tokens,
                    "producers": output_dict.get("producers"),
                    "songwriters": output_dict.get("songwriters"),
                }

                with open(output_file_path, "a", newline="", encoding="utf-8") as file:
                    writer = csv.writer(file)
                    writer.writerow(new_row.values())


if __name__ == "__main__":
    execute_web_scraping()

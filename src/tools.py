from langchain_community.tools.ddg_search.tool import DuckDuckGoSearchRun
from langchain_community.utilities.wikipedia import WikipediaAPIWrapper

from langchain.agents import Tool

wikipedia_tool = Tool(
    name="wikipedia",
    func=WikipediaAPIWrapper().run,
    description="Useful for when you need to look up the songwriters, genre, \
                and producers for a song on wikipedia",
)

duckduckgo_tool = Tool(
    name="DuckDuckGo_Search",
    func=DuckDuckGoSearchRun().run,
    description="Useful for when you need to do a search on the internet to find \
                information that the other tools can't find.",
)

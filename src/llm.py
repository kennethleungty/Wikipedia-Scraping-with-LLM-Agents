import box
import yaml
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI

with open("config/config.yaml", "r", encoding="utf8") as ymlfile:
    cfg = box.Box(yaml.safe_load(ymlfile))
load_dotenv(dotenv_path=cfg.ENVDIR, verbose=True)

llm = ChatOpenAI(
    model=cfg.MODEL_NAME, temperature=cfg.TEMPERATURE, model_kwargs={"seed": cfg.SEED}
)

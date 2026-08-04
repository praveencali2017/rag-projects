from pydantic_settings import BaseSettings
from pydantic import Field
import os

class Settings(BaseSettings):

    openai_api_key: str = Field(description="OpenAI API key", env="OPENAI_API_KEY")
    openai_llm_model: str = Field(description="OpenAI LLM model", env="OPENAI_LLM_MODEL")

# Create an instance of the Settings class to access the configuration values
settings = Settings()

os.environ["OPENAI_API_KEY"] = settings.openai_api_key
os.environ["OPENAI_LLM_MODEL"] = settings.openai_llm_model
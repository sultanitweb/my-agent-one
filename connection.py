import os
from agents import AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig

# Get the API key from an environment variable for security
gemini_api_key = os.getenv("GOOGLE_API_KEY")

if not gemini_api_key:
    raise ValueError("Please set the GOOGLE_API_KEY environment variable.")

# Use the openai client with the API key and the base URL
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)
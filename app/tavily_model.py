from tavily import TavilyClient, MissingAPIKeyError
import os
from dotenv import load_dotenv

load_dotenv()

tavily_api_key = os.getenv('TAVILY_API_KEY')

try:
    tavily_client = TavilyClient(api_key=tavily_api_key)
except MissingAPIKeyError:
    print("API key is missing. Please provide a valid API key.")


def search_result_using_tavily(query:str):
    response = tavily_client.get_search_context(query)
    print("Travily model is running....!")
    # print(response)
    return response


# search_result_using_tavily("Virat")
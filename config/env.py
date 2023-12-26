import os
from dotenv import load_dotenv

# Load environment variables from the .env file in the parent directory
dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
load_dotenv(dotenv_path)

OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
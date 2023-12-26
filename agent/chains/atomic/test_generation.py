from config.env import OPENAI_API_KEY
from langchain.llms import openai
from langchain.chains import LLMChain
from agent.prompts import test_generation_prompt

def initialize_test_generation_chain() -> LLMChain:
    """
    Initialize the Langchain chain with the OpenAI model and prompt template.
    
    Returns:
        LLMChain: Initialized Langchain chain.
    """
    model = openai.OpenAI(api_key=OPENAI_API_KEY)
    
    test_generation_chain = LLMChain(
        llm=model,
        prompt=test_generation_prompt,
        output_key='test'
    )
    
    return test_generation_chain

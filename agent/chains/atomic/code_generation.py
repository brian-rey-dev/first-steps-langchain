from config.env import OPENAI_API_KEY
from langchain.llms import openai
from langchain.chains import LLMChain
from agent.prompts import code_generation_prompt

def initialize_code_generation_chain() -> LLMChain:
    """
    Initialize the Langchain chain with the OpenAI model and prompt template.
    
    Returns:
        LLMChain: Initialized Langchain chain.
    """
    model = openai.OpenAI(api_key=OPENAI_API_KEY)
    
    code_generation_chain = LLMChain(
        llm=model,
        prompt=code_generation_prompt,
        output_key='code'
    )
    
    return code_generation_chain

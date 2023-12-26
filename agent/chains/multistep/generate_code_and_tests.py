from langchain.chains import SequentialChain
from agent.chains.atomic.code_generation import initialize_code_generation_chain
from agent.chains.atomic.test_generation import initialize_test_generation_chain
from typing import List


def initialize_code_and_test_sequential_chain(inputs: List[str]) -> SequentialChain:
    outputs = ['code', 'test']
    
    chain = SequentialChain(
        chains=[
            initialize_code_generation_chain(),
            initialize_test_generation_chain()
        ],
        output_variables=outputs,
        input_variables=inputs
    )
    
    return chain
    
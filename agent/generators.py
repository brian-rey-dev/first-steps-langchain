from agent.inputs import CodeGenerationPromptInputs
from agent.chains.multistep.generate_code_and_tests import initialize_code_and_test_sequential_chain
from typing import Dict

def generate_code_and_tests(inputs: CodeGenerationPromptInputs) -> Dict[str,str]:
  input_keys = list(inputs.keys())
  chain = initialize_code_and_test_sequential_chain(input_keys)
  
  return chain(inputs)
from langchain.prompts import PromptTemplate

code_generation_prompt = PromptTemplate(
  template="Write a very short {language} function that will {task}. Write it maximizing optimization and ensuring you write very elegant and simple code.",
  input_variables=['language', 'task']
)

test_generation_prompt = PromptTemplate(
  template="Write a unit test for this {code} written in {language}. Cover multiple scenarios and document it properly.",
  input_variables=['language', 'task']
)
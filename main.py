import streamlit as st
from agent.generators import generate_code_and_tests
from agent.inputs import CodeGenerationPromptInputs

def main():
    st.title("Code Generation using Langchain")

    # Input fields
    languages = ["python", "javascript", "java", "c++", "ruby", "go"]  # Add or remove languages as needed
    language = st.selectbox("Select the language:", languages)
    task = st.text_input("Enter the task:")

    # Button to generate code
    if st.button("Generate Code"):
        if language and task:
            user_input = CodeGenerationPromptInputs(language=language, task=task)

            # Use st.spinner to show a loading spinner while processing
            with st.spinner("Generating code... Please wait"):
                try:
                    generated_output = generate_code_and_tests(user_input)
                    st.success("Code Generated Successfully.")

                    # Display the generated code
                    if 'code' in generated_output:
                        st.subheader("Generated Code:")
                        st.code(generated_output['code'], language=language)  # Adjust the language if needed

                    # Display the generated tests
                    if 'test' in generated_output:
                        st.subheader("Generated Test:")
                        st.code(generated_output['test'], language=language)  # Adjust the language if needed

                except Exception as e:
                    st.error(f"An error occurred while generating code: {e}")
        else:
            st.warning("Both language and task must be provided.")

if __name__ == '__main__':
    main()

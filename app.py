import streamlit as st
from ai_workflow import run_workflow

st.set_page_config(page_title="AI Agent Workflow", layout="centered")
st.title("\U0001F9E0 AI Agent Workflow")
st.markdown("**Multi-step content creation with Researcher ➔ Writer ➔ Evaluator agents**")

prompt = st.text_input("Enter a topic to generate content:", placeholder="e.g., How AI is changing education")

if st.button("Run Workflow") and prompt:
    with st.spinner("Running AI workflow..."):
        try:
            result = run_workflow(prompt)
            st.success("Workflow completed!")
            st.subheader("\U0001F4DD Final Output")
            st.write(result)

            # Optional: Export to text file
            st.download_button("Download Output", result, file_name="ai_output.txt")
        except Exception as e:
            st.error(f"Error: {e}")

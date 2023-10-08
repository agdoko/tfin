import streamlit as st
import google.generativeai as palm

# Set the title of your Streamlit app
st.title("Meme from Text Creator")

# Configure api key authentication
palm.configure(api_key=st.secrets["PALM_API_KEY"])

# Get a list of available models, print one
models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name
st.write(model)

#TODO: Add a text input field and move the code below into the button

prompt = """
You are an expert at solving word problems.

Solve the following problem:

Tell me a funny joke about a cafe that is very full at the start of busines at 10am on a Sunday morning.

Think about it step by step, and show your work.
"""

completion = palm.generate_text(
    model=model,
    prompt=prompt,
    temperature=0,
    # The maximum length of the response
    max_output_tokens=800,
)

st.write(completion.result)
####

# Add a button to initiate meme generation
if st.button("Create Meme"):
    pass

else:
    st.write("Please write something")

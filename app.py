import streamlit as st
from langchain.llms import OpenAI
from transformers import pipeline
sentiment_pipeline = pipeline("sentiment-analysis")
# initialize the models
openai = OpenAI(
    model_name="text-davinci-003",
    openai_api_key="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"
)
def generate_email(content, tone, recipient_type,recipient_name,sender_name):
    # Prompt
    prompt = f"Generate a professional email to a {recipient_type} with an elaboration on the following content: '{content}' and set the tone to {tone}. The name of the recipient is {recipient_name} and name of the sender is {sender_name}"

    response = openai(prompt)
    return response

# Example usage
st.title("Email Generator")
email_content = st.text_input("Enter Content",placeholder="Enter Details for the Email")
if not email_content:
    email_content = "Trail email"
selected_tone = st.selectbox(label="Select the the tone of tour mail",
                             options=("Formal","Informal","Happy","Angry","Sad","Sarcastic"))
selected_recipient_type = st.radio(label="Enter Realtionship",
                                   options=("Boss","Coworker"))
recipient_name = st.text_input("Enter Receiver Name",placeholder="Name of the Receiver")
if not recipient_name:
    recipient_name = selected_recipient_type
sender_name = st.text_input("Enter Sender Name",placeholder="Name of the sender")
if not sender_name:
    sender_name = "[Insert Name]"
if st.button("Generate"):
    generated_email = generate_email(email_content, selected_tone, selected_recipient_type,recipient_name,sender_name)
    st.write(generated_email)
    score = sentiment_pipeline(generated_email)
    if score[0]['label'] == 'POSITIVE':
        st.success(f"Sentiment = Positive")
        st.success(f"Confidence = {score[0]['score']*100}%")
    else:
        st.error(f"Sentiment = Negative")
        st.error(f"Confidence = {score[0]['score']*100}%")
        
# Print the generated email
# print(generated_email)
# print(sentiment_pipeline(generated_email))

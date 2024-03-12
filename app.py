import streamlit as st

# Function to generate a response from the chatbot
def get_response(input_text):
    # You can implement your chatbot logic here
    # For now, let's just echo back the input
    return f"You said: {input_text}"

# Streamlit UI
def main():
    st.title("Simple Chatbot")

    # Text input for user to type their message
    user_input = st.text_input("Enter your message here:")

    # Button to submit the message
    if st.button("Send"):
        # Display the user's message
        st.write(f"You: {user_input}")

        # Get and display the chatbot's response
        bot_response = get_response(user_input)
        st.write(f"Bot: {bot_response}")

if __name__ == "__main__":
    main()

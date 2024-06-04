from groq import Groq

client = Groq(
    api_key="",
)

# Define a variable to store conversation history
conversation_history = []

# Initial prompt of the chatbot
print("Hello! How can I help you?\n")
prompt_phrase = "Ask me anything or type 'exit' or 'finished' to quit: "

while True:
    try:
        user_input = input(prompt_phrase)  # Take the user's input
        if user_input.lower() in ["exit", "finished"]:
            print("Have a nice day!")
            break  # Quit the loop if the user's input is one of the end words

        # Add the user's question to the conversation history
        conversation_history.append({"role": "user", "content": user_input})

        # Create a request to end the conversation with the user's question
        chat_completion = client.chat.completions.create(
            messages=conversation_history,
            model="llama3-8b-8192",
        )

        # Add the chatbot's response to the conversation history
        conversation_history.append(chat_completion.choices[0].message)

        # Print the result
        print("Chatbot response:", chat_completion.choices[0].message.content)

    except Exception as e:
        print("Something went wrong. Please try again!")

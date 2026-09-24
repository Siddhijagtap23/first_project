from langchain_groq import ChatGroq
# Import ChatGroq to use Groq models

from dotenv import load_dotenv
# Import function to load .env variables

load_dotenv(override=True)
# Load API key from .env file

llm = ChatGroq(model="openai/gpt-oss-120b")
# Create the AI model using Groq

print("My first chatbot")
# Display chatbot title
history=[]

while True:
# Keep the chatbot running

    prompt = input("user: ")
    # Take input from the user
    history.append(prompt)

    if prompt == "exit":
        # Check if user wants to stop

        break
        # Stop the loop

    response = llm.invoke(history)
    # Send the user's question to the AI
    history.append(response)

    print("AI:", response.content)
    # Print the AI's actual response

     
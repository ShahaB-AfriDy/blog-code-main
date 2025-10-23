from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import HumanMessage
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=os.getenv("GOOGLE_API_KEY")
)
prompt = ChatPromptTemplate.from_template(
    "You are a helpful AI chatbot. Answer the user query politely and clearly.\n\nUser: {question}"
)

def Chatbot(user_input: str):
    """Generate chatbot response from Gemini model using LangChain."""
    messages = prompt.format_messages(question=user_input)
    response = llm.invoke(messages)
    return response


if __name__ == "__main__":
    print("Gemini Chatbot (type 'exit' to quit)\n")
    while True:
        print(" Human Message ".center(80,"="))
        user_input = input()
        if user_input.lower() in ["exit", "quit"]:
            print(" Bot exit ".center(100,"*"))
            break
        chatbot_response = Chatbot(HumanMessage(content=user_input))
        chatbot_response.pretty_print()

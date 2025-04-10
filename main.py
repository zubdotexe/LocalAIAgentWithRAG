from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(model="gemma3:1b")

template = """
    You are an expert in answering questions about a pizza restaurant

    Here are some relevant reviews: {reviews}

    Here is the question to answer: {question}
"""

prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model

while True:
    print("\n\n")
    print("="*50)
    question = input("Please ask (q to quit):\n")
    print("\n\n")

    if question == "q":
        print("Quitting the program...\n\n")
        break
    
    reviews = retriever.invoke(question)
    result = chain.invoke({"reviews": reviews, "question": question})

    print(result)
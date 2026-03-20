from rag import RAGSystem
from llm import generate_answer

rag=RAGSystem()

query=input("Ask a question: ")

retrieved_docs=rag.retrieve(query)

context="\n".join(retrieved_docs)

answer=generate_answer(context,query)

print("\nAnswer: ")
print(answer)
LangChain vs Manual Implementation — Examples


The goal is to highlight how LangChain abstracts common tasks such as prompt management, memory handling, and multi-step orchestration.


🧩 Example 1: Using OpenAI Client vs LangChain for Simple Prompting
Without LangChain (Manual OpenAI Client)
```
from openai import OpenAI

client = OpenAI()

def generate_answer(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

print(generate_answer("What is LangChain and why is it useful?"))
```
With LangChain
```
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOpenAI(model="gpt-4o-mini")
prompt = ChatPromptTemplate.from_template("What is LangChain and why is it useful?")
chain = prompt | llm

print(chain.invoke({}))
```

🧠 Example 2: Manual Memory Handling vs LangChain Memory
Without LangChain (Manual Context Tracking)
```
from openai import OpenAI

client = OpenAI()
chat_history = []

def chat_with_memory(user_input):
    global chat_history
    chat_history.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=chat_history
    )
    answer = response.choices[0].message.content
    chat_history.append({"role": "assistant", "content": answer})
    return answer

print(chat_with_memory("Hello, who are you?"))
print(chat_with_memory("Can you remind me what I just asked?"))
```

With LangChain
```

from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

llm = ChatOpenAI(model="gpt-4o-mini")
memory = ConversationBufferMemory()
conversation = ConversationChain(llm=llm, memory=memory)

print(conversation.predict(input="Hello, who are you?"))
print(conversation.predict(input="Can you remind me what I just asked?"))
```

⚙️ Example 3: Multi-Step Workflow (Manual vs LangChain)
Without LangChain (Manual Chaining)
```
from openai import OpenAI

client = OpenAI()

def summarize_text(text):
    return client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": f"Summarize this: {text}"}]
    ).choices[0].message.content

def translate_summary(summary):
    return client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": f"Translate this to Spanish: {summary}"}]
    ).choices[0].message.content

text = "LangChain helps developers build context-aware, reasoning AI systems."
summary = summarize_text(text)
translation = translate_summary(summary)
print(translation)
```
With LangChain
```
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableSequence

llm = ChatOpenAI(model="gpt-4o-mini")

summarize_prompt = ChatPromptTemplate.from_template("Summarize this: {text}")
translate_prompt = ChatPromptTemplate.from_template("Translate this to Spanish: {summary}")

summarize_chain = summarize_prompt | llm
translate_chain = translate_prompt | llm

workflow = RunnableSequence(first=summarize_chain, second=translate_chain)

print(workflow.invoke({"text": "LangChain helps developers build context-aware, reasoning AI systems."}))
```
---
RAG (embeddings + retrieval)
3A — Manual embeddings + FAISS (minimal)

```
import openai
import faiss
import numpy as np

openai.api_key = "OPENAI_API_KEY"

# Example docs
docs = ["LangChain connects LLMs and data.", "LangGraph is for graph orchestration."]
# Create embeddings (OpenAI)
emb_list = []
for d in docs:
    emb = openai.Embedding.create(model="text-embedding-3-small", input=d)["data"][0]["embedding"]
    emb_list.append(np.array(emb, dtype=np.float32))

# Build FAISS index
dim = len(emb_list[0])
index = faiss.IndexFlatL2(dim)
index.add(np.vstack(emb_list))

# Query
q = "What coordinates multiple agents?"
q_emb = np.array(openai.Embedding.create(model="text-embedding-3-small", input=q)["data"][0]["embedding"], dtype=np.float32)
D, I = index.search(q_emb.reshape(1, -1), k=1)
print("Best doc:", docs[int(I[0][0])])

```

3B — LangChain RAG (OpenAIEmbeddings + FAISS + RetrievalQA)
```
# 3B_langchain_rag.py
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA

# Docs
texts = ["LangChain connects LLMs and data.", "LangGraph coordinates multi-agent workflows."]

# Create embeddings + FAISS via LangChain helper
emb = OpenAIEmbeddings(model="text-embedding-3-small")
vectorstore = FAISS.from_texts(texts, emb)

# Build retrieval QA chain
llm = OpenAI(model_name="gpt-4", temperature=0.2)
qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=vectorstore.as_retriever())

# Query
print(qa.run("Which library helps coordinate multiple agents?"))
```


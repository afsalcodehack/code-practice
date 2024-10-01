import os
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA

# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = "your-openai-api-key"

# Step 1: Load and preprocess documents
loader = TextLoader('your_documents.txt')  # Replace with your document path
documents = loader.load()

# Step 2: Split documents into chunks
from langchain.text_splitter import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
docs = text_splitter.split_documents(documents)

# Step 3: Generate embeddings for documents
embeddings = OpenAIEmbeddings()
vector_store = FAISS.from_documents(docs, embeddings)

# Step 4: Create a retriever
retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 3})

# Step 5: Initialize the language model
llm = OpenAI(temperature=0)

# Step 6: Create the RetrievalQA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",  # Options: 'stuff', 'map_reduce', 'refine', 'map_rerank'
    retriever=retriever,
    return_source_documents=True
)

# Step 7: Query the chain
query = "What are the maintenance procedures for HVAC systems?"
result = qa_chain(query)

# Step 8: Print the answer and source documents
print("Answer:")
print(result['result'])

print("\nSource Documents:")
for doc in result['source_documents']:
    print(doc.page_content)

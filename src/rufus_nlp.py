from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from sentence_transformers import SentenceTransformer
import openai
import os

# Load OpenAI API Key (Set your key as an environment variable)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

def split_text(text, chunk_size=512, overlap=50):
    """ Splits text into manageable chunks """
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=overlap)
    return splitter.split_text(text)

def generate_embeddings(text_chunks):
    """ Converts text chunks into embeddings for similarity search """
    return embedding_model.encode(text_chunks, convert_to_tensor=True)

def rank_relevant_text(text_chunks, query):
    """ Finds the most relevant text chunks based on user query """
    query_embedding = embedding_model.encode(query, convert_to_tensor=True)
    chunk_embeddings = generate_embeddings(text_chunks)

    # Compute cosine similarity
    similarities = (query_embedding @ chunk_embeddings.T).tolist()
    
    # Rank chunks by relevance
    ranked_chunks = sorted(zip(text_chunks, similarities), key=lambda x: x[1], reverse=True)
    return [chunk for chunk, _ in ranked_chunks[:3]]  # Return top 3 relevant chunks

def filter_relevant_text(raw_text, user_query):
    """ Main function to extract and return relevant content """
    text_chunks = split_text(raw_text)
    # Ensure we don't pass empty chunks to the embedding model
    text_chunks = [chunk for chunk in text_chunks if len(chunk.split()) > 5]

    if not text_chunks:
        return ["No relevant content found."]
    
    return rank_relevant_text(text_chunks, user_query)

# ## Optional: Uncomment if you want to use OpenAI for summarization
# def summarize_text(text):
#     """ Uses GPT-4 to summarize extracted text (Optional) """
#     if not OPENAI_API_KEY:
#         print("No OpenAI API key found. Returning unmodified text.")
#         return text  # Skip if no API key

#     response = openai.ChatCompletion.create(
#         model="gpt-4",
#         messages=[{"role": "system", "content": "Summarize this text in a concise way."},
#                   {"role": "user", "content": text}]
#     )
#     return response["choices"][0]["message"]["content"]

def summarize_text(text):
    """ Alternative Summarization without OpenAI (Simple Extractive Summary) """
    sentences = text.split(". ")
    return " ".join(sentences[:3]) 
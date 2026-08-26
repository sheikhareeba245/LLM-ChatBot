import os
import numpy as np
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client=genai.Client(api_key=api_key)

sentences=[
    "I love reading books",
    "Reading novels is my favorite habbit",
    "The water is cold today."
]
try:
    embeddings=[]
    for sentence in sentences:
        result=client.models.embed_content(
            model="gemini-embedding-001",
            contents=sentence
        )
        vector=result.embeddings[0].values
        embeddings.append(vector)

        print(f"Sentence: {sentence}")
        print(f"Vector Length: {len(vector)}")
        print(f"First 5 values: {vector[:5]}\n")

    # Manually calculate consine similarity with the help of numpy
    def cosine_similarity(vec1,vec2):
        vec1=np.array(vec1)
        vec2=np.array(vec2)
        dot_product=np.dot(vec1,vec2)
        norm1=np.linalg.norm(vec1)
        norm2=np.linalg.norm(vec2)
        return dot_product/(norm1*norm2)

    sim_1_2=cosine_similarity(embeddings[0],embeddings[1])
    sim_1_3=cosine_similarity(embeddings[0],embeddings[2])

    print(f"Similarity (Sentence 1 & 2 -both about reading):{sim_1_2:.4f}")
    print(f"Similarity (Sentence 1 & 3 - unrelated topics ):{sim_1_3:.4f}")
except Exception as e:
    print(f"Error: {e}")

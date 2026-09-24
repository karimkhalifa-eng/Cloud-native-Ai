from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')


chunks=[
    "The agent uses FastAPI web server to handle incoming requests and provide responses.",
    "The calculator supports basic arithmetic operations.",
    "JSON data is stored in a local file for persistence."
]

embeddings = model.encode(chunks)
print(embeddings)

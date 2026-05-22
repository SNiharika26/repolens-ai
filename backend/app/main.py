from fastapi import FastAPI

app = FastAPI(title="RepoLens AI")

@app.get("/")
def root():
    return {"message": "RepoLens AI backend is running"}

@app.post("/ask")
def ask_question(question: str):
    return {
        "question": question,
        "answer": "RepoLens will search the repository and answer using AI."
    }
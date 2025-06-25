from fastapi import FastAPI
from routes import ia
import os
import uvicorn
from rich import print
import redis

redis_client = redis.Redis(host="localhost", port=6379, decode_responses=True)

# Exemplo de uso:
redis_client.set("chave", "valor")
print(redis_client.get("chave"))


PORT = 3000

app = FastAPI()

app.include_router(ia.router, prefix="/api/v1/ia", tags=["IA"])

@app.get("/api/v1")
def hello():
    return {"message": "Foi hein!"}

if __name__ == '__main__':
    port = int(os.environ.get("PORT", PORT))
    print("[bold blue] Iniciando o backend Elizabet...[/]")
    print(f"[yellow]Rodando em http://localhost:{port}/api/v1[/]")
    uvicorn.run(app=app, port=port)

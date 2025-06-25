
# 🤖 ELIZABET - Assistente de Análises Esportivas

Elizabet é uma IA especializada em prever resultados de partidas de futebol com base em mensagens do usuário. Você envia um confronto (ex: "Palmeiras x Botafogo") e ela retorna a **probabilidade de vitória** de cada time, como:

```
Palmeiras x Botafogo  
65% x 35%
```

A IA responde com linguagem direta, como se fosse uma analista de apostas esportivas.  
Você pode integrá-la com outras APIs de futebol para pré-processar dados e gerar previsões mais completas.

---

## 🚀 Rodando o projeto

Certifique-se de ter o Python e o `venv` ativado.

```bash
# Instale as dependências
pip install -r requirements.txt

# Rode a aplicação
uvicorn main:app --host 0.0.0.0 --port 3000 --reload
```

A API estará disponível em:  
👉 [`http://localhost:3000/api/v1`](http://localhost:3000/api/v1)  
Swagger docs: [`http://localhost:3000/docs#/`](http://localhost:3000/docs#/)

---

## 🧪 Como usar

Faça uma requisição POST para:

```
POST /api/v1/ia/resposta-ia
```

Com o seguinte corpo JSON:

```json
{
  "response_user": "Flamengo x Chelsea"
}
```

A resposta será algo assim:

```json
{
  "success": true,
  "message": "Flamengo x Chelsea\n55% x 45%",
  "code": 200
}
```

---

## 🗂️ Estrutura de Pastas

```plaintext
elizabet/
└── backend/
    └── src/
        ├── main.py                 # Arquivo principal da aplicação FastAPI
        ├── controllers/            # Lógica de controle de rotas
        │   └── ia_controller.py    # Controller para IA
        ├── routes/                 # Definição de endpoints
        │   └── ia.py               # Rotas da IA
        ├── schema/                 # Schemas (Pydantic) para validação de entrada
        │   └── schemas.py          
        ├── services/               # Serviços e lógica de integração com a IA
        │   └── ia.py               # Comunicação com a API Groq (LLaMA)
        └── __init__.py             # Deixa o diretório como pacote Python
    ├── .env                        # Segredos (ex: chave da API Groq)
    ├── requirements.txt            # Dependências
    └── README.md                   # Este arquivo
```

---

## 📌 Notas

- A IA usada é o modelo **LLaMA-3** da Groq.
- Toda a lógica de predição está na pasta `services/`.
- Elizabet pode ser integrada com bancos de dados e APIs de futebol para análises mais avançadas.
- O projeto segue boas práticas com separação de camadas: `routes`, `controllers`, `schemas`, `services`.

---

## 👨‍💻 Autor

Desenvolvido por **Alessandro (Juninho)** – criador da Elizabet, fã de futebol, código limpo e IA criativa ⚽🧠.
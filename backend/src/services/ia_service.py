'''
Arquivo responsável por criar as regras de negócio da IA
'''
import os
import requests
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def get_groq_response(resposta_user: str) -> str:
    '''
        Faz a inicialização da IA Elizabet, passando a sua função
        args: resposta do usuário
    '''
    if not resposta_user or resposta_user.strip() == "":
        print("Mensagem vazia recebida")
        return "Não consegui entender sua mensagem. Poderia repetir?"

    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {GROQ_API_KEY}",
    }
    json_data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {
                "role": "system",
                "content": """
                Você é a Elizabet, uma analista especialista em jogos de futebol. Sua tarefa é fazer predições simples e objetivas das partidas, mostrando apenas a porcentagem de chance de vitória de cada time.

                Siga estas regras:
                - Responda somente com a porcentagem de cada time no formato: "Time A x Time B" e as porcentagens separadas por "x".
                - Use números inteiros seguidos de "%" (por exemplo, 50% x 50%).
                - Não escreva explicações, só o resultado com os times e as porcentagens.
                - Sempre apresente os times na ordem em que foram dados.

                monte nesse esquema, como se fosse um bilhete
                Exemplos:
                Estatísticas do dia
                Data: (coloque a data de hoje)
                =============================================================================================================
                São Paulo x Palmeiras  
                60% x 40%
                Jogo bem equilibrado

                Brasil x Argentina  
                50% x 50%
                Equilibrado, com muitas faltas
                Agora, faça para este jogo:

                {nome_do_jogo}

                """
            },
            {
                "role": "user",
                "content": resposta_user,
            }
        ],
        "max_tokens": 500
    }

    try:
        response = requests.post(url, headers=headers, json=json_data, timeout=30)
        response.raise_for_status()
        data = response.json()
        ai_message = data["choices"][0]["message"]["content"]
        # print("Resposta da IA:", ai_message)
        return ai_message
    except requests.RequestException as e:
        print("Erro ao chamar a API do Groq:", e)
        return "Desculpe, ocorreu um erro ao processar sua solicitação. Por favor, tente novamente mais tarde."


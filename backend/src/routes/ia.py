from fastapi import APIRouter
from schema.schemas import Pergunta 
import services.ia_service as ia_service  

router = APIRouter()


@router.get("/")
async def hello():
    return {"message": "Foi hein"}

@router.post("/resposta-ia")
async def obter_resposta(pergunta: Pergunta):
    """
    Retorna a resposta da IA
    args: response_user (str): texto do usuário
    """
    response_ia = ia_service.get_groq_response(pergunta.response_user)
    return {
        "success": True,
        "message": response_ia,
        "code": 200
    }

from fastapi import APIRouter
import controllers.ia_controller as ia_controller
from schema.schemas import Pergunta

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
    response_ia = ia_controller.response_ia(pergunta.response_user)
    return response_ia

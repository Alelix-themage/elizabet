

#Módulo responsável pela controller das IA's

import services.ia_service as ia_service
from schema.schemas import Pergunta

def response_ia(response_user: Pergunta):
    
    # Resposta da IA
    # args: response_user

    if response_user is None:
        return {
            "success": False,
            "message": "Dados enviados ausentes ou inválidos",
            "code": 404
        }
    try:
        response_user = response_user
        ret_response_ia = ia_service.get_groq_response(response_user)
        
        
        return {
            "success": True,
            "message": ret_response_ia,
            "code": 200
        }
    except Exception as error:
        return {
            "success": False,
            "message": error,
            "code": 500

        }

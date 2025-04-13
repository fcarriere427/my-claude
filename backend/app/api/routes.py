"""
Routes de l'API FastAPI.
Définit les endpoints pour interagir avec Claude.
"""
from fastapi import APIRouter, HTTPException, Depends
from ..services.claude import claude_service
from ..config import settings
from .models import ChatRequest, ChatResponse, HealthCheck

router = APIRouter()

@router.get("/health", response_model=HealthCheck)
async def health_check():
    """Vérifie la santé de l'API."""
    return {
        "status": "ok",
        "version": settings.APP_VERSION
    }

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Endpoint pour envoyer un message à Claude et obtenir une réponse.
    
    Args:
        request: La requête contenant le message et l'historique
        
    Returns:
        La réponse de Claude et l'historique mis à jour
    """
    try:
        result = await claude_service.send_message(
            message=request.message,
            conversation_history=request.conversation_history
        )
        return ChatResponse(
            response=result["response"],
            conversation_history=result["conversation_history"]
        )
    except Exception as e:
        # Log l'erreur ici si nécessaire
        raise HTTPException(status_code=500, detail=f"Erreur lors de la communication avec Claude: {str(e)}")

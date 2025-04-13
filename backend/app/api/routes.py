"""
Routes de l'API FastAPI.
Définit les endpoints pour interagir avec Claude.
"""
from fastapi import APIRouter, HTTPException
from ..services.claude import claude_service
from ..services.currency import currency_service
from ..config import settings
from .models import ChatRequest, ChatResponse, HealthCheck, ModelsResponse, ModelInfo, ModelPricing

router = APIRouter()

@router.get("/health", response_model=HealthCheck)
async def health_check():
    """Vérifie la santé de l'API."""
    return {
        "status": "ok",
        "version": settings.APP_VERSION
    }

@router.get("/models", response_model=ModelsResponse)
async def get_models():
    """
    Récupère la liste des modèles Claude disponibles.
    
    Returns:
        Liste des modèles avec leurs informations et le taux de conversion USD->EUR
    """
    # Récupérer le taux de conversion USD->EUR
    usd_to_eur_rate = await currency_service.get_exchange_rate()
    
    models = []
    for model_data in claude_service.get_available_models():
        models.append(ModelInfo(
            id=model_data["id"],
            name=model_data["name"],
            description=model_data["description"],
            pricing=ModelPricing(
                input=model_data["pricing"]["input"],
                output=model_data["pricing"]["output"]
            ),
            current=model_data.get("current", True)  # Par défaut à True si non spécifié
        ))
    
    return ModelsResponse(
        models=models,
        usd_to_eur_rate=usd_to_eur_rate,
        rate_updated_at=currency_service.last_update
    )

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Endpoint pour envoyer un message à Claude et obtenir une réponse.
    
    Args:
        request: La requête contenant le message, l'historique et le modèle à utiliser
        
    Returns:
        La réponse de Claude et l'historique mis à jour
    """
    try:
        # Vérifier si un modèle spécifique a été demandé et s'il existe
        model_id = request.model_id
        if model_id:
            model_info = claude_service.get_model_info(model_id)
            if not model_info:
                raise HTTPException(
                    status_code=400, 
                    detail=f"Modèle inconnu: {model_id}. Utilisez l'endpoint /models pour voir les modèles disponibles."
                )
        
        # Envoyer le message à Claude
        result = await claude_service.send_message(
            message=request.message,
            conversation_history=request.conversation_history,
            model_id=model_id
        )
        
        return ChatResponse(
            response=result["response"],
            conversation_history=result["conversation_history"],
            token_usage=result.get("token_usage"),
            model_used=result.get("model_used")
        )
    except HTTPException:
        # Rethrow HTTP exceptions
        raise
    except Exception as e:
        # Log l'erreur ici si nécessaire
        raise HTTPException(status_code=500, detail=f"Erreur lors de la communication avec Claude: {str(e)}")

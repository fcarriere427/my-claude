"""
Modèles de données pour l'API.
Utilise Pydantic pour la validation des données.
"""
from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import datetime

class Message(BaseModel):
    """Modèle pour un message dans la conversation."""
    role: str = Field(..., description="Le rôle de l'auteur du message (user ou assistant)")
    content: str = Field(..., description="Le contenu du message")
    timestamp: Optional[datetime] = Field(default_factory=datetime.now, description="Horodatage du message")

class ChatRequest(BaseModel):
    """Modèle pour une requête de chat."""
    message: str = Field(..., description="Le message envoyé par l'utilisateur")
    conversation_history: Optional[List[Message]] = Field(default=[], description="Historique de la conversation")

class TokenUsage(BaseModel):
    """Modèle pour l'utilisation des tokens."""
    input_tokens: int = Field(..., description="Nombre de tokens en entrée")
    output_tokens: int = Field(..., description="Nombre de tokens en sortie")

class ChatResponse(BaseModel):
    """Modèle pour une réponse de chat."""
    response: str = Field(..., description="La réponse de Claude")
    conversation_history: List[Message] = Field(..., description="Historique de la conversation mise à jour")
    token_usage: Optional[TokenUsage] = Field(None, description="Utilisation des tokens pour cette requête")

class HealthCheck(BaseModel):
    """Modèle pour la vérification de santé de l'API."""
    status: str = Field("ok", description="Statut de l'API")
    version: str = Field(..., description="Version de l'API")

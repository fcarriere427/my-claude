"""
Modèles de données pour l'API.
Utilise Pydantic pour la validation des données.
"""
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field
from datetime import datetime

class Message(BaseModel):
    """Modèle pour un message dans la conversation."""
    role: str = Field(..., description="Le rôle de l'auteur du message (user ou assistant)")
    content: str = Field(..., description="Le contenu du message")
    timestamp: Optional[datetime] = Field(default_factory=datetime.now, description="Horodatage du message")
    model: Optional[str] = Field(None, description="Modèle Claude utilisé pour ce message")

class ModelPricing(BaseModel):
    """Modèle pour les tarifs d'un modèle Claude."""
    input: float = Field(..., description="Tarif en euros par million de tokens en entrée")
    output: float = Field(..., description="Tarif en euros par million de tokens en sortie")

class ModelInfo(BaseModel):
    """Modèle pour les informations d'un modèle Claude."""
    id: str = Field(..., description="Identifiant technique du modèle")
    name: str = Field(..., description="Nom convivial du modèle")
    description: str = Field(..., description="Description du modèle")
    pricing: ModelPricing = Field(..., description="Tarifs du modèle")
    current: bool = Field(True, description="Indique si le modèle est un modèle courant ou legacy")

class ChatRequest(BaseModel):
    """Modèle pour une requête de chat."""
    message: str = Field(..., description="Le message envoyé par l'utilisateur")
    conversation_history: Optional[List[Message]] = Field(default=[], description="Historique de la conversation")
    model_id: Optional[str] = Field(None, description="Identifiant du modèle Claude à utiliser")

class TokenUsage(BaseModel):
    """Modèle pour l'utilisation des tokens."""
    input_tokens: int = Field(..., description="Nombre de tokens en entrée")
    output_tokens: int = Field(..., description="Nombre de tokens en sortie")

class ChatResponse(BaseModel):
    """Modèle pour une réponse de chat."""
    response: str = Field(..., description="La réponse de Claude")
    conversation_history: List[Message] = Field(..., description="Historique de la conversation mise à jour")
    token_usage: Optional[TokenUsage] = Field(None, description="Utilisation des tokens pour cette requête")
    model_used: Optional[str] = Field(None, description="Modèle Claude utilisé pour cette réponse")

class HealthCheck(BaseModel):
    """Modèle pour la vérification de santé de l'API."""
    status: str = Field("ok", description="Statut de l'API")
    version: str = Field(..., description="Version de l'API")

class ModelsResponse(BaseModel):
    """Modèle pour la réponse de la liste des modèles disponibles."""
    models: List[ModelInfo] = Field(..., description="Liste des modèles Claude disponibles")
    usd_to_eur_rate: float = Field(..., description="Taux de conversion USD vers EUR")
    rate_updated_at: Optional[datetime] = Field(None, description="Date de dernière mise à jour du taux de change")

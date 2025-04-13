"""
Service d'intégration avec l'API Claude d'Anthropic.
Gère les appels à l'API et le formatage des messages.
"""
from typing import List, Dict, Any, Optional
import httpx
from ..config import settings
from ..api.models import Message

class ClaudeService:
    """Service pour interagir avec l'API Claude d'Anthropic."""
    
    def __init__(self):
        """Initialise le service avec la configuration."""
        self.api_key = settings.ANTHROPIC_API_KEY
        self.model = settings.CLAUDE_MODEL
        self.api_url = "https://api.anthropic.com/v1/messages"
        self.headers = {
            "x-api-key": self.api_key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json"
        }
    
    async def send_message(self, message: str, conversation_history: Optional[List[Message]] = None) -> Dict[str, Any]:
        """
        Envoie un message à Claude et récupère sa réponse.
        
        Args:
            message: Le message de l'utilisateur
            conversation_history: L'historique de la conversation
        
        Returns:
            La réponse de Claude et l'historique mis à jour
        """
        if conversation_history is None:
            conversation_history = []
        
        # Conversion de l'historique au format attendu par l'API Anthropic
        messages = []
        for msg in conversation_history:
            messages.append({
                "role": msg.role,
                "content": msg.content
            })
        
        # Ajout du nouveau message de l'utilisateur
        messages.append({
            "role": "user",
            "content": message
        })
        
        # Préparation de la requête
        payload = {
            "model": self.model,
            "messages": messages,
            "max_tokens": 1024
        }
        
        # Envoi de la requête à l'API
        async with httpx.AsyncClient() as client:
            response = await client.post(
                self.api_url,
                headers=self.headers,
                json=payload,
                timeout=30.0
            )
            
            # Vérification de la réponse
            response.raise_for_status()
            response_data = response.json()
            
            # Extraction de la réponse
            claude_response = response_data.get("content", [{}])[0].get("text", "")
            
            # Extraction des informations d'utilisation des tokens
            token_usage = None
            if "usage" in response_data:
                token_usage = {
                    "input_tokens": response_data["usage"].get("input_tokens", 0),
                    "output_tokens": response_data["usage"].get("output_tokens", 0)
                }
            
            # Mise à jour de l'historique
            conversation_history.append(Message(role="user", content=message))
            conversation_history.append(Message(role="assistant", content=claude_response))
            
            return {
                "response": claude_response,
                "conversation_history": conversation_history,
                "token_usage": token_usage
            }

# Instance du service pour utilisation globale
claude_service = ClaudeService()

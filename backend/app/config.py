"""
Configuration de l'application.
Gère les variables d'environnement et les paramètres de configuration.
"""
import os
from pydantic import BaseSettings
from typing import Optional, Dict, List

# Configuration des modèles Claude disponibles
# Les modèles seront triés par coût croissant dans la classe Settings
CLAUDE_MODELS = [
    # Modèles courants
    {
        "id": "claude-3-7-sonnet-20240219",
        "name": "Claude 3.7 Sonnet",
        "description": "Notre modèle le plus intelligent, avec capacités de raisonnement avancées",
        "pricing": {
            "input": 3.00, # Dollars par million de tokens en entrée
            "output": 15.00 # Dollars par million de tokens en sortie
        },
        "current": True
    },

    {
        "id": "claude-3-5-haiku-20240307",
        "name": "Claude 3.5 Haiku",
        "description": "Le plus rapide et économique, idéal pour les applications à volume élevé",
        "pricing": {
            "input": 0.80,  
            "output": 4.00   
        },
        "current": True
    },
    {
        "id": "claude-3-opus-20240229",
        "name": "Claude 3 Opus (Legacy)",
        "description": "Modèle puissant pour les tâches complexes (/!\ très cher)",
        "pricing": {
            "input": 15.00,
            "output": 75.00
        },
        "current": True
    },
    
    # Modèles legacy
    {
        "id": "claude-3-5-sonnet-20240620",
        "name": "Claude 3.5 Sonnet (Legacy)",
        "description": "Version précédente du modèle Sonnet",
        "pricing": {
            "input": 3.00,
            "output": 15.00
        },
        "current": False
    },
    {
        "id": "claude-3-haiku-20240307",
        "name": "Claude 3 Haiku (Legacy)",
        "description": "Version précédente du modèle Haiku",
        "pricing": {
            "input": 0.25,
            "output": 1.25
        },
        "current": False
    }
    
]

class Settings(BaseSettings):
    """Paramètres de configuration de l'application."""
    
    # Configuration de l'API Anthropic
    ANTHROPIC_API_KEY: str = os.getenv("ANTHROPIC_API_KEY", "")
    CLAUDE_MODEL: str = os.getenv("CLAUDE_MODEL", "claude-3-haiku-20240307")
    
    # Tri des modèles Claude par statut (courant d'abord) puis par coût croissant
    @property
    def CLAUDE_MODELS(self) -> List[Dict]:
        # D'abord trier par statut (courant en premier), puis par coût
        sorted_models = sorted(
            CLAUDE_MODELS, 
            key=lambda model: (
                not model.get("current", True),  # Les modèles courants en premier (False en premier dans le tri)
                model["pricing"]["input"] + model["pricing"]["output"]
            )
        )
        return sorted_models
    
    # Configuration de l'application
    APP_NAME: str = "my-claude"
    APP_VERSION: str = "0.1.0"
    APP_DESCRIPTION: str = "Interface web simple pour converser avec Claude via l'API Anthropic"
    
    # Configuration du serveur
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", "8000"))
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"
    
    # Configuration CORS
    CORS_ORIGINS: list = ["*"]
    
    class Config:
        env_file = ".env"

# Instance de configuration globale
settings = Settings()

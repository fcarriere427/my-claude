"""
Configuration de l'application.
Gère les variables d'environnement et les paramètres de configuration.
"""
import os
from pydantic import BaseSettings
from typing import Optional, Dict, List

# Configuration des modèles Claude disponibles
CLAUDE_MODELS = [
    {
        "id": "claude-3-opus-20240229",
        "name": "Claude 3 Opus",
        "description": "Modèle le plus puissant et le plus précis",
        "pricing": {
            "input": 15.00,  # Euros par million de tokens en entrée
            "output": 75.00  # Euros par million de tokens en sortie
        }
    },
    {
        "id": "claude-3-sonnet-20240229",
        "name": "Claude 3 Sonnet",
        "description": "Bon équilibre entre performance et coût",
        "pricing": {
            "input": 7.50,
            "output": 24.00
        }
    },
    {
        "id": "claude-3-haiku-20240307",
        "name": "Claude 3 Haiku",
        "description": "Le plus rapide, économique pour les tâches simples",
        "pricing": {
            "input": 0.25,
            "output": 1.25
        }
    },
    {
        "id": "claude-3-5-sonnet-20240620",
        "name": "Claude 3.5 Sonnet",
        "description": "Version améliorée de Sonnet",
        "pricing": {
            "input": 3.00,
            "output": 15.00
        }
    }
]

class Settings(BaseSettings):
    """Paramètres de configuration de l'application."""
    
    # Configuration de l'API Anthropic
    ANTHROPIC_API_KEY: str = os.getenv("ANTHROPIC_API_KEY", "")
    CLAUDE_MODEL: str = os.getenv("CLAUDE_MODEL", "claude-3-haiku-20240307")
    CLAUDE_MODELS: List[Dict] = CLAUDE_MODELS
    
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

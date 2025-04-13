"""
Configuration de l'application.
Gère les variables d'environnement et les paramètres de configuration.
"""
import os
from pydantic import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    """Paramètres de configuration de l'application."""
    
    # Configuration de l'API Anthropic
    ANTHROPIC_API_KEY: str = os.getenv("ANTHROPIC_API_KEY", "")
    CLAUDE_MODEL: str = os.getenv("CLAUDE_MODEL", "claude-3-haiku-20240307")
    
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

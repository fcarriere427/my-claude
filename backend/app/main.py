"""
Point d'entrée principal de l'application FastAPI.
Configure et démarre le serveur.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from .config import settings
from .api.routes import router as api_router

# Création de l'application FastAPI
app = FastAPI(
    title=settings.APP_NAME,
    description=settings.APP_DESCRIPTION,
    version=settings.APP_VERSION,
)

# Configuration CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclusion des routes API
app.include_router(api_router, prefix="/api")

@app.get("/")
async def root():
    """Route racine de l'API."""
    return {
        "message": f"Bienvenue sur l'API {settings.APP_NAME}",
        "version": settings.APP_VERSION,
        "docs_url": "/docs"
    }

if __name__ == "__main__":
    """Démarrage du serveur en mode développement."""
    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG
    )

"""
Service de conversion de devises.
Gère la conversion USD -> EUR et la mise à jour quotidienne du taux.
"""
import httpx
from datetime import datetime, timedelta
import logging
from ..config import USD_TO_EUR_RATE, LAST_RATE_UPDATE

# Configuration du logger
logger = logging.getLogger(__name__)

class CurrencyService:
    """Service pour la conversion de devises."""
    
    def __init__(self):
        """Initialise le service avec les valeurs par défaut."""
        self.usd_to_eur_rate = USD_TO_EUR_RATE
        self.last_update = LAST_RATE_UPDATE
    
    async def get_exchange_rate(self, force_update=False):
        """
        Récupère le taux de change USD -> EUR.
        Le taux n'est mis à jour qu'une fois par jour.
        
        Args:
            force_update: Forcer la mise à jour même si le taux a déjà été mis à jour aujourd'hui
            
        Returns:
            Le taux de conversion USD -> EUR
        """
        now = datetime.now()
        
        # Vérifier si une mise à jour est nécessaire
        if (self.last_update is None or 
            now - self.last_update > timedelta(days=1) or 
            force_update):
            
            try:
                # Tenter de récupérer le taux de change depuis une API externe
                # Note: Nous utilisons l'API de la BCE qui est publique et gratuite
                async with httpx.AsyncClient() as client:
                    response = await client.get(
                        "https://api.frankfurter.app/latest?from=USD&to=EUR",
                        timeout=5.0
                    )
                    
                    if response.status_code == 200:
                        data = response.json()
                        if "rates" in data and "EUR" in data["rates"]:
                            # Mettre à jour le taux et l'horodatage
                            self.usd_to_eur_rate = data["rates"]["EUR"]
                            self.last_update = now
                            logger.info(f"Taux de change USD/EUR mis à jour: {self.usd_to_eur_rate}")
                        else:
                            logger.warning("Format de réponse API de change inattendu")
                    else:
                        logger.warning(f"Échec de la mise à jour du taux de change: {response.status_code}")
            
            except Exception as e:
                logger.error(f"Erreur lors de la mise à jour du taux de change: {str(e)}")
                # Continuer avec le taux existant
        
        return self.usd_to_eur_rate
    
    async def usd_to_eur(self, amount_usd):
        """
        Convertit un montant de USD en EUR.
        
        Args:
            amount_usd: Montant en USD
            
        Returns:
            Montant converti en EUR
        """
        rate = await self.get_exchange_rate()
        return amount_usd * rate

# Instance du service pour utilisation globale
currency_service = CurrencyService()

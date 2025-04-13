/**
 * Service d'API pour communiquer avec le backend
 */
import axios from 'axios';

// Création d'une instance axios avec la configuration de base
const api = axios.create({
  baseURL: '/api',  // Utilise le proxy configuré dans vue.config.js
  timeout: 30000, // 30 secondes
  headers: {
    'Content-Type': 'application/json',
  },
});

// Variables pour stocker les modèles et leurs tarifs
let cachedModels = null;
let usdToEurRate = 0.913; // Taux par défaut (13 avril 2025)

/**
 * Service pour interagir avec l'API backend
 */
export default {
  /**
   * Vérifier la santé de l'API
   * @returns {Promise} Statut de l'API
   */
  checkHealth() {
    return api.get('/health');
  },

  /**
   * Récupérer la liste des modèles disponibles
   * @returns {Promise} Liste des modèles avec leurs informations
   */
  async getModels() {
    if (cachedModels) {
      console.log('Utilisation du cache de modèles');
      return { data: cachedModels };
    }
    
    console.log('Récupération des modèles depuis l\'API...');
    const response = await api.get('/models');
    console.log('Réponse API des modèles:', response.data);
    
    // Stocker le taux de change dans la variable globale
    if (response.data && response.data.usd_to_eur_rate) {
      usdToEurRate = response.data.usd_to_eur_rate;
      console.log(`Taux de change USD/EUR: ${usdToEurRate}`);
    }
    
    cachedModels = response.data;
    return response;
  },
  
  /**
   * Récupérer le taux de conversion USD/EUR actuel
   * @returns {number} Taux de conversion
   */
  getUsdToEurRate() {
    return usdToEurRate;
  },

  /**
   * Envoyer un message à Claude
   * @param {string} message - Message de l'utilisateur
   * @param {Array} conversationHistory - Historique de la conversation
   * @param {string} modelId - ID du modèle Claude à utiliser
   * @returns {Promise} Réponse et historique mis à jour
   */
  sendMessage(message, conversationHistory = [], modelId = null) {
    console.log("Envoi de requête avec modelId:", modelId);
    console.log("Type de modelId:", typeof modelId);
    return api.post('/chat', {
      message,
      conversation_history: conversationHistory,
      model_id: modelId
    });
  },
};

/**
 * Fonction utilitaire pour calculer le coût en euros en fonction du modèle
 * @param {number} inputTokens - Nombre de tokens en entrée
 * @param {number} outputTokens - Nombre de tokens en sortie
 * @param {Object} modelPricing - Tarifs du modèle (input/output)
 * @returns {Object} Coûts calculés en euros
 */
export const calculateCost = (inputTokens, outputTokens, modelPricing) => {
  // Utilisation des tarifs par défaut si non fournis
  const pricing = modelPricing || {
    input: 0.80,  // Prix par défaut pour Claude 3.5 Haiku (en dollars)
    output: 4.00
  };
  
  // Calculer le coût en dollars
  const inputCostUsd = (inputTokens / 1000000) * pricing.input;
  const outputCostUsd = (outputTokens / 1000000) * pricing.output;
  const totalCostUsd = inputCostUsd + outputCostUsd;
  
  // Convertir les coûts en euros
  const inputCostEur = inputCostUsd * usdToEurRate;
  const outputCostEur = outputCostUsd * usdToEurRate;
  const totalCostEur = totalCostUsd * usdToEurRate;
  
  return {
    inputCost: parseFloat(inputCostEur.toFixed(6)),
    outputCost: parseFloat(outputCostEur.toFixed(6)),
    totalCost: parseFloat(totalCostEur.toFixed(6))
  };
};

/**
 * Fonction utilitaire pour obtenir les tarifs d'un modèle par son ID
 * @param {string} modelId - ID du modèle
 * @param {Array} models - Liste des modèles disponibles
 * @returns {Object} Tarifs du modèle
 */
export const getModelPricing = async (modelId) => {
  if (!modelId) {
    // Tarifs par défaut pour Claude 3 Haiku
    return {
      input: 0.25,
      output: 1.25
    };
  }
  
  try {
    // Récupérer la liste des modèles si pas encore chargée
    const modelsResponse = await api.getModels();
    const models = modelsResponse.data.models;
    
    // Rechercher le modèle demandé
    const model = models.find(m => m.id === modelId);
    if (model) {
      return model.pricing;
    }
    
    // Modèle non trouvé, utiliser les tarifs par défaut
    return {
      input: 0.25,
      output: 1.25
    };
  } catch (error) {
    console.error("Erreur lors de la récupération des tarifs du modèle:", error);
    // En cas d'erreur, utiliser les tarifs par défaut
    return {
      input: 0.25,
      output: 1.25
    };
  }
};

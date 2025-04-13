/**
 * Service d'API pour communiquer avec le backend
 */
import axios from 'axios';

// Configuration des prix des tokens (en euros par million de tokens)
export const TOKEN_PRICING = {
  input: 3, // 3€ par million de tokens en entrée
  output: 15 // 15€ par million de tokens en sortie
};

// Fonction utilitaire pour calculer le coût en euros
export const calculateCost = (inputTokens, outputTokens) => {
  const inputCost = (inputTokens / 1000000) * TOKEN_PRICING.input;
  const outputCost = (outputTokens / 1000000) * TOKEN_PRICING.output;
  return {
    inputCost: parseFloat(inputCost.toFixed(6)),
    outputCost: parseFloat(outputCost.toFixed(6)),
    totalCost: parseFloat((inputCost + outputCost).toFixed(6))
  };
};

// Création d'une instance axios avec la configuration de base
const api = axios.create({
  baseURL: '/api',  // Utilise le proxy configuré dans vue.config.js
  timeout: 30000, // 30 secondes
  headers: {
    'Content-Type': 'application/json',
  },
});

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
   * Envoyer un message à Claude
   * @param {string} message - Message de l'utilisateur
   * @param {Array} conversationHistory - Historique de la conversation
   * @returns {Promise} Réponse et historique mis à jour
   */
  sendMessage(message, conversationHistory = []) {
    return api.post('/chat', {
      message,
      conversation_history: conversationHistory,
    });
  },
};

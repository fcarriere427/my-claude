/**
 * Service d'API pour communiquer avec le backend
 */
import axios from 'axios';

// Création d'une instance axios avec la configuration de base
const api = axios.create({
  baseURL: process.env.VUE_APP_API_URL || 'http://localhost:8000/api',
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

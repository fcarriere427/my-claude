<template>
  <div class="app">
    <header>
      <h1>my-claude</h1>
      <div v-if="totalTokenUsage.input_tokens > 0 || totalTokenUsage.output_tokens > 0" class="token-counter">
        <div class="token-counter-item">
          <span class="token-counter-label">Total Tokens: </span>
          <span class="token-counter-value">{{ totalTokenUsage.input_tokens + totalTokenUsage.output_tokens }}</span>
        </div>
        <div class="token-counter-item">
          <span class="token-counter-label">Entrée: </span>
          <span class="token-counter-value">{{ totalTokenUsage.input_tokens }}</span>
        </div>
        <div class="token-counter-item">
          <span class="token-counter-label">Sortie: </span>
          <span class="token-counter-value">{{ totalTokenUsage.output_tokens }}</span>
        </div>
      </div>
      <div v-if="totalCost.totalCost > 0" class="cost-counter">
        <div class="cost-counter-item">
          <span class="cost-counter-label">Coût total: </span>
          <span class="cost-counter-value">{{ totalCost.totalCost.toFixed(4) }}€</span>
        </div>
        <div class="cost-counter-item">
          <span class="cost-counter-label">Entrée: </span>
          <span class="cost-counter-value">{{ totalCost.inputCost.toFixed(4) }}€</span>
        </div>
        <div class="cost-counter-item">
          <span class="cost-counter-label">Sortie: </span>
          <span class="cost-counter-value">{{ totalCost.outputCost.toFixed(4) }}€</span>
        </div>
      </div>
    </header>
    <main>
      <div class="toolbar">
        <ModelSelector 
          :isLoading="isLoading" 
          @model-change="handleModelChange"
          ref="modelSelector"
        />
      </div>
      <ChatWindow :messages="messages" :isLoading="isLoading" />
      <MessageInput :isLoading="isLoading" @send-message="sendMessage" />
    </main>
    <footer>
      <p>Powered by Anthropic Claude API</p>
    </footer>
  </div>
</template>

<script>
import ChatWindow from './components/ChatWindow.vue';
import MessageInput from './components/MessageInput.vue';
import ModelSelector from './components/ModelSelector.vue';
import api, { calculateCost } from './services/api';

export default {
  name: 'App',
  components: {
    ChatWindow,
    MessageInput,
    ModelSelector
  },
  data() {
    return {
      messages: [],
      isLoading: false,
      totalTokenUsage: {
        input_tokens: 0,
        output_tokens: 0
      },
      totalCost: {
        inputCost: 0,
        outputCost: 0,
        totalCost: 0
      },
      selectedModel: null,
      models: []
    };
  },
  mounted() {
    // Exposer l'API pour les composants enfants
    this.$api = api;
    
    // Vérifier la connexion à l'API au démarrage
    api.checkHealth()
      .then(response => {
        console.log('API connectée:', response.data);
      })
      .catch(error => {
        console.error('Erreur de connexion à l\'API:', error);
        alert('Impossible de se connecter à l\'API. Veuillez vérifier que le backend est en cours d\'exécution.');
      });
  },
  methods: {
    handleModelChange(modelId, modelData) {
      this.selectedModel = modelData;
      console.log('Modèle sélectionné:', modelData);
    },
    
    async sendMessage(message) {
      // Ajouter le message de l'utilisateur à la conversation
      this.messages.push({
        role: 'user',
        content: message
      });
      
      // Indiquer le chargement
      this.isLoading = true;
      
      try {
        // Récupérer l'ID du modèle sélectionné
        const modelId = this.selectedModel ? this.selectedModel.id : null;
        
        // Envoyer la requête à l'API avec le modèle sélectionné
        const response = await api.sendMessage(message, this.messages, modelId);
        
        // Mettre à jour l'historique des messages avec les informations de coût
        const updatedHistory = response.data.conversation_history;
        
        // Récupérer le modèle utilisé
        const modelUsed = response.data.model_used;
        
        // Ajouter les informations de token_usage au dernier message assistant
        if (response.data.token_usage) {
          const lastAssistantMessage = updatedHistory.filter(msg => msg.role === 'assistant').pop();
          if (lastAssistantMessage) {
            lastAssistantMessage.token_usage = response.data.token_usage;
            
            // Récupérer les tarifs du modèle utilisé
            const modelPricing = this.selectedModel ? this.selectedModel.pricing : null;
            
            // Calculer le coût en euros
            const messageCost = calculateCost(
              response.data.token_usage.input_tokens,
              response.data.token_usage.output_tokens,
              modelPricing
            );
            
            lastAssistantMessage.cost = messageCost;
            lastAssistantMessage.model = modelUsed;
            
            // Mettre à jour le compteur total
            this.totalTokenUsage.input_tokens += response.data.token_usage.input_tokens;
            this.totalTokenUsage.output_tokens += response.data.token_usage.output_tokens;
            
            // Mettre à jour le coût total
            this.totalCost.inputCost += messageCost.inputCost;
            this.totalCost.outputCost += messageCost.outputCost;
            this.totalCost.totalCost += messageCost.totalCost;
          }
        }
        
        this.messages = updatedHistory;
      } catch (error) {
        console.error('Erreur lors de l\'envoi du message:', error);
        
        // Ajouter un message d'erreur à la conversation
        this.messages.push({
          role: 'assistant',
          content: 'Désolé, une erreur s\'est produite lors de la communication avec Claude. Veuillez réessayer.'
        });
      } finally {
        // Désactiver l'indicateur de chargement
        this.isLoading = false;
      }
    }
  }
};
</script>

<style>
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  line-height: 1.6;
  color: #333;
  background-color: #f8f9fa;
}

.app {
  display: flex;
  flex-direction: column;
  height: 100vh;
  max-width: 1200px;
  margin: 0 auto;
  background-color: white;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

header {
  background-color: #4a56e2;
  color: white;
  padding: 1rem;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.token-counter, .cost-counter {
  margin-top: 0.5rem;
  font-size: 0.8rem;
  background-color: rgba(255, 255, 255, 0.2);
  border-radius: 8px;
  padding: 0.5rem 1rem;
  display: flex;
  gap: 1rem;
}

.cost-counter {
  margin-top: 0.25rem;
  background-color: rgba(255, 255, 255, 0.15);
}

.token-counter-item, .cost-counter-item {
  display: flex;
  align-items: center;
}

.token-counter-label, .cost-counter-label {
  margin-right: 0.3rem;
  opacity: 0.8;
}

.token-counter-value, .cost-counter-value {
  font-weight: bold;
}

main {
  flex: 1;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.toolbar {
  padding: 0.5rem 1rem;
  border-bottom: 1px solid #eee;
  background-color: #f8f9fa;
}

footer {
  padding: 0.5rem;
  text-align: center;
  font-size: 0.8rem;
  color: #666;
  border-top: 1px solid #eee;
}
</style>

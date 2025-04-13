<template>
  <div class="app">
    <header>
      <h1>Claude Rasp</h1>
    </header>
    <main>
      <ChatWindow :messages="messages" :isLoading="isLoading" />
      <MessageInput :isLoading="isLoading" @send-message="sendMessage" />
    </main>
    <footer>
      <p>Powered by Claude API</p>
    </footer>
  </div>
</template>

<script>
import ChatWindow from './components/ChatWindow.vue';
import MessageInput from './components/MessageInput.vue';
import api from './services/api';

export default {
  name: 'App',
  components: {
    ChatWindow,
    MessageInput
  },
  data() {
    return {
      messages: [],
      isLoading: false
    };
  },
  mounted() {
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
    async sendMessage(message) {
      // Ajouter le message de l'utilisateur à la conversation
      this.messages.push({
        role: 'user',
        content: message
      });
      
      // Indiquer le chargement
      this.isLoading = true;
      
      try {
        // Envoyer la requête à l'API
        const response = await api.sendMessage(message, this.messages);
        
        // Mettre à jour l'historique des messages
        this.messages = response.data.conversation_history;
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
}

main {
  flex: 1;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

footer {
  padding: 0.5rem;
  text-align: center;
  font-size: 0.8rem;
  color: #666;
  border-top: 1px solid #eee;
}
</style>

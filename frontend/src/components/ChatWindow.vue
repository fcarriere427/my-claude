<template>
  <div class="chat-window">
    <div class="messages" ref="messagesContainer">
      <div v-if="messages.length === 0" class="empty-state">
        <p>👋 Bonjour ! Je suis my-claude : comment puis-je vous aider aujourd'hui ?</p>
      </div>
      <div
        v-for="(message, index) in messages"
        :key="index"
        :class="['message', message.role]"
      >
        <div class="message-header">
          <strong>{{ message.role === 'user' ? 'Vous' : 'Claude' }}</strong>
        </div>
        <div class="message-content" v-html="formatMessage(message.content)"></div>
        <div v-if="message.role === 'assistant'" class="message-footer">
          <span v-if="message.model" class="model-badge">
            {{ formatModelName(message.model) }}
          </span>
          <span v-if="message.token_usage" class="token-usage">
            Tokens: {{ message.token_usage.input_tokens }} en entrée / {{ message.token_usage.output_tokens }} en sortie
          </span>
          <span v-if="message.cost" class="cost-usage">
            Coût: {{ message.cost.totalCost.toFixed(4) }}€
          </span>
        </div>
      </div>
      <div v-if="isLoading" class="message assistant loading">
        <div class="message-header">
          <strong>Claude</strong>
        </div>
        <div class="message-content">
          <div class="typing-indicator">
            <span></span>
            <span></span>
            <span></span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { marked } from 'marked';

export default {
  name: 'ChatWindow',
  props: {
    messages: {
      type: Array,
      default: () => []
    },
    isLoading: {
      type: Boolean,
      default: false
    }
  },
  watch: {
    messages() {
      this.$nextTick(() => {
        this.scrollToBottom();
      });
    },
    isLoading() {
      this.$nextTick(() => {
        this.scrollToBottom();
      });
    }
  },
  mounted() {
    this.scrollToBottom();
  },
  methods: {
    formatMessage(content) {
      // Convertir le Markdown en HTML
      return marked(content);
    },
    scrollToBottom() {
      const container = this.$refs.messagesContainer;
      if (container) {
        container.scrollTop = container.scrollHeight;
      }
    },
    formatModelName(modelId) {
      // Extraire le nom du modèle à partir de l'ID
      // Ex: "claude-3-haiku-20240307" -> "Claude 3 Haiku"
      if (!modelId) return '';
      
      const parts = modelId.split('-');
      if (parts.length < 3) return modelId;
      
      // Formater la première partie (claude -> Claude)
      let name = parts[0].charAt(0).toUpperCase() + parts[0].slice(1);
      
      // Ajouter la version (3)
      name += ' ' + parts[1];
      
      // Ajouter le nom du modèle (haiku/opus/sonnet)
      name += ' ' + parts[2].charAt(0).toUpperCase() + parts[2].slice(1);
      
      // Ajouter le numéro de version si disponible (3.5)
      if (parts[1].includes('.')) {
        name = parts[0].charAt(0).toUpperCase() + parts[0].slice(1) + ' ' + parts[1] + ' ' + parts[2].charAt(0).toUpperCase() + parts[2].slice(1);
      }
      
      return name;
    }
  }
}
</script>

<style scoped>
.chat-window {
  flex: 1;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.messages {
  flex: 1;
  overflow-y: auto;
  padding: 1rem;
}

.message {
  margin-bottom: 1rem;
  padding: 1rem;
  border-radius: 8px;
  max-width: 80%;
}

.message.user {
  align-self: flex-end;
  background-color: #e6f7ff;
  margin-left: auto;
}

.message.assistant {
  align-self: flex-start;
  background-color: #f0f0f0;
}

.message-header {
  margin-bottom: 0.5rem;
  color: #555;
}

.message-content {
  white-space: pre-wrap;
  word-break: break-word;
}

.message-content >>> p {
  margin-top: 0.5rem;
  margin-bottom: 0.5rem;
}

.message-content >>> pre {
  background-color: #f5f5f5;
  padding: 0.5rem;
  border-radius: 4px;
  overflow-x: auto;
}

.message-content >>> code {
  background-color: #f5f5f5;
  padding: 0.1rem 0.3rem;
  border-radius: 3px;
  font-family: monospace;
}

.message-footer {
  margin-top: 0.5rem;
  font-size: 0.8rem;
  color: #888;
  text-align: right;
  display: flex;
  justify-content: flex-end;
  gap: 10px;
  flex-wrap: wrap;
}

.token-usage, .cost-usage, .model-badge {
  background-color: #f0f0f0;
  padding: 2px 6px;
  border-radius: 4px;
}

.cost-usage {
  background-color: #f0f8ff;
}

.model-badge {
  background-color: #e6f7ff;
  color: #0066cc;
  font-weight: 500;
}

.empty-state {
  text-align: center;
  color: #888;
  margin: 2rem 0;
}

.typing-indicator {
  display: flex;
  align-items: center;
  column-gap: 0.5rem;
}

.typing-indicator span {
  height: 8px;
  width: 8px;
  float: left;
  margin: 0 1px;
  background-color: #9E9EA1;
  display: block;
  border-radius: 50%;
  opacity: 0.4;
}

.typing-indicator span:nth-of-type(1) {
  animation: 1s blink infinite 0.3333s;
}

.typing-indicator span:nth-of-type(2) {
  animation: 1s blink infinite 0.6666s;
}

.typing-indicator span:nth-of-type(3) {
  animation: 1s blink infinite 0.9999s;
}

@keyframes blink {
  50% {
    opacity: 1;
  }
}
</style>

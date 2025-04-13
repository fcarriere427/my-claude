<template>
  <div class="message-input">
    <form @submit.prevent="sendMessage">
      <textarea
        v-model="message"
        placeholder="Tapez votre message ici..."
        @keydown.ctrl.enter="sendMessage"
        :disabled="isLoading"
      ></textarea>
      <button type="submit" :disabled="isLoading || !message.trim()">
        {{ isLoading ? 'Envoi...' : 'Envoyer' }}
      </button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'MessageInput',
  props: {
    isLoading: {
      type: Boolean,
      default: false
    }
  },
  data() {
    return {
      message: ''
    }
  },
  methods: {
    sendMessage() {
      if (this.message.trim() && !this.isLoading) {
        this.$emit('send-message', this.message);
        this.message = '';
      }
    }
  }
}
</script>

<style scoped>
.message-input {
  padding: 1rem;
  border-top: 1px solid #ddd;
  background-color: #f9f9f9;
}

form {
  display: flex;
  flex-direction: column;
}

textarea {
  width: 100%;
  min-height: 100px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  resize: vertical;
  font-family: inherit;
  margin-bottom: 10px;
}

button {
  align-self: flex-end;
  padding: 8px 16px;
  background-color: #4a56e2;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-weight: bold;
}

button:hover:not(:disabled) {
  background-color: #3a46c2;
}

button:disabled {
  background-color: #a0a0a0;
  cursor: not-allowed;
}
</style>

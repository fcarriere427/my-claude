<template>
  <div class="model-selector">
    <label for="model-select">Modèle:</label>
    <select 
      id="model-select" 
      v-model="selectedModelId" 
      @change="handleModelChange"
      :disabled="isLoading"
    >
      <option v-for="model in models" :key="model.id" :value="model.id">
        {{ model.name }} - {{ formatCost(model.pricing) }}
      </option>
    </select>
    <div class="model-description" v-if="selectedModel">
      {{ selectedModel.description }}
    </div>
  </div>
</template>

<script>
export default {
  name: 'ModelSelector',
  props: {
    isLoading: {
      type: Boolean,
      default: false
    }
  },
  data() {
    return {
      models: [],
      selectedModelId: null,
      error: null
    };
  },
  computed: {
    selectedModel() {
      if (!this.selectedModelId) return null;
      return this.models.find(model => model.id === this.selectedModelId);
    }
  },
  methods: {
    async loadModels() {
      try {
        // Remplacer par votre service API pour charger les modèles
        const response = await this.$api.getModels();
        this.models = response.data.models;
        
        // Sélectionner le premier modèle par défaut si aucun n'est sélectionné
        if (!this.selectedModelId && this.models.length > 0) {
          this.selectedModelId = this.models[0].id;
          this.handleModelChange();
        }
      } catch (error) {
        console.error('Erreur lors du chargement des modèles:', error);
        this.error = 'Impossible de charger la liste des modèles.';
      }
    },
    handleModelChange() {
      this.$emit('model-change', this.selectedModelId, this.selectedModel);
    },
    formatCost(pricing) {
      return `${pricing.input}€/1M tokens entrée, ${pricing.output}€/1M tokens sortie`;
    }
  },
  mounted() {
    this.loadModels();
  }
}
</script>

<style scoped>
.model-selector {
  margin: 0.5rem 0;
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

label {
  font-weight: 600;
  margin-right: 0.5rem;
  font-size: 0.9rem;
  color: #555;
}

select {
  padding: 0.4rem 0.6rem;
  border-radius: 4px;
  border: 1px solid #ccc;
  background-color: white;
  font-size: 0.9rem;
  width: 100%;
  cursor: pointer;
}

select:focus {
  outline: none;
  border-color: #4a56e2;
  box-shadow: 0 0 0 1px rgba(74, 86, 226, 0.3);
}

select:disabled {
  background-color: #f1f1f1;
  cursor: not-allowed;
}

.model-description {
  font-size: 0.8rem;
  color: #666;
  margin-top: 0.25rem;
  font-style: italic;
}
</style>

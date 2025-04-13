<template>
  <div class="model-selector">
    <label for="model-select">Modèle:</label>
    <select 
      id="model-select" 
      v-model="selectedModelId" 
      @change="handleModelChange"
      :disabled="isLoading"
    >
      <option v-if="!models.length" value="">Chargement des modèles...</option>
      <option 
        v-for="model in sortedModels" 
        :key="model.id" 
        :value="model.id"
      >
        {{ model.name }} - {{ formatCost(model.pricing) }}
      </option>
    </select>
    <div class="error-message" v-if="error">
      {{ error }}
    </div>
    <div class="model-description" v-if="selectedModel">
      {{ selectedModel.description }}
    </div>
    <!-- Affichage de debugging -->
    <div class="debug-info" v-if="debug">
      Nb modèles chargés: {{ models.length }}<br>
      Nb modèles triés: {{ sortedModels.length }}
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
      error: null,
      debug: true // Activer temporairement pour le débogage
    };
  },
  computed: {
    selectedModel() {
      if (!this.selectedModelId) return null;
      return this.models.find(model => model.id === this.selectedModelId);
    },
    sortedModels() {
      if (!this.models || this.models.length === 0) {
        return [];
      }
      // Trier d'abord les modèles courants par coût croissant, puis les modèles legacy par coût croissant
      const currentModels = this.models
        .filter(model => model.current === true)
        .sort((a, b) => (a.pricing.input + a.pricing.output) - (b.pricing.input + b.pricing.output));
      
      const legacyModels = this.models
        .filter(model => !model.current)
        .sort((a, b) => (a.pricing.input + a.pricing.output) - (b.pricing.input + b.pricing.output));
      
      // Concaténer les deux listes triées
      return [...currentModels, ...legacyModels];
    }
  },
  methods: {
    async loadModels() {
      try {
        // Chargement des modèles depuis l'API
        const response = await this.$api.getModels();
        console.log('Modèles chargés depuis l\'API:', response.data);
        
        if (response.data && response.data.models) {
          this.models = response.data.models;
          console.log('Nombre de modèles chargés:', this.models.length);
          
          // Sélectionner le premier modèle par défaut si aucun n'est sélectionné
          if (!this.selectedModelId && this.models.length > 0) {
            this.selectedModelId = this.models[0].id;
            this.handleModelChange();
          }
        } else {
          console.error('Format de données incorrect:', response.data);
          this.error = 'Format de données incorrect lors du chargement des modèles.';
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
      const inputCost = pricing.input.toFixed(2);
      const outputCost = pricing.output.toFixed(2);
      return `$${inputCost}/1M tokens entrée, $${outputCost}/1M tokens sortie`;
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

.error-message {
  color: #e74c3c;
  font-size: 0.8rem;
  margin-top: 0.25rem;
}

.debug-info {
  margin-top: 0.5rem;
  padding: 0.5rem;
  background-color: #f8f9fa;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 0.75rem;
  font-family: monospace;
  color: #555;
}
</style>
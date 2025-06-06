# Claude Rasp

Une interface web simple pour converser avec Claude via l'API Anthropic, déployée sur un Raspberry Pi.

## Aperçu du projet

Claude Rasp est un MVP (Minimum Viable Product) conçu pour permettre une conversation avec Claude, un modèle d'IA développé par Anthropic, via une interface web légère. L'application est optimisée pour fonctionner sur un Raspberry Pi avec des ressources limitées.

## Fonctionnalités

- Interface de conversation simple et intuitive
- Conservation de l'historique de la conversation courante
- Support de la mise en forme Markdown dans les réponses
- Indicateur de chargement pendant le traitement des requêtes
- Affichage du coût de chaque message (nombre de tokens en entrée/sortie)
- Sélection du modèle Claude à utiliser (Claude 3 Opus, Sonnet, Haiku, etc.)
- Calcul des coûts adaptés selon le modèle sélectionné
- Tri des modèles par statut (courants/legacy) et par coût croissant

## Architecture technique

### Backend
- Framework: FastAPI (Python)
- Serveur WSGI: Gunicorn
- Proxy inverse: Nginx

### Frontend
- Framework: Vue.js
- Bibliothèques: Axios (requêtes HTTP), Marked (rendu Markdown)

## Prérequis

- Python 3.7+
- Node.js 14+
- Npm
- Une clé API Anthropic valide

## Configuration

### Backend

1. Naviguer vers le dossier backend
   ```bash
   cd backend
   ```

2. Installer les dépendances
   ```bash
   pip install -r requirements.txt
   ```

3. Créer un fichier `.env` à partir du modèle
   ```bash
   cp .env.example .env
   ```

4. Modifier le fichier `.env` avec votre clé API Anthropic

### Frontend

1. Naviguer vers le dossier frontend
   ```bash
   cd frontend
   ```

2. Installer les dépendances
   ```bash
   npm install
   ```

3. Créer un fichier `.env` à partir du modèle
   ```bash
   cp .env.example .env
   ```

4. Modifier le fichier `.env` avec l'URL de l'API backend

## Développement

### Backend

```bash
cd backend
python -m app.main
```

L'API sera accessible à l'adresse http://localhost:8000.

### Frontend

```bash
cd frontend
npm run serve
```

L'application sera accessible à l'adresse http://localhost:8080.

## Déploiement sur Raspberry Pi

1. Cloner le dépôt sur votre Raspberry Pi
   ```bash
   git clone [URL_DU_REPO] claude-rasp
   cd claude-rasp
   ```

2. Déployer l'application complète
   ```bash
   chmod +x deploy.sh
   ./deploy.sh
   ```

   Ce script va :
   - Mettre à jour le dépôt Git
   - Construire et déployer le frontend
   - Installer les dépendances backend si nécessaire
   - Redémarrer le service backend

3. Accéder à l'application à l'adresse http://claude.letsq.xyz

## Structure du projet

```
claude-rasp/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py           # Point d'entrée FastAPI
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   ├── routes.py     # Endpoints API
│   │   │   └── models.py     # Modèles Pydantic
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   └── claude.py     # Logique d'intégration avec API Claude
│   │   └── config.py         # Configuration (API key, modèles, etc.)
│   ├── requirements.txt
│   └── deploy.sh             # Script de déploiement backend
├── frontend/
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── App.vue           # Composant principal
│   │   ├── main.js           # Point d'entrée Vue
│   │   ├── components/
│   │   │   ├── ChatWindow.vue
│   │   │   ├── MessageInput.vue
│   │   │   └── ModelSelector.vue  # Sélection du modèle Claude
│   │   └── services/
│   │       └── api.js        # Appels au backend
│   ├── package.json
│   └── deploy.sh             # Script de déploiement frontend
├── deploy.sh                 # Script de déploiement global
└── README.md
```

## Modèles Claude disponibles

L'application supporte les modèles suivants avec leurs tarifs associés (en dollars par million de tokens) :

### Modèles courants

| Modèle | Prix entrée | Prix sortie | Description |
|--------|-------------|-------------|-------------|
| Claude 3.5 Haiku | $0.80 | $4.00 | Le plus rapide et économique, idéal pour les applications à volume élevé |
| Claude 3.5 Sonnet | $3.00 | $15.00 | Puissant et polyvalent, recommandé pour la plupart des cas d'usage |
| Claude 3.7 Sonnet | $3.00 | $15.00 | Notre modèle le plus intelligent, avec capacités de raisonnement avancées |
| Claude 3 Opus | $15.00 | $75.00 | Modèle très puissant pour les tâches complexes (/!\ coût élevé) |

### Modèles legacy

| Modèle | Prix entrée | Prix sortie | Description |
|--------|-------------|-------------|-------------|
| Claude 3 Haiku (Legacy) | $0.25 | $1.25 | Version précédente du modèle Haiku |
| Claude 3.5 Sonnet (Legacy) | $3.00 | $15.00 | Version précédente du modèle Sonnet |

## Résolution des problèmes courants

### Erreur de connexion à l'API

Si vous rencontrez l'erreur "Erreur lors de la communication avec Claude", vérifiez les points suivants :
1. Votre clé API Anthropic est correctement configurée dans le fichier `.env` du backend
2. Le service backend est bien démarré et accessible
3. Vous avez une connexion Internet fonctionnelle

### Pas de modèles dans le menu déroulant

Si le menu déroulant des modèles est vide :
1. Vérifiez que le backend répond correctement à l'endpoint `/models`
2. Consultez les logs du serveur backend pour identifier d'éventuelles erreurs
3. Actualisez la page pour recharger les données

## Améliorations futures possibles

- Sauvegarde des conversations
- Authentification utilisateur
- Paramètres de conversation configurables
- Interface responsive pour mobile
- Statistiques d'utilisation par modèle
- Sauvegarde du modèle préféré pour les futures sessions
- Thème sombre/clair
- Export des conversations

## Journal des correctifs

### 13 avril 2025
- Mise à jour de la liste des modèles Claude disponibles avec tous les modèles dans une seule liste
- Mise à jour des tarifs exacts selon la tarification officielle d'Anthropic (en dollars)
- Simplification de l'interface du sélecteur de modèles pour une meilleure visibilité des options
- Tri des modèles Claude par statut (courants d'abord) puis par coût croissant pour faciliter la sélection
- Amélioration du formatage des coûts dans l'interface utilisateur pour une meilleure lisibilité
- Correction du problème de duplication des messages utilisateur dans l'interface chat
- Correction du script de déploiement qui ne se terminait pas correctement
- Ajout d'un script de déploiement global avec gestion des erreurs
- Amélioration de la gestion des erreurs dans l'interface utilisateur

## Licence

[MIT License](LICENSE)

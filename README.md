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

2. Déployer le backend
   ```bash
   cd backend
   ./deploy.sh
   ```

3. Déployer le frontend
   ```bash
   cd frontend
   ./deploy.sh
   ```

4. Accéder à l'application à l'adresse http://claude.letsq.xyz

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
│   └── deploy.sh
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
│   └── deploy.sh
└── README.md
```

## Modèles Claude disponibles

L'application supporte les modèles suivants avec leurs tarifs associés (en euros par million de tokens) :

| Modèle | Prix entrée | Prix sortie | Description |
|--------|-------------|-------------|-------------|
| Claude 3 Opus | 15.00€ | 75.00€ | Modèle le plus puissant et le plus précis |
| Claude 3 Sonnet | 7.50€ | 24.00€ | Bon équilibre entre performance et coût |
| Claude 3 Haiku | 0.25€ | 1.25€ | Le plus rapide, économique pour les tâches simples |
| Claude 3.5 Sonnet | 3.00€ | 15.00€ | Version améliorée de Sonnet |

## Améliorations futures possibles

- Sauvegarde des conversations
- Authentification utilisateur
- Paramètres de conversation configurables
- Interface responsive pour mobile
- Statistiques d'utilisation par modèle
- Sauvegarde du modèle préféré pour les futures sessions

## Journal des correctifs

### 13 avril 2025
- Correction du problème de duplication des messages utilisateur dans l'interface chat en évitant d'ajouter deux fois le même message dans l'historique du backend

## Licence

[MIT License](LICENSE)

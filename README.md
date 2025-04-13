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
│   │   └── config.py         # Configuration (API key, etc.)
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
│   │   │   └── MessageInput.vue
│   │   └── services/
│   │       └── api.js        # Appels au backend
│   ├── package.json
│   └── deploy.sh
└── README.md
```

## Améliorations futures possibles

- Sauvegarde des conversations
- Authentification utilisateur
- Paramètres de conversation configurables
- Support de différents modèles Claude
- Interface responsive pour mobile
- Statistiques d'utilisation et suivi des coûts

## Licence

[MIT License](LICENSE)

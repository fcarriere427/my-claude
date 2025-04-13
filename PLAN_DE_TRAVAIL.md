# Plan de travail - Claude Rasp MVP

## Aperçu du projet
Ce document détaille le plan de développement d'un MVP pour une interface web permettant de converser avec Claude via l'API d'Anthropic, déployée sur un Raspberry Pi.

## Objectifs
- Créer une interface web simple et fonctionnelle pour communiquer avec Claude
- Déployer l'application sur un Raspberry Pi avec des ressources limitées
- Servir d'outil d'apprentissage pour les bonnes pratiques de développement web

## Stack technique
- **Backend**: FastAPI (Python)
- **Frontend**: Vue.js
- **Base de données**: SQLite (pour l'historique de session)
- **Déploiement**: Gunicorn + Nginx

## Structure du projet
```
my-claude/
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
│   └── Dockerfile            # Optionnel
├── frontend/
│   ├── index.html
│   ├── package.json
│   ├── src/
│   │   ├── App.vue           # Composant principal
│   │   ├── main.js           # Point d'entrée Vue
│   │   ├── components/
│   │   │   ├── ChatWindow.vue
│   │   │   └── MessageInput.vue
│   │   └── services/
│   │       └── api.js        # Appels au backend
│   └── public/
│       └── style.css
└── README.md
```

## Plan d'implémentation

### Étape 1: Configuration initiale et backend (Semaine 1)
- [ ] Créer la structure du projet
- [ ] Initialiser le projet FastAPI
- [ ] Configurer l'environnement Python avec les dépendances nécessaires
- [ ] Implémenter la connexion à l'API Claude (service)
- [ ] Créer les routes API de base (nouveau message, historique)
- [ ] Tester les endpoints avec un client REST (Postman/Insomnia)

### Étape 2: Développement du frontend (Semaine 2)
- [ ] Initialiser le projet Vue.js
- [ ] Créer la structure des composants
- [ ] Développer l'interface utilisateur de base
- [ ] Implémenter les appels API vers le backend
- [ ] Gérer l'affichage des messages et des états (chargement, erreurs)

### Étape 3: Fonctionnalités de conversation (Semaine 2-3)
- [ ] Implémenter la gestion de l'historique de conversation
- [ ] Ajouter le formatage des messages (Markdown)
- [ ] Gérer les états de chargement pendant les appels à l'API
- [ ] Améliorer la gestion des erreurs
- [ ] Effectuer des tests d'intégration

### Étape 4: Déploiement sur Raspberry Pi (Semaine 3)
- [ ] Préparer le Raspberry Pi (OS, dépendances)
- [ ] Configurer Nginx comme proxy inverse
- [ ] Configurer Gunicorn pour servir l'application FastAPI
- [ ] Déployer l'application
- [ ] Tester les performances et résoudre les problèmes éventuels

### Étape 5: Finalisation et optimisations (Semaine 4)
- [ ] Optimiser les performances sur Raspberry Pi
- [ ] Améliorer l'interface utilisateur si nécessaire
- [ ] Effectuer des tests approfondis
- [ ] Documenter le processus complet
- [ ] Préparer des scripts de maintenance
- [ ] Ajouter l'affichage du coût des messages (nombre de tokens en entrée/sortie)

## Bonnes pratiques à respecter
- Utiliser le typage avec Python (type hints)
- Documenter les fonctions et méthodes
- Séparer clairement les responsabilités (services, API, UI)
- Gérer correctement les variables d'environnement pour les secrets
- Implémenter une gestion d'erreur robuste
- Écrire des tests pour les fonctionnalités essentielles

## Suivi de progression
| Étape | Statut | Date de début | Date de fin | Notes |
|-------|--------|--------------|------------|-------|
| 1     | À faire |              |            |       |
| 2     | À faire |              |            |       |
| 3     | À faire |              |            |       |
| 4     | À faire |              |            |       |
| 5     | À faire |              |            |       |

## Ressources et références
- [Documentation FastAPI](https://fastapi.tiangolo.com/)
- [Guide Vue.js](https://vuejs.org/guide/introduction.html)
- [API Anthropic](https://docs.anthropic.com/claude/reference/getting-started-with-the-api)
- [Documentation Nginx](https://nginx.org/en/docs/)
- [Documentation Gunicorn](https://docs.gunicorn.org/en/stable/)
- [Optimisation Raspberry Pi](https://www.raspberrypi.org/documentation/computers/os.html)

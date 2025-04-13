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
│   │   │   ├── MessageInput.vue
│   │   │   └── ModelSelector.vue  # Nouveau composant pour la sélection de modèle
│   │   └── services/
│   │       └── api.js        # Appels au backend
│   └── public/
│       └── style.css
└── README.md
```

## Plan d'implémentation

### Étape 1: Configuration initiale et backend (Semaine 1)
- [x] Créer la structure du projet
- [x] Initialiser le projet FastAPI
- [x] Configurer l'environnement Python avec les dépendances nécessaires
- [x] Implémenter la connexion à l'API Claude (service)
- [x] Créer les routes API de base (nouveau message, historique)
- [x] Tester les endpoints avec un client REST (Postman/Insomnia)

### Étape 2: Développement du frontend (Semaine 2)
- [x] Initialiser le projet Vue.js
- [x] Créer la structure des composants
- [x] Développer l'interface utilisateur de base
- [x] Implémenter les appels API vers le backend
- [x] Gérer l'affichage des messages et des états (chargement, erreurs)

### Étape 3: Fonctionnalités de conversation (Semaine 2-3)
- [x] Implémenter la gestion de l'historique de conversation
- [x] Ajouter le formatage des messages (Markdown)
- [x] Gérer les états de chargement pendant les appels à l'API
- [x] Améliorer la gestion des erreurs
- [x] Effectuer des tests d'intégration

### Étape 4: Déploiement sur Raspberry Pi (Semaine 3)
- [x] Préparer le Raspberry Pi (OS, dépendances)
- [x] Configurer Nginx comme proxy inverse
- [x] Configurer Gunicorn pour servir l'application FastAPI
- [x] Déployer l'application
- [x] Tester les performances et résoudre les problèmes éventuels

### Étape 5: Finalisation et optimisations (Semaine 4)
- [x] Optimiser les performances sur Raspberry Pi
- [x] Améliorer l'interface utilisateur si nécessaire
- [x] Effectuer des tests approfondis
- [x] Documenter le processus complet
- [x] Préparer des scripts de maintenance
- [x] Ajouter l'affichage du coût des messages (nombre de tokens en entrée/sortie)

### Étape 6: Amélioration des fonctionnalités (Semaine 5)
- [x] Ajouter la sélection de modèle Claude dans l'interface
- [x] Adapter le calcul des coûts en fonction du modèle sélectionné
- [x] Améliorer l'affichage des informations sur les modèles et leurs coûts
- [ ] Sauvegarder le modèle préféré pour les futures sessions
- [ ] Ajouter des statistiques d'utilisation par modèle

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
| 1     | Terminé |              |            |       |
| 2     | Terminé |              |            |       |
| 3     | Terminé |              |            |       |
| 4     | Terminé |              |            |       |
| 5     | Terminé |              |            |       |
| 6     | En cours |              |            | Implémentation de la sélection de modèle |
| 7     | En cours |              |            | Corrections de bugs d'interface |

## Bugs corrigés
- [x] Correction du problème de duplication des messages utilisateur dans l'interface (13/04/2025) - Modification du service backend pour éviter d'ajouter deux fois le même message dans l'historique

## Ressources et références
- [Documentation FastAPI](https://fastapi.tiangolo.com/)
- [Guide Vue.js](https://vuejs.org/guide/introduction.html)
- [API Anthropic](https://docs.anthropic.com/claude/reference/getting-started-with-the-api)
- [Tarification Claude API](https://www.anthropic.com/pricing#api)
- [Documentation Nginx](https://nginx.org/en/docs/)
- [Documentation Gunicorn](https://docs.gunicorn.org/en/stable/)
- [Optimisation Raspberry Pi](https://www.raspberrypi.org/documentation/computers/os.html)

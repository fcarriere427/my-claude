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

### Étape 7: Maintenance et amélioration des scripts (Semaine 6)
- [x] Correction du script de déploiement global
- [ ] Amélioration des scripts de surveillance et monitoring
- [ ] Mise en place d'un système de logs centralisé
- [ ] Automatisation des sauvegardes
- [ ] Ajout d'un script de diagnostic pour résoudre les problèmes courants

### Étape 8: Améliorations UX et nouvelles fonctionnalités (Semaine 7)
- [ ] Implémenter le thème sombre/clair avec toggle
- [ ] Ajouter la fonctionnalité d'export de conversation (PDF/Markdown)
- [ ] Ajouter une page d'aide et de documentation utilisateur
- [ ] Optimiser l'interface pour mobile

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
| 7     | En cours | 13/04/2025   |            | Correction des scripts de déploiement |
| 8     | À faire | 14/04/2025   |            | Améliorations UX |

## Bugs corrigés
- [x] Correction du problème de duplication des messages utilisateur dans l'interface (13/04/2025) - Modification du service backend pour éviter d'ajouter deux fois le même message dans l'historique
- [x] Tri des modèles par coût croissant dans le sélecteur (13/04/2025) - Mise en place d'un tri automatique dans le backend
- [x] Correction de l'affichage du sélecteur de modèles (13/04/2025) - Modification de l'interface pour afficher tous les modèles dans une seule liste au lieu d'utiliser des optgroup
- [x] Correction du problème d'absence de modèles dans le menu déroulant (13/04/2025) - Ajout de la propriété `current` dans le modèle Pydantic `ModelInfo` et dans la sérialisation API
- [x] Correction du script de déploiement qui ne se terminait pas (13/04/2025) - Création d'un script global avec meilleure gestion des erreurs et statut du service
- [x] Correction du problème d'affichage des erreurs API (13/04/2025) - Amélioration de la gestion des erreurs dans le composant frontend

## Améliorations réalisées
- [x] Ajout des modèles Claude 3.5 Haiku et Claude 3.7 Sonnet (13/04/2025)
- [x] Mise à jour des tarifs selon la tarification officielle d'Anthropic (13/04/2025)
- [x] Tri des modèles par coût croissant pour faciliter la sélection du modèle le plus économique
- [x] Simplification de l'interface de sélection des modèles pour améliorer l'expérience utilisateur (13/04/2025)
- [x] Mise en place d'un script de déploiement global robuste avec gestion des erreurs (13/04/2025)
- [x] Ajout d'un indicateur de chargement plus visible pendant le traitement des requêtes (13/04/2025)

## Améliorations planifiées
- [ ] Mise en place d'une fonctionnalité de sauvegarde du modèle préféré (cookie/localStorage)
- [ ] Ajout d'un tableau de bord de statistiques (utilisation par modèle, coûts cumulés)
- [ ] Implémentation d'un système de thèmes (clair/sombre)
- [ ] Support pour les pièces jointes et les images (via l'API Claude)
- [ ] Script de diagnostics pour identifier et résoudre rapidement les problèmes courants
- [ ] Documentation utilisateur accessible depuis l'interface

## Ressources et références
- [Documentation FastAPI](https://fastapi.tiangolo.com/)
- [Guide Vue.js](https://vuejs.org/guide/introduction.html)
- [API Anthropic](https://docs.anthropic.com/claude/reference/getting-started-with-the-api)
- [Tarification Claude API](https://www.anthropic.com/pricing#api)
- [Documentation Nginx](https://nginx.org/en/docs/)
- [Documentation Gunicorn](https://docs.gunicorn.org/en/stable/)
- [Optimisation Raspberry Pi](https://www.raspberrypi.org/documentation/computers/os.html)

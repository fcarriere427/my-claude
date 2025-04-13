#!/bin/bash
# Script de déploiement pour le frontend Claude Rasp

# Variables
DEPLOY_DIR="/var/www/claude.letsq.xyz"

# 1. Installation des dépendances
echo "Installation des dépendances..."
npm install

# 2. Construction du projet
echo "Construction du projet..."
npm run build

# 3. Copie des fichiers dans le répertoire de déploiement
echo "Déploiement des fichiers..."
sudo mkdir -p $DEPLOY_DIR/public
sudo cp -r ./dist/* $DEPLOY_DIR/public/

echo "Déploiement du frontend terminé !"
echo "L'application est accessible à l'adresse: claude.letsq.xyz"

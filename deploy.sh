#!/bin/bash
# Script global de déploiement pour Claude Rasp

echo "Début du déploiement de Claude Rasp..."
echo "-------------------------------------"

# Vérification des mises à jour du dépôt
echo "1. Mise à jour du dépôt Git..."
git pull || { echo "Erreur lors de la mise à jour Git"; exit 1; }

# Déploiement du frontend
echo "2. Déploiement du frontend..."
echo "-------------------------------------"
cd ./frontend || { echo "Erreur: Répertoire frontend non trouvé"; exit 1; }
# Build du frontend
npm install || { echo "Erreur lors de l'installation des dépendances frontend"; exit 1; }
npm run build || { echo "Erreur lors du build frontend"; exit 1; }
# Copie des fichiers vers le répertoire de déploiement
sudo cp -r ./dist/* /var/www/claude.letsq.xyz/ || { echo "Erreur lors de la copie des fichiers frontend"; exit 1; }
echo "*** Frontend: OK, deployed to /var/www/claude.letsq.xyz/"

# Retour au répertoire racine
cd ..

# Déploiement du backend
echo "3. Déploiement du backend..."
echo "-------------------------------------"
cd ./backend || { echo "Erreur: Répertoire backend non trouvé"; exit 1; }
# Installation des dépendances Python si nécessaire
source .venv/bin/activate
pip install -r requirements.txt || { echo "Erreur lors de l'installation des dépendances backend"; exit 1; }
# Redémarrage du service
sudo systemctl restart my-claude.service || { echo "Erreur lors du redémarrage du service"; exit 1; }
# Affichage du statut sans bloquer le script
sudo systemctl status my-claude.service --no-pager
echo "*** Backend: voir ci-dessus le statut après redémarrage du service"

echo "-------------------------------------"
echo "Déploiement terminé avec succès !"
echo "L'application est accessible à l'adresse: claude.letsq.xyz"

exit 0

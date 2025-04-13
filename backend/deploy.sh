#!/bin/bash
# Script de déploiement pour Claude Rasp

# Variables
DEPLOY_DIR="/var/www/claude.letsq.xyz"
SERVICE_NAME="claude-rasp"

# 1. Création du répertoire de déploiement si nécessaire
echo "Création du répertoire de déploiement..."
sudo mkdir -p $DEPLOY_DIR

# 2. Copie des fichiers
echo "Copie des fichiers backend..."
sudo cp -r ./app $DEPLOY_DIR/
sudo cp requirements.txt $DEPLOY_DIR/

# 3. Installation des dépendances
echo "Installation des dépendances Python..."
cd $DEPLOY_DIR
sudo pip install -r requirements.txt

# 4. Configuration du service systemd pour Gunicorn
echo "Configuration du service systemd..."
cat > /tmp/claude-rasp.service << EOF
[Unit]
Description=Gunicorn service pour Claude Rasp
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=$DEPLOY_DIR
ExecStart=$(which gunicorn) app.main:app --workers 2 --worker-class uvicorn.workers.UvicornWorker --bind unix:$DEPLOY_DIR/claude-rasp.sock
Restart=on-failure

[Install]
WantedBy=multi-user.target
EOF

sudo mv /tmp/claude-rasp.service /etc/systemd/system/

# 5. Démarrage du service
echo "Démarrage du service..."
sudo systemctl daemon-reload
sudo systemctl enable $SERVICE_NAME
sudo systemctl restart $SERVICE_NAME

echo "Déploiement terminé !"
echo "L'application est accessible à l'adresse: claude.letsq.xyz"

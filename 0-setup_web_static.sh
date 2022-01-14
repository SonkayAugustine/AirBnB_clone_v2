#!/usr/bin/env bash
# setup my web server for the deployment of web_static
sudo apt-get update
sudo apt-get -y upgrade
sudo apt-get -y install nginx
sudo mkdir -p /data_web_static/releases/test /data/_web_static/shared
echo "Testing it out" | sudo tee /data_web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx restart

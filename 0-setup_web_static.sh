#!/usr/bin/env bash
# setup my web server for the deployment of web_static
sudo apt-get update
sudo apt install -y nginx
sudo mkdir -p /data/web_static/shared /data_web_static/releases/test/
sudo echo "<html>
  <head>
  </head>
  <body>
        Holberton School
  </body>
</html>" | sudo tee /data_web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\alias /data/web_static/current;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx start

#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static

sudo apt-get update
sudo apt-get install nginx
sudo ufw allow 'Nginx HTTP'

# creating directories
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

# creating an index.html file in test dir
sudo touch /data/web_static/releases/test/index.html

# adding some temporary html
sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

#creating a symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# giving ownership to /data/ directory to user ubuntu
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of 
# /data/web_static/current/ to hbnb_static(ex https://mydomainname.tech/hbnb_static)
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

sudo service nginx restart

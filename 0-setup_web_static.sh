#!/usr/bin/env bash
# Install and Start Nginx with the updated config

sudo apt-get update
sudo apt-get -y install nginx

# Create necessary directories if they don't exist
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

# Create HTML file
FILE="<html>
<head>
</head>
<body>
    Holberton School
</body>
</html>"
echo "$FILE" > /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
SERVER_CONFIG="
server {
    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }
}"
sudo bash -c "echo '$SERVER_CONFIG' > /etc/nginx/sites-available/default"

sudo service nginx restart

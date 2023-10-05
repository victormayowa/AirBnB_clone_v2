#!/usr/bin/env bash
# Bash script to set up web servers for deployment of web_static

# Install Nginx if not already installed
if ! command -v nginx &> /dev/null
then
    sudo apt-get -y update
    sudo apt-get -y install nginx
fi

# Create necessary folders if they don't exist
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file
echo "<html><head></head><body>Holberton School</body></html>" | sudo tee /data/web_static/releases/test/index.html

# Create symbolic link and update ownership
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
CONFIG_BLOCK="location /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n"
sudo sed -i "/^\s*server\s*{/a $CONFIG_BLOCK" /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart

exit 0

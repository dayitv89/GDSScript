# install nginx, nodejs 8.x, PM2
# configure everything on new aws-ubuntu instance
# https://medium.com/@utkarsh_verma/configure-nginx-as-a-web-server-and-reverse-proxy-for-nodejs-application-on-aws-ubuntu-16-04-server-872922e21d38

# ubuntu updates
sudo apt-get update
sudo apt-get upgrade -y

# nginx install
sudo apt-get install nginx -y
# sudo systemctl status nginx    # To check the status of nginx
sudo systemctl start nginx     # To start nginx
sudo systemctl enable nginx

# node 8.x install 
# https://nodejs.org/en/download/package-manager/#debian-and-ubuntu-based-linux-distributions
curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
sudo apt-get install -y nodejs
sudo apt-get install -y build-essential

# check node version
node -v # 8.x
npm -v  # 5.3 or 5.x

# install express and PM2 
mkdir ~/www
cd ~/www
echo '{}' > package.json
npm i express
sudo npm i pm2 -g

# write some code on app.js
# $ nano ~/www/app.js
#	var express = require('express');
#	var app = express();
#	app.get('/', function(req, res){
#   		res.send("Hello World!");
#	});
#	app.listen(3000, 'private_ip_address');

# run pm2 for node server
# $ pm2 start ~/www/app.js

# start server and basic routing in nginx 
# https://medium.com/@utkarsh_verma/configure-nginx-as-a-web-server-and-reverse-proxy-for-nodejs-application-on-aws-ubuntu-16-04-server-872922e21d38

# get private ip by
# $ wget -q -O - 'http://169.254.169.254/latest/meta-data/local-ipv4'

# put this config in nginx to node server
# sudo rm /etc/nginx/sites-available/default
# sudo nano /etc/nginx/sites-available/default
#	server {
#    		listen 80;
#    		server_name your_domain.com;
#    		location / {
#        		proxy_pass http://private_ip_address:3000;
#        		proxy_http_version 1.1;
#        		proxy_set_header Upgrade $http_upgrade;
#        		proxy_set_header Connection 'upgrade';
#        		proxy_set_header Host $host;
#        		proxy_cache_bypass $http_upgrade;
#     		}
#	} 

# restart nginx after everything
# $ sudo nginx -t
# $ sudo /etc/init.d/nginx reload


# reload nginx after config
# sudo /etc/init.d/nginx reload

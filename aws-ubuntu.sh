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


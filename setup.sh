# Install any dependencies you need here (you can run more than apt-get, and
# this script runs as root)
apt-get -y install openjdk-8-jdk

# This last line must stay to avoid ssh errors
ssh-keyscan -t rsa github.com >> ~/.ssh/known_hosts

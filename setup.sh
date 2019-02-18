# Install any dependencies you need here (you can run more than apt-get, and
# this script runs as root)
wget https://download.java.net/java/ga/jdk11/openjdk-11_linux-x64_bin.tar.gz
tar xzf openjdk-11_linux-x64_bin.tar.gz

# Testing to get media.jar to work
echo y | apt-get install cmake libfreetype6-dev libfontconfig1-dev xclip

# This last line must stay to avoid ssh errors
ssh-keyscan -t rsa github.com >> ~/.ssh/known_hosts

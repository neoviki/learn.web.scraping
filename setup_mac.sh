#sudo pip3 install selenium --upgrade
#Check Software Installed
brew install wget
#sudo pip2 install selenium --upgrade
brew install geckodriver
wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-macos.tar.gz 
gunzip geckodriver*.tar.gz 
tar -xvf geckodriver*.tar
chmod +x geckodriver
sudo rm /usr/bin/geckodriver
sudo rm /usr/local/bin/geckodriver
sudo mv geckodriver /usr/local/bin/

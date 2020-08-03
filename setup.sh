# APT installs 

apt-get install sox
apt-get install mysql-server
apt-get install mysql-client

# pip installs

pip3 install mysql-connector-python
pip3 install getpass
pip3 install sox
pip3 install tabulate

# making directories

mkdir ~/calApp
cp -r . ~/calApp
cd ~/calApp
chmod +x *

echo "alias calel='~/calApp/calel.sh'" >> ~/.bash_aliases
source ~/.bash_aliases
./init.sh

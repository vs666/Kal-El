echo "Create a mysql user for the purpose of calApp..."
read -p "Do you possess a user named '"$USER"' in mysql users [Y/N]" op
if  [ $op == 'Y' ]  ||  [ $op == 'y' ]
then
    echo "Please make sure you have account named '$USER'@'localhost' and you know the password"
else
    read -p "Choose a password for sql id '$USER'@'localhost' :" pswd
    touch tmp.sql
    touch tmp.sql
    echo "CREATE USER '$USER'@'localhost' IDENTIFIED BY '$pswd';" >> tmp.sql
    echo "GRANT ALL PRIVILEGES ON *.* TO '$USER'@'localhost';" >> tmp.sql
    echo "quit" >> tmp.sql
    echo "Enter sudo password."
    sudo mysql -u root -p < tmp.sql
    rm tmp.sql
fi

python3 ./script.py


#sudo apt-get install libsqlite3-dev
#sudo apt install python3.10-venv
#apt install python3.10-venv


python3 -m pip install --upgrade build
python3 -m build
cd dist/
ls
pip3 install CHANGEME_PACKAGE_NAME-0.0.1.tar.gz 
cd ..

testcli -h
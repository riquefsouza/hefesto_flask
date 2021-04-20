python3 -m venv flask-env
source flask-env/bin/activate
ou
deactivate

code .

git init

touch .gitignore
__pycache__
flask-env
.DS_Store

git add .

git commit -m "hefesto-fastapi"

python3 -m pip install --upgrade pip

pip3 install flask-sqlalchemy flask-migrate flask-script flask-wtf flask-login

python3 run.py runserver


git clone https://github.com/riquefsouza/hefesto_flask.git


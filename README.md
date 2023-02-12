Hello ! In this project, I implemented a simple task-manager.
To start my project locally you need write some simple commands:

1. python3 -m venv env
2. source env/bin/activate (Windows : venv/Scripts/activate)
3. pip3 install -r requirements.txt
4. python3 manage.py migrate
5. Generate your secret_key here : https://djecrety.ir/ and IMPORTANT! Paste it SECRET_KEY (that`s your djando secret key to run project ) into settings or .env.sample file to load secret information from AND RENAME FILE TO .env !
6. python3 manage.py runserver

If you want to create more data just login by this superuser data :
username : admin
password: admin 
python3 -m venv env

source env/bin/activate 3 git clone https://github.com/Rav944/Tsilevart.git

cd Tsilevart

pip install -r requirements.txt

./manage.py migrate 

./manage.py import_users_data <file path>
  
./manage.py runserver

http://127.0.0.1:8000/tsilevart/users/ -> users list

http://127.0.0.1:8000/tsilevart/users/<pk> -> single user(you can also update points here)
  
  
To Do:

  1.Test

  2.Pagination

  3.Nicer information about a successful user update
  
  4.Dockerization


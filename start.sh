sudo apt-get update
sudo apt-get install python3 python3-virtualenv -y
virtualenv env
. env/bin/activate
pip install django
pip install django-emailuser
django-admin startproject wr
cd wr
python manage.py makemigrations emailuser
python manage.py migrate
python manage.py createsuperuser
python manage.py dumpdata auth.User --indent 4 > superuser.json
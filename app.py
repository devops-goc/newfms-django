import os
import time
import datetime
import logging
logging.basicConfig(encoding='utf-8', level=logging.INFO)

def log(m):
    logging.info(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}; {m}")

os.system('/home/user/venv/bin/python manage.py startapp app_newfms')
os.system('/home/user/venv/bin/python manage.py makemigrations')
os.system('/home/user/venv/bin/python manage.py migrate --noinput')
os.system('nohup /home/user/venv/bin/python manage.py runserver 0.0.0.0:8080 &')
while True:
    log('running...')
    time.sleep(600)

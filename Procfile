release: python ./painel/manage.py makemigrations
release: python ./painel/manage.py migrate
web: gunicorn painel.wsgi
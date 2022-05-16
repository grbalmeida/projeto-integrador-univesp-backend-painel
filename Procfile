release: python ./painel/manage.py makemigrations & python ./painel/manage.py migrate
web: gunicorn ./painel/painel.wsgi
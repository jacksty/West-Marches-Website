web: python manage.py migrate
web: python manage.py loaddata fixture.json
web: waitress-serve --port=$PORT westmarches.wsgi:application

# Quick Start

````
python manage.py runserver
````

# Setup

```
.env
DATABASE_NAME=chaincue-real-estate-db
DATABASE_USER=admin
DATABASE_PASSWORD=admin
DATABASE_HOST=localhost
DATABASE_PORT=5432
```

```
docker compose up -d
pip install -r requirements.txt
python manage.py runserver
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser --username admin --email admin@example.com
```

# Useful Commands

```
django-admin startapp ...
```

```
python manage.py showmigrations
```

### migrate

```
python manage.py makemigrations
python manage.py migrate
```

### if problem with migration

```
python manage.py migrate country zero --fake
```

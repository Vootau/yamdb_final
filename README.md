![Build Status](https://github.com/github/docs/actions/workflows/main.yml/badge.svg)(https://github.com/vootau/yamdb_final/workflows/main.yml)

### How to start project:

Clone repo and go to directory in command line:

```
git clone https://github.com/yandex-praktikum/yamdb_final.git
```

```
cd yamdb_final
```

Create and activate virtual environment:

```
python -m venv env
```

```
source venv/Scripts/activate
```

```
python -m pip install --upgrade pip
```

Install dependences from requirements.txt:

```
pip install -r ./api_yamdb/requirements.txt
```

Make migrations:

```
cd api_yamdb
python manage.py migrate
```

Run project:

```
python manage.py runserver

python manage.py createsuperuser
```
Server_ip:

```
158.160.5.174
```


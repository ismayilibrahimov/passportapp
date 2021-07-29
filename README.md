## Prerequisite

- mysql v8.0.23
- python 3.9.2
- git

## Installation

```bash
git clone https://github.com/ismayilibrahimov/passportapp.git
cd passportapp
```

create virtualenv and activate

```bash
python -m virtualenv venv
source venv/scripts/activate (windows) or venv/bin/activate (linux, unix)
```

```bash
pip install -r requirements.txt
```

add database credentials to settings.py file

```bash
py manage.py makemigrations
py manage.py migrate
py manage.py runserver
```

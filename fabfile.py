from fabric.api import local

def generate_fixtures():
    local("python manage.py generate_fixture issues.__all__ --indent=4 > issues/initial_data.json")

def reset():
    local("rm db/db.sqlite3")
    local("python manage.py syncdb")
    local("python manage.py loaddata issues/initial_data.json")

def update():
    local("pip install -r requirements.txt")
    reset()
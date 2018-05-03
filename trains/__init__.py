from trains.web import app
from trains.models import create_tables

def main():
    create_tables()
    app.run('localhost', debug=True)

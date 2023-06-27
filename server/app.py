from flask import request, make_response, session, abort
from flask_restful import Resource

from config import app, db, api
from models import Contact

class Home(Resource):
    def get(self):
        return 'portfolio time!'

api.add_resource(Home, '/')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
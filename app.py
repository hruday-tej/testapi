from flask import Flask
from resources.emp import Emp
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

api.add_resource(Emp,'/emp')

    

app.run(debug=True, port='8800')
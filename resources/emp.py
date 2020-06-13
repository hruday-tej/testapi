from flask import jsonify
from flask_restful import Resource,reqparse
from db import query

class Emp(Resource):
    def get(self):

        parser = reqparse.RequestParser()
        parser.add_argument('empno',type=int, required=True, help="empno cannot be left blank!")
        data = parser.parse_args()
        # print(data)
        try:
            return query(f'''SELECT * FROM testapi.emp WHERE empno={data['empno']};''')
        except:
            return {"message":"There was an error connecting to emp table"},500
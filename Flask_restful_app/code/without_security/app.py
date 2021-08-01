from flask import Flask
from flask_restful import Resource, Api

#defining flask app
app = Flask(__name__)

api = Api(app)

"""
Create a Student resource that inhereits Resource Class. In Flask-RESTful, all Resources are Classes that inherit from Resource class

"""

## defining resources
class Student(Resource):
    # redefine get method
    def get(self,name):
        return({'student':name})


# Add resources to the API using add_resources
api.add_resource(Student,'/student/<string:name>')

# Run app on which port
app.run(port=4999)

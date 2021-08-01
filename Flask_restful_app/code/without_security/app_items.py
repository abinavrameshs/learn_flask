from flask import Flask, request
from flask_restful import Resource, Api

#defining flask app
app = Flask(__name__)

api = Api(app)

"""
Create a Student resource that inhereits Resource Class. In Flask-RESTful, all Resources are Classes that inherit from Resource class

Flask-RESTful can return dictionaries and we dont need to use jsonify to convert dictionaries to Strings using jsonify

"""
items = [

]

## defining resources
class Item(Resource):
    # redefine get method
    def get(self,name):
        for item in items :
            if(item['name']==name):
                return(item)
        return({'item':'null'}, 404)
    
    def post(self,name):
        sent_dict=request.get_json()
        dict_item = {'name':name, 'price':sent_dict['price']}
        items.append(dict_item)
        return(dict_item,201)

class ItemList(Resource):
    def get(self):
        return({'items' : items})

# Add resources to the API using add_resources
api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList, '/items')

# Run app on which port
app.run(port=4999, debug=True)

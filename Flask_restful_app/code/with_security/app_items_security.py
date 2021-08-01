from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

#defining flask app
app = Flask(__name__)

api = Api(app)

# Set app's secret key
app.secret_key = "abinav"

jwt = JWT(app,authenticate,identity) # creates a new end point called /auth , to which we send username and password and get a auth id as a response


"""
Create a Student resource that inhereits Resource Class. In Flask-RESTful, all Resources are Classes that inherit from Resource class

Flask-RESTful can return dictionaries and we dont need to use jsonify to convert dictionaries to Strings using jsonify

Every item has a name and a price
""" 
items = [

]

## defining resources
class Item(Resource):
    # redefine get method
    @jwt_required()
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
    
    def delete(self,name):
        # we use `global items` to tell to the program that whatever variable called "items" is reference d in the program is indeed the global variabe items, not a local variable
        global items
        items = list(filter(lambda x: ( x['name']!=name ), items)) 
        return({"message" : f"Item with name {name} has been deleted. Use GET API to verify if item is deleted"})

    def put(self,name):
        data = request.get_json() # we get a dict from the input name and price
        item=next(filter(lambda x : x['name']==name,items),None)
        if item :
            item.update(data)
            #self.delete(name)
            #items.append(item)
        else : 
            item = {"name" : name, "price" : data['price']}
            items.append(item)
        return(item)

class ItemList(Resource):
    def get(self):
        return({'items' : items})

# Add resources to the API using add_resources
api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList, '/items')

# Run app on which port
app.run(port=4999, debug=True)

from flask import Flask, jsonify, request,render_template

app = Flask(__name__)

"""
# We define a list of stores.
Each store is a dictionary with a name and a list of items.
Each item is a disctionary with a name and a price

"""

stores = [
{
    'name' : 'First Store',
    'items' : [
        {
            'name' : 'item1_store1',
            'price' : 1
        },
        {
            'name' : 'item2_store1',
            'price' : 2
        },
        {
            'name' : 'item3_store1',
            'price' : 3
        }
    ]
},
{
    'name' : '2nd Store',
    'items' : [
        {
            'name' : 'item1_store2',
            'price' : 11
        },
        {
            'name' : 'item2_store2',
            'price' : 22
        },
        {
            'name' : 'item3_store2',
            'price' : 33
        }
    ]
},
{
    'name' : '3rd Store',
    'items' : [
        {
            'name' : 'item1_store3',
            'price' : 111
        },
        {
            'name' : 'item2_store3',
            'price' : 222
        },
        {
            'name' : 'item3_store3',
            'price' : 333
        }
    ]
}

]



"""
While developing a flask web application, we create a web server, that deals with GET or put requests
GET Store
PUT Store
GET Item
PUT Item
"""


@app.route('/')
def home():
    # render_template automatically looks for index.html under the templates folder
    return(render_template('index.html'))

# POST method for a particular store -- to create a new store
@app.route('/store', methods =['POST'] )
def create_store():
    
    print(f"Creating new store \n")

    store_dict=request.get_json()
    new_store_dict = {
        'name' : store_dict['name'],
        'items' : []
    }

    stores.append(new_store_dict)
    return(jsonify(new_store_dict))

# Get method for a store - get a given store with a given name
@app.route('/store/<string:name>',methods = ['GET'])
def return_store(name):
    print(f"The name of the store to get is {name}\n\n")
    store_dict ={'message' : 'Store not found'}
    for i in stores : 
        if(i['name']==name):
            store_dict = i
        else : 
            continue
    return(jsonify(store_dict))

# Get all stores at once

@app.route('/store',methods = ['GET'])
def return_all_stores():
    return(jsonify({'stores': stores}))

# POST an item onto a store with a name : /store/<string:name>/item {name: , price : }

@app.route('/store/<string:name>/item', methods=['POST','PUT'])
def create_new_item(name):
    item = request.get_json()
    new_dict = {
        'name' : item['name'],
        'price' : item['price']
    }
    for store in stores:
        if(name==store['name']):
            store['items'].append(item)
            return(jsonify(item))
    return(jsonify({'message' : "Error : Store with name not found"}))

    


# Get items of a store

@app.route('/store/<string:name>/item', methods=['GET'])
def return_all_items_of_a_store(name):
    for store in stores:
        if(store['name']==name):
            items = store['items']
            return jsonify({'items' : items})
            
    return(jsonify({'message' : 'Store not found and hence cannot retreive items for the store'}))

app.run(port=4999)
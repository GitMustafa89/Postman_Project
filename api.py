from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Welcome to My store"

stores = [
    {
        'name': 'My Store',
        'items':[
            {'name': 'flowers', 'price': 1000}
                ]
    },
    {
        'name': 'My Store 2',
        'items':[
            {'name': 'books', 'price': 2000}
                ]
    }
  
]

@app.route('/store')
def get_all_store_name():
    return jsonify({'stores': stores})

# Create store 
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify({'store': new_store})

# Show store list
@app.route("/showstore")
def showstore():
    return jsonify({'list':stores})

# Fetching the store name
@app.route('/store/<string:name>')
def get_store_by_name(name):
    for store in stores:
        if(store['name'] == name):
            return jsonify({'store': store})
    return jsonify({'message': 'store not found'})

# Add items name and price in the store
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if(store['name'] == name):
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify({'item': new_item})
    return jsonify({'message': 'store not found'})


if __name__ == "__main__":
    app.run(debug=True)  # run app in debug mode on
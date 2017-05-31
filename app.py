from flask import Flask, jsonify, request

app = Flask(__name__)
stores = [{
        'name': "Tesco",
        'items': [{'name': 'Butter Squash', 'price': 2.99}]},
        {'name': "Sainsbury",
        'items': [{'name': 'Coconut', 'price': 1.99}]
}]

#POST - used to recieve data
#GET - Used to send data back only

# POST /store data: {name:}
@app.route('/store', methods=['POST']) # 'http://127.0.0.1:5000/store'
def create_store():
    request_data = request.get_json()
    new_store = {
        'name' : request_data['name'],
        'items' : []
    }
    stores.append(new_store)
    return jsonify(new_store)

# GET /store/<name> # '# 'http://127.0.0.1:5000/store/some_name'
@app.route('/store/<string:name>')
def get_store(name):
    #iterate over stores
    #if the store name matches, return it
    #if none match, return an error message
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message' : 'store not found'})

# GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})

# POST /store/<name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST']) # 'http://127.0.0.1:5000/store'
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return  jsonify({'message' : 'store not found'})

# GET /store/<name>/item # '# 'http://127.0.0.1:5000/store/some_name'
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message' : 'store not found'})

app.run(port=5000)

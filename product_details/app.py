
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)
app.config['DEBUG']= True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///product.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db=SQLAlchemy(app)
ma=Marshmallow(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(100))

    def __init__(self, name, price, quantity, description):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'price', 'quantity')

schema = ProductSchema()
schemas = ProductSchema(many=True)

# Alternative : To handle formatting of data we use marshmallow
def format_result(obj):
  result = {}
  print(obj.quantity, obj.id, obj.name)
  result['id'] = obj.id
  result['name'] = obj.name
  result['price'] = obj.price
  result['quantity'] = obj.quantity
  result['description'] = obj.description
  return result

@app.route('/products', methods=['GET'])
def get_products():
    #res = []

    products = Product.query.all()
    print(products)
    result = schemas.dump(products)
    # for product in products:
    #     r = format_result(product)
    #     res.append(r)
    return jsonify(result)

@app.route('/products/<id>', methods=['GET'])
def get_product(id):
    product = Product.query.get(id)
    res = schema.dump(product)
    #res = format_result(product)
    return jsonify(res)

@app.route('/products/<id>', methods=['PUT'])
def update_product(id):
    name = request.json['name']
    price = request.json['price']
    quantity = request.json['quantity']
    description  = request.json['description']

    product = Product.query.get(id)
    product.name = name
    product.quantity = quantity
    product.description = description
    product.price = price

    db.session.commit()
    res = schema.dump(product)
    #res = format_result(product)
    return jsonify(res)

@app.route('/products/<id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get(id)
    if not product:
        return 'ID NOT FOUND'
    db.session.delete(product)
    db.session.commit()
    res = schema.dump(product)
    #res = format_result(product)
    return jsonify(res)


@app.route('/products', methods=['POST'])
def add_product():
    name = request.json['name']
    price = request.json['price']
    quantity = request.json['quantity']
    description  = request.json['description']
    # Check if product with same name exists
    obj = get_product_by_name(name)
    if not obj:
        obj = Product(name, price, quantity, description)
    else:
        obj.price = price
        obj.quantity = quantity
        obj.description = description
    db.session.add(obj)
    db.session.commit()
    res = schema.dump(obj)
    #res = format_result(obj)
    return jsonify(res)

def get_product_by_name(name):
    res = Product.query.filter(Product.name == name).first()
    return res

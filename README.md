# Rest_APIs
Sample project to perform CRUD operations via REST APIs using python, flask, sqlalchemy, marshmallow

Install requirements and deps
----------------------------

> python3 -m venv myproject

> virtualenv myproject

> source myproject/bin/activate

> pip3 install flask

> pip3 install flask-sqlalchemy

> pip3 install flask-marshmallow

> pip3 install marshmallow-sqlalchemy

> pip3 freeze > requirements.txt

> export FLASK_APP=/Users/jjayaramrask/Documents/Personal/Study/Rest_APIs/product_details/app.py

# create db
python
> from product_details.app import db

> db.create_all()

> exit()

flask run

APIs
-------------------


Get All Products:
-------------------
curl --location --request GET "http://127.0.0.1:5000/products"

Add Product:
-------------------
curl --location --request POST "http://127.0.0.1:5000/products" \
  --header "Content-Type: application/json" \
  --data "{
\"name\": \"Coke\",
\"price\": 35,
\"quantity\": 200,
\"description\": \"Popular Cold drink\"
}"

get product detail by id
-------------------
curl --location --request GET "http://127.0.0.1:5000/products/1"

update product
-------------------
curl --location --request PUT "http://127.0.0.1:5000/products/1" \
  --header "Content-Type: application/json" \
  --data "{
\"name\": \"Coke\",
\"price\": 35,
\"quantity\": 2000,
\"description\": \"Popular Cold drink\"
}"

Delete product
------------------
curl --location --request DELETE "http://127.0.0.1:5000/products/3"

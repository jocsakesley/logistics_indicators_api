
from flask import Flask


from src.infra.db import db
from src.infra.routes.customer_services_routes import cs_bp
from src.infra.routes.customers_routes import customer_bp


app = Flask(__name__)

db.init_db()

app.register_blueprint(cs_bp, url_prefix='/v1')
app.register_blueprint(customer_bp, url_prefix='/v1')









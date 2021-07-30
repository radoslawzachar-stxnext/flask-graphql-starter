from flask import Flask, jsonify
from flask_graphql import GraphQLView

from app_name.graphql_schema import schema

app = Flask(__name__)


@app.route("/")
def hello_world():
    return jsonify(hello="world")


app.add_url_rule(
    "/graphql", view_func=GraphQLView.as_view("graphql", schema=schema, batch=True)
)

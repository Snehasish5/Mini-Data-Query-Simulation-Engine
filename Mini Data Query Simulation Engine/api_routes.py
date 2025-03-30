from flask import Blueprint, request, jsonify
from query_processor import convert_to_sql, explain_query, validate_query
from database import get_mock_data
from functools import wraps
import os

# API Blueprint
api_blueprint = Blueprint("api", __name__)

# API Key authentication
API_KEY = os.getenv("API_KEY", "OGNJUdjdejrjr6258hjdfj")

def require_api_key(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if request.headers.get("X-API-KEY") != API_KEY:
            return jsonify({"error": "Unauthorized"}), 403
        return f(*args, **kwargs)
    return decorated_function

@api_blueprint.route("/query", methods=["POST"])
@require_api_key
def query():
    data = request.json
    if not data or "query" not in data:
        return jsonify({"error": "No query provided"}), 400

    nl_query = data["query"]
    sql_query = convert_to_sql(nl_query)
    return jsonify({"query": nl_query, "sql": sql_query, "data": get_mock_data()["sales"]})

@api_blueprint.route("/explain", methods=["POST"])
@require_api_key
def explain():
    data = request.json
    if not data or "query" not in data:
        return jsonify({"error": "No query provided"}), 400

    return jsonify(explain_query(data["query"]))

@api_blueprint.route("/validate", methods=["POST"])
@require_api_key
def validate():
    data = request.json
    if not data or "query" not in data:
        return jsonify({"error": "No query provided"}), 400

    return jsonify(validate_query(data["query"]))
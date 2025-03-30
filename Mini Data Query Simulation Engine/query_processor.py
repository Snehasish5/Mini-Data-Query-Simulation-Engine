def convert_to_sql(nl_query):
    if "total sales" in nl_query.lower():
        return "SELECT SUM(sales) FROM sales;"
    return "SELECT * FROM sales;"

def explain_query(nl_query):
    return {"explanation": f"Interpreted as: {convert_to_sql(nl_query)}"}

def validate_query(nl_query):
    return {"valid": "sales" in nl_query.lower()}
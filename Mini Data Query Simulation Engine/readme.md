# Mini Data Query Simulation Engine Objective

## Overview

This README provides comprehensive instructions on setting up the API Query Interface and details about how to use the API.

## Setup Instructions

### Installation Steps

- Clone the Repository

        git clone https://github.com/your-repository/api-query-interface.git
        cd api-query-interface
- Create a Virtual Environment (Optional but recommended)

        python -m venv venv
        source venv/bin/activate    # On Windows use `venv\Scripts\activate`

- Run the application

        python app.py

- Access the API Interface

Open your browser and navigate to: http://127.0.0.1:5000

## API Documentation

- Base URL

            http://127.0.0.1:5000

- Endpoints

    /api/query

1. Method: POST
2. Description: Sends a query to the database and returns results.
3. Request Body:


            {
            "query": "sales"
            }
4. Response:
    Success (200):

            {
            "data": [
                {
                "product": "Laptop",
                "sales": 500
                },
                {
                "product": "Phone",
                "sales": 300
                }
            ],
            "query": "sales",
            "sql": "SELECT * FROM sales;"
            }

5. Error (400):

            {
            "error": "Bad Request. Query not valid."
            }

## Usage

To use the API, enter your query in the input field and click "Send Query." The result will be displayed below, showing the data retrieved from the database.

## Troubleshooting

404 Not Found Error

- Ensure the server is ning and accessible at the specified address.
- Invalid Query
- Check your query syntax. The backend expects queries in a specific format.
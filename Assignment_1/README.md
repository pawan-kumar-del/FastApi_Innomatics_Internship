# IN126014402_fastapi

## Project Overview

The project demonstrates the implementation of a simple **E-commerce API using FastAPI**.

The API is tested using **Swagger UI** and all output screenshots are included for evaluation.

## Features Implemented

* Home endpoint for API welcome message
* Retrieve all products with total count
* Get product details by product ID
* Display only in-stock products
* Filter products based on category, price, and availability
* Search products using keyword
* Identify best deal and premium product
* Store summary information

## Technologies Used

* Python
* FastAPI
* Uvicorn
* Swagger UI (API Testing)

## How to Run the API:

1. Install dependencies:
pip install fastapi uvicorn

2. Run the server:
uvicorn main:app --reload

3. Open Swagger UI

http://127.0.0.1:8000/docs